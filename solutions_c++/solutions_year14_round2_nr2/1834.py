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

int main(){
    FILE *f = freopen("A.txt","r",stdin);
	FILE *g = freopen("out.txt","w",stdout);
	int ntsts;
	cin >> ntsts;
	const int infty = 10000000;
	for(int ntst = 1; ntst <= ntsts; ++ntst){ 
		char buf[200];
		int A,B,K; cin>>A>>B>>K;
		int win = 0;
		for(int a = 0; a<A; ++a){
			for(int b = 0; b<B; ++b){
				if( (a&b) < K ){
					win++;
				}
			}
		}
		

		fail:

		printf("Case #%d: %d\n",ntst,win);
	}

	//printf("%I64d\n", nr);
	return 0;
}
