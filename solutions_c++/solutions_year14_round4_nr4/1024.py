#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
using namespace std;

int get_trie1(vector <string> v) {
	set <string> ans;
	ans.insert("");
	for (int i=0; i<v.size(); i++)
		for (int j=1; j<=v[i].size(); j++)
			ans.insert(v[i].substr(0,j));
	return ans.size();
}
int get_trie(vector <string> v) {
	vector <string> ans;
	for (int i=0; i<v.size(); i++)
		for (int j=0; j<=v[i].size(); j++) {
			string t=v[i].substr(0,j);
			if (count(ans.begin(),ans.end(),t)==0)
				ans.push_back(t);
		}
	return ans.size();
}

void printvi(vector <int> vi) {
	for (int i=0; i<vi.size(); i++)
		cout << vi[i] << " ";
	cout << endl;
}

int get_tries1(vector <string> v,vector <int> bf,int N) {
	int ans=0;
	for (int i=0; i<N; i++) {
		vector <string> t;
		for (int j=0; j<v.size(); j++)
			if (bf[j]==i)
				t.push_back(v[j]);
		ans+=get_trie(t);
	}
	return ans;
}

int get_tries(vector <string> v,vector <int> bf,int N) {
	int ans=0;
	vector <vector <string> > vvs(N);
	for (int j=0; j<v.size(); j++)
		vvs[bf[j]].push_back(v[j]);
	for (int i=0; i<N; i++) {
		ans+=get_trie(vvs[i]);
	}
	return ans;
}

string solve(vector <string> v,int N) {
	int ans=0, M=v.size();
	map <int,int> m;
	for (int i=0; i<1<<M; i++)
		for (int j=0; j<1<<M; j++) {
			vector <int> bf;
			for (int k=0; k<M; k++)
				bf.push_back( ((i&(1<<k))!=0)+((j&(1<<k))!=0)*2);
			// check ar visi:
			bool visi=true;
			for (int k=0; k<N; k++)
				if (count(bf.begin(),bf.end(),k)==0) {
					visi=false; break;
				}
			if (!visi)
				continue;
			for (int k=0; k<bf.size(); k++) // ar uztenka servu
				if (bf[k]>=N) {
					visi=false; break;
				}
			if (visi) {
				//printvi(bf);
				int tr=get_tries(v,bf,N);
				//cout << tr << endl;
				ans=max(ans,tr);
				m[tr]++;

			}

		

		}


	cout << ans << " " << m[ans] << endl;
	//return to_string(ans) + " " + to_string(m[ans]);
	return "\n";
}

int main() {
	freopen("D-small-attempt1.in", "rt", stdin); freopen("D-small1.out", "wt", stdout);
	//freopen("D-large.in", "rt", stdin); freopen("D-large.out", "wt", stdout);
	//freopen("test.in","rt",stdin);

	int T,N,M;
	string t;
	cin>>T;
	for (int i=0; i<T; i++) {
		cin>>M>>N;
		vector <string> v;
		for (int j=0; j<M; j++) {
			cin>>t;
			v.push_back(t);
		}
//		if (i>=25)
//		if (i>=50)
//		if (i>=75)
		cout << "Case #" << i+1 << ": ";
		solve(v,N);// << endl;
	}
}
