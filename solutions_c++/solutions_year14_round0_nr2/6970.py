#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define ps system("pause")
#define message printf("*\n")
#define pb push_back
#define X first
#define Y second
#define PII pair<int,int>
#define rep(a,b,c) for(int a=b;a<=c;a++)
#define per(a,b,c) for(int a=b;a>=c;a--)

typedef long long ll;

using namespace std;

int T;
double C,F,X,Last,Cur;

int main(){
	freopen("1.in","r",stdin);
	freopen("haha.txt","w",stdout);
	scanf("%d",&T);
	rep(TT,1,T){
		cin >>C >>F >>X;
		Last=X/2.0;
		rep(i,1,X+1){
			Cur=0;
			rep(j,1,i)	Cur=Cur+C/(F*(j-1)+2);
			Cur=Cur+X/(F*i+2);
			if	(Cur>Last)	break;
			else	Last=Cur;
		}
		printf("Case #%d: %.7lf\n",TT,Last);
	}
}


