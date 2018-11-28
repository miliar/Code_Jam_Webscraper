#include <iostream>
#include <ostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <stack>
#include <queue>
#include <set>

using namespace std;
template<class T>
ostream & operator<<(ostream& o, const vector<T>& v){ 
	for (auto i = v.begin(); i!=v.end(); ++i)
	{ o<<*i; if (i!=v.end()-1) o << " "; }
	return o;
}

typedef long long ll;

vector<pair<char,int>> f(string s){
	int i =0;
	vector<pair<char,int>> r;
	while (i < s.length()){
		int j= 1;
		while (s[i]==s[i+1]){
			j++;
			i++;
		}
		r.push_back(make_pair(s[i], j));
//		cout << s[i] << " " << j << endl;
		i++;
	}
	return r;
}

int main(){
	int t; cin >> t;
	for (int ti = 0; ti < t; ti++){
		bool impos = false;
		vector<vector <pair<char,int>>> v;
		int n; cin >> n;
		for (int i =0; i<n;i++){
			string tmps; cin >> tmps;
			v.push_back(f(tmps));
		}
		int r = 0;
		for (int i=0; i<n; i++) {
			if (v[i].size()!= v[0].size()){
				impos = true;
				continue;
			}
			for (int j=0; j<v[i].size(); j++){
				if (v[i][j].first != v[0][j].first){
					impos = true;
				}
			}
		}
		if (!impos){
			for (int i=0; i<v[0].size(); i++){
				double sum = 0;
				for (int j=0; j<n; j++)
					sum +=v[j][i].second;
				sum /= n;
				int over = 0;
				for (int j=0; j<n; j++)
					if (v[j][i].second > sum) over++;
				if (over > n/2)
					sum=ceil(sum);
				else
					sum=floor(sum);
				for (int j=0; j<n; j++)
					r+=abs(v[j][i].second -sum);
			}
		}
		cout << "Case #" << ti + 1 << ": ";
		if (impos) cout << "Fegla Won" << endl;
		else cout << r << endl;
	}
}
