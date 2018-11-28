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

int T;

int main(){
	freopen("i.txt","r",stdin);freopen("o.txt","w",stdout);
	scanf("%d",&T);
	For(t,1,T){
		double C,F,X,Rate=2,Time=0,MoneySpent=0,Ans=100000;
		cin>>C>>F>>X;
		while(MoneySpent<X){
			Ans=Min(Ans,Time+X/Rate);
			Time+=(C/Rate);
			MoneySpent+=C;
			Rate+=F;
		}
		printf("Case #%d: ",t);
		printf("%.7f\n",Ans);
	}
}
