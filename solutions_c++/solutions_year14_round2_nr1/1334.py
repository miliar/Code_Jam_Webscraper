#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;

#define INF 2000000000

// Precondition: v is sorted
int minimize(vector<int> v)
{
	int p = v.size();
	int mint=INF;
	for(int m=1; m<=v[p-1]; ++m) {
		int t=0;
		for(int i=0; i<v.size(); ++i) t += abs(v[i]-m);
		if(t<mint) {
			mint = t;
		}
	}
	if(mint == INF) mint = 0;
	return mint;
}

int main()
{
	
	//g s = "aabbcc";
	//string t;
	ifstream fin("identical.in");
	ofstream fout("identical.out");
	int t; fin >> t;
	//cout << s << ' ' << t << ' ' << s.size() << endl;
	for(int i=0; i<t; ++i) {
		fout << "Case #" << i+1 << ": ";
		vector<string> v;
		int n; fin >> n;
		for(int j=0; j<n; ++j) {
			string s; fin >> s;
			v.push_back(s);
		}
		
		int flag=1;
		vector<string> v_uni;
		int p = v.size();
		for(int j=0; j<p-1; ++j) {
			string s1,s2;
			unique_copy(v[j].begin(),v[j].end(),std::back_inserter(s1));
			unique_copy(v[j+1].begin(),v[j+1].end(),std::back_inserter(s2));
			if(s1!=s2) {
				flag=0;
				break;
			}
			if(j==0) v_uni.push_back(s1);
			v_uni.push_back(s2);
		}
		if(flag==0) {fout << "Fegla Won\n"; continue;}
		
		// get counts of all characters from all strings
		vector<int> cts[105];
		for(int k=0; k<v.size(); ++k) {
			int ind=1, ind2=0, ct=1;
			while(ind < v[k].size()) {
				if(v[k][ind] != v[k][ind-1]) {
					cts[ind2].push_back(ct);
					++ind2;
					ct=0;
				}
				++ct; ++ind;
			}
			cts[ind2].push_back(ct);
		}
		
		int ans=0;
		for(int j=0; j<v_uni[0].size(); ++j) {
			sort(cts[j].begin(), cts[j].end());
			ans += minimize(cts[j]);
		}
		fout << ans << endl;
	}
}
