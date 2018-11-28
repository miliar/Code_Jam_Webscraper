#include<vector>
#include<cmath>
#include<complex>
#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<float.h>
#include<set>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
using namespace std;


typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define pb push_back
#define mp make_pair
#define snd second
#define fst first
#define debug printf("--%d--\n",__LINE__)
#define ll long long int

int casenum;
int n, m;
vvi ps;
int main(void){
	cin >> casenum >> n >> m;
	
	vi p((n-1)/2);
	p[p.size()-2] = p[p.size()-1] = 1;
	do{
		ps.pb(p);
	}while(next_permutation(p.begin(), p.end()));
	int cnt = 0;
	cout << "Case #1:" << endl;
	for(int i=0;i<ps.size();i++){
		for(int j=0;j<ps.size();j++){
			string s = "";
			for(int k=0;k<n;k++) s += '0';
			s[0] = s[n-1] = '1';
			for(int k=0;k<ps[i].size();k++){
				if (ps[i][k]==1) s[1+2*k] = '1';
				if (ps[j][k]==1) s[2+2*k] = '1';
			}
			cout << s << " 3 2 3 2 7 3 3 2 3" << endl;
			cnt++;
			if (cnt >= m) return 0;
		}
	}
	
	
	return 0;
}
