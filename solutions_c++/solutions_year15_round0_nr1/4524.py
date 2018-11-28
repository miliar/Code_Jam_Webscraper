#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define fortodo(i,a,b) for (int i=(a);i<=(b);i++)
using namespace std;
const int maxn=2001;
char s[maxn];
int a[maxn],tot,T,n;

inline void judge(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
}

int main(){
	judge();
	scanf("%d",&T);
	fortodo(p,1,T){
		scanf("%d",&n);
		scanf("%s",s);
		fortodo(i,0,n) a[i]=s[i]-'0';
		tot=a[0];
		int ans=0;
		fortodo(i,1,n){
			if (tot<i){
				ans+=i-tot;
				tot=i;
			}
			tot+=a[i];
		}
		printf("Case #%d: %d\n",p,ans);
	}
	return 0;
}

