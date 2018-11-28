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
int t,n,bl[1002],br[1002],s[1002],sl[1002];
int main(){
	if(!testing){
		freopen("B-large.in","r",stdin);
		freopen("B.out","w",stdout);
	}
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&n);
		printf("Case #%d: ",i);
		for(int j=1;j<=n;j++) scanf("%d",&s[j]);
		int ans=0;
		for(int j=1;j<=n;j++){
			bl[j]=0;
			for(int k=1;k<j;k++) if(s[k]>s[j]) bl[j]++;
			br[j]=0;
			for(int k=j+1;k<=n;k++) if(s[k]>s[j]) br[j]++;
			ans+=min(bl[j],br[j]);
		}
		
		printf("%d\n",ans);
	}
	return 0;
}
