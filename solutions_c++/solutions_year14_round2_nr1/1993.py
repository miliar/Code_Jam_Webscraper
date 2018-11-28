// CF.cpp: define el punto de entrada de la aplicaci?n de consola.
//
#pragma warning ( disable: 4996 )
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <map>
#include <iostream>

typedef std::pair<int,int> ii;
typedef long long int Int;
typedef unsigned long long int uInt;
typedef std::vector<int> vi;
typedef std::vector<double> vd;
typedef std::vector<vi> vvi;
typedef std::vector<std::string> vs;
typedef std::vector<ii> vii;
#define sz(X) int((X).size())
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,v) for(int i = 0; i < int(v.size()); ++i)
#define ALL(v) v.begin(),v.end()
using namespace std;

int dp[100][100];

string clean(string t){
	string s;
	for(int i = 0; i<sz(t); ++i){
		if(s.length()==0||t[i]!=s.back())
			s.push_back(t[i]);
	}
	return s;
}
int main(){
    FILE *f = freopen("A.txt","r",stdin);
	FILE *g = freopen("out.txt","w",stdout);
	int ntsts;
	scanf("%d\n",&ntsts);
	const int infty = 10000000;
	for(int ntst = 1; ntst <= ntsts; ++ntst){ 
		char buf[200];
		int N;
		int bst = infty;
		scanf("%d\n",&N);
		vector<int> P(N);
		vector<string> S(N);
		string s="",t;
		for(auto &a:S){ 
			scanf("%s\n",&buf); 
			a = buf; 
			t = clean(a);
			if(s.length()==0) s = t;
			else if(s!=t) goto fail;
		}
		bst = 0;
		for(int i = 0; i<s.length(); ++i){
			vector<int> nc(N);
			int nch = 0;
			for(int n = 0; n<N; ++n){
				while(P[n] < S[n].length() && S[n][P[n]]==s[i])
					P[n]++,nc[n]++;
				nch += nc[n];
			}
			int nch2 = (nch+N/2)/N;
			int nst = 0;
			for(int n = 0; n<N; ++n){
				nst += abs(nc[n]-nch2);
			}
			bst += nst;
		}
		

		fail:

		printf("Case #%d: ",ntst);
		if( bst == infty){
			printf("Fegla Won\n");
		} else {
			printf("%d\n",bst);
		}
	}

	//printf("%I64d\n", nr);
	return 0;
}
