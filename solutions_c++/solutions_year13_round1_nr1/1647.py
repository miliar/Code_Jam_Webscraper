#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef unsigned long long ul;
typedef long double ld;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

int main(){
	
	freopen("xyz.txt","r",stdin);
	freopen("abc.txt","w",stdout);
	int Kase=GI;
	ld d;
	ul y,x,r,t;
	FOR(kase,1,Kase+1){
		cin>>r>>t;
		printf("Case #%d: ",kase);
        x=2*r-1;x=x*x;x=x+8*t;
        d=sqrt((ld)x);d=d-2*r+1;d=d/4;
        y=(ul)d;
        cout<<y<<endl;		
	}
	return 0;
}
