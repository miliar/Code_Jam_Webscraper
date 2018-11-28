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

int T,key;
int a[10],vis[20];

int main(){
	freopen("1.in","r",stdin);
	freopen("haha.txt","w",stdout);
	cin >>T;
	rep(TT,1,T){
		memset(vis,0,sizeof vis);
		scanf("%d",&key);
		rep(i,1,4){
			rep(j,1,4)	scanf("%d",&a[j]);
			if	(i==key)
				rep(j,1,4)	vis[a[j]]=1;
		}
		int cnt=0,sav;
		scanf("%d",&key);
		rep(i,1,4){
			rep(j,1,4)	scanf("%d",&a[j]);
			if	(i==key)
				rep(j,1,4)	if	(vis[a[j]])	cnt++,sav=a[j];
		}
		printf("Case #%d: ",TT);
		if	(cnt>1)	puts("Bad magician!");
		if	(cnt==0)	puts("Volunteer cheated!");
		if	(cnt==1)	printf("%d\n",sav);
	}
}


