#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<list>
#include<queue>
#include<map>
#include<cmath>
#include<string>
#include<cstdlib>
#include<ctime>
#include<vector>
#include<deque>
#include<stack>
using namespace std;
#define LL long long
#define ULL unsigned long long
#define UI unsigned int
#define PII pair<int,int>
#define PLL pair<LL,LL>
#define mp make_pair
#define PB push_back
#define PF push_front
#define _PB pop_back
#define _PF pop_front
#define F first
#define S second
#define PI 3.1415926535897
#define _e 2.718281828
#define FIN(i,a,b) for(int i=a;i<=b;i++)
#define FEX(i,a,b) for(int i=a;i<b ;i++)
#define DIN(i,a,b) for(int i=a;i>=b;i--)
#define DEX(i,a,b) for(int i=a;i>b ;i--)
#define DEBUG printf
bool testing = false;
int tc,n,cap,s[10005];
int main(){
	if(!testing){
		freopen("A-large.in","r",stdin);
		freopen("A.out","w",stdout);
	}
	scanf("%d",&tc);
	for(int i=1;i<=tc;i++){
		scanf("%d %d",&n,&cap);
		printf("Case #%d: ",i);
		for(int i=1;i<=n;i++) scanf("%d",&s[i]);
		sort(s+1,s+1+n);
		int lt=1,ans=0;
		for(int i=n;i>=lt;i--){
			ans++;
			if(s[lt]+s[i]<=cap) lt++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
