#include<iostream>
#include<sstream>
#include<string>
#include<cstdio>
#include<vector>
#include<map>
using namespace std;

int n;
string s;
map<string, int> M;
vector<int> a[1000];
int l[10000];
int L[10000];

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	int tt;
	cin >> tt;
	for (int _tt=0 ; _tt < tt ; _tt++){
		cerr << _tt << endl;
		int J = 1000 * 1000 * 1000;
		memset(L, 0, sizeof L);
		int T = 0;
		M.clear();
		cin >> n;
		for (int i=0 ; i<n ; i++) a[i].clear();
		for (int i=0 ; i<n ; i++){
			string s;
			while(!s.size())
				getline(cin, s);
			stringstream ss(s);
			while(ss >> s){
				if (!M[s]) M[s] = ++T;
				a[i].push_back(M[s]);
			}
		}
		for (int k=0 ; k<a[0].size() ; k++)
			L[a[0][k]] |= 1;
		for (int k=0 ; k<a[1].size() ; k++)
			L[a[1][k]] |= 2;
		for (int i=0 ; i<(1<<n) ; i++){
			if (i&1) continue;
			if (!(i&2)) continue;
			memset(l, 0, sizeof l);
			for (int j=2 ; j<n ; j++){
				int O = 1;
				if (i&(1<<j)) O = 2;
				for (int k=0 ; k<a[j].size() ; k++)
					l[a[j][k]] |= O;
			}		
			int jj = 0;
			for (int i=0 ; i<=T ; i++)
				jj += ((l[i]|L[i]) == 3);
			J = min(J, jj);
		}
		cout << "Case #" << _tt+1 << ": " << J << endl;
	}
}
