#include <iomanip>
#include <map>
#include <queue>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <map>
//#pragma comment(linker,"/STACK:1024000000,1024000000")
inline const int getint() { int r=0, k=1; char c=getchar(); for(; c<'0'||c>'9'; c=getchar()) if(c=='-') k=-1; for(; c>='0'&&c<='9'; c=getchar()) r=r*10+c-'0'; return k*r; }

using namespace std;
#define eps 1e-9
#define LL long long
#define ull unsigned long long
#define Rep(i,l,r) for(i=(l);i<(r);i++)
#define rep(i,l,r) for(i=(l);i<=(r);i++)
#define red(i,l,r) for(i=(l);i>=(r);i--)
#define pb push_back
#define mp make_pair
const int maxn=1e5+10;
int d[5][5]={1,1,1,1,1,
	         1,1,2,3,4,
			 1,2,-1,4,-3,
			 1,3,-4,-1,2,
			 1,4,3,-2,-1
};
int ss1[maxn],ss2[maxn];
int get(char c){
	switch(c){
	case'i': return 2;
	case'j': return 3;
	case'k': return 4;
	}
}
char  s1[maxn];
int s[maxn];
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,len;
	scanf("%d",&T);
	int ka=1;
	int l,x;
	while(T--){
		scanf("%d%d",&l,&x);
		scanf("%s",s1);
		int i,j;
		rep(i,0,l-1) s[i]=get(s1[i]);
		rep(i,2,x){
			rep(j,0,l-1){
				s[(i-1)*l+j]=s[j];
			}
		}
		int len=l*x;
		ss1[0]=s[0];
		ss2[len-1]=s[len-1];
		rep(i,1,len-1){
			int temp=abs(ss1[i-1]);
			ss1[i]=d[temp][s[i]];
			if(ss1[i-1]<0) ss1[i]=-ss1[i];
		}
		red(i,len-2,0){
			int temp=abs(ss2[i+1]);
			ss2[i]=d[s[i]][temp];
			if(ss2[i+1]<0) ss2[i]=-ss2[i];
		}
		printf("Case #%d: ",ka++);
		if(ss1[len-1]!=-1){
			cout<<"NO"<<endl;
			continue;
		}
		int flag1=len-1,flag2=0;
		rep(i,0,len-1){
			if(ss1[i]==2){
				flag1=i;
				break;
			}
		}
		red(i,len-1,0){
			if(ss2[i]==4){
				flag2=i;
				break;
			}
		}
		if(flag1<flag2){
			cout<<"YES"<<endl;
		}
		else cout<<"NO"<<endl;
	}
	return 0;
}