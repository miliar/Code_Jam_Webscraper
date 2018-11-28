// GCJ 2014 1B b 
// Template

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define REP(i,a,b) for(int i=a; i <b; i++)

// printf("");
// scanf("",&);


int T,cases;
int A,B,K;


int main(){

//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("B-small-attempt0.out","w",stdout);

	cin >> T;
	cin.ignore();

	while(cases++<T){
		cin >> A >> B >> K;
		int ans = 0;
		REP(a,0,A){
			REP(b,0,B){
				if( (a & b) < K){
					ans++;
				}

			}
		}
		printf("Case #%d: %d\n",cases,ans);

	}

return 0;
}