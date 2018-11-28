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
int t,n,m,ans,ap;
char s[29][29];
int main(){
	if(!testing){
		freopen("D-small-attempt0.in","r",stdin);
		freopen("D.out","w",stdout);
	}
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d %d\n",&n,&m);
		for(int j=1;j<=n;j++) gets(s[j]);
		printf("Case #%d: ",i);
		int exp=1,gp[29];
		bool sel[29];
		ans=ap=0;
		for(int j=1;j<=n;j++) exp*=m;
		for(int j=0;j<exp;j++){
			for(int k=0;k<m;k++) sel[k]=false;
			int x=j;
			for(int k=1;k<=n;k++){
				gp[k]=x%m;
				x/=m;
				sel[gp[k]]=true;
			}
			bool end=false;
			for(int k=0;k<m;k++) if(!sel[k]) end=1;
			if(end) continue;
			int tmp=0;
			for(int k=1;k<=n;k++){
				tmp+=strlen(s[k]);
				int cool=0;
				for(int l=1;l<k;l++){
					if(gp[l]!=gp[k]) continue;
					int pos=0,L1=strlen(s[k]),L2=strlen(s[l]);
					while(pos<L1 && pos<L2){
						if(s[k][pos]!=s[l][pos]) break;
						pos++;
					}
					cool=max(cool,pos);
				}
				tmp-=cool;
			}
			//printf("(%d,%d)\n",j,tmp);
			if(tmp>ans){
				ans=tmp;
				ap=1;
			}else if(tmp==ans) ap++;
		}
		printf("%d %d\n",ans+m,ap);
	}
	return 0;
}
