#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue> 
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define inf 2000000000
#define Min(a,b) (a<b?a:b)
#define Max(a,b) (a>b?a:b)
#define For(i,s,n) for (int i=s;i<=n;i++)
#define FOR(i,s,n) for (int i=s;i<n;i++)
#define Ford(i,s,n) for (int i=s;i>=n;i--)
#pragma comment(linker, "/STACK:16777216")


#define MD 1000000007
#define PI 3.1415926535897932384626433832795

typedef long long ll;

using namespace std;

int x[10],y[10];


int main(){
	freopen("i.txt","r",stdin);freopen("o.txt","w",stdout);
	int T;
	scanf("%d",&T);
	For(t,1,T){
		int Row;
		scanf("%d",&Row);
		For(i,1,4)
			For(j,1,4){
				int tmp;
				if (i==Row) scanf("%d",x+j);else scanf("%d",&tmp);
		}
		scanf("%d",&Row);
		For(i,1,4)
			For(j,1,4){
				int tmp;
				if (i==Row) scanf("%d",y+j);else scanf("%d",&tmp);
		}
		int c=0,Ans=0;
		For(i,1,4)
			For(j,1,4)
				if (x[i]==y[j]){
					c++;Ans=x[i];
				}
		printf("Case #%d: ",t);
		if (!c) puts("Volunteer cheated!");
		if (c>1) puts("Bad magician!");
		if (c==1) printf("%d\n",Ans);
	}
}