#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <functional>
#include <climits>
#include <list>
#include <ctime>
#include <complex>

#define F1(x,y,z) for(int x=y;x<z;x++)
#define F2(x,y,z) for(int x=y;x<=z;x++)
#define F3(x,y,z) for(int x=y;x>z;x--)
#define F4(x,y,z) for(int x=y;x>=z;x--)
#define mp make_pair
#define pb push_back
#define LL long long
#define co complex<double>

#define MAX 100005
#define AMAX 1500
#define MOD 1000000007

#define f(c,d) ((1<<(c))*(d))

using namespace std;

int t,n,nn,r,p,s,ta,tb,tc,x[3],z[MAX];
char ans[MAX];
bool ok;

bool comp(int a,int b){
	F1(c,0,b)if(ans[a+c]!=ans[a+b+c])return ans[a+c]>ans[a+b+c];
	return 0;
}

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		scanf("%d%d%d%d",&n,&r,&p,&s);
		nn=1<<n;
		ok=0;
		if(!ok){
			ta=1<<n;
			z[0]=0;
			F1(b,0,n){
				ta>>=1;
				F1(c,0,(1<<b))z[ta*(c*2+1)]=(z[ta*c*2]+2)%3;
			}
			memset(x,0,sizeof(x));
			F1(b,0,nn)x[z[b]]++;
			if(x[0]==r&&x[1]==p&&x[2]==s)ok=1;
		}
		if(!ok){
			ta=1<<n;
			z[0]=1;
			F1(b,0,n){
				ta>>=1;
				F1(c,0,(1<<b))z[ta*(c*2+1)]=(z[ta*c*2]+2)%3;
			}
			memset(x,0,sizeof(x));
			F1(b,0,nn)x[z[b]]++;
			if(x[0]==r&&x[1]==p&&x[2]==s)ok=1;
		}
		if(!ok){
			ta=1<<n;
			z[0]=2;
			F1(b,0,n){
				ta>>=1;
				F1(c,0,(1<<b))z[ta*(c*2+1)]=(z[ta*c*2]+2)%3;
			}
			memset(x,0,sizeof(x));
			F1(b,0,nn)x[z[b]]++;
			if(x[0]==r&&x[1]==p&&x[2]==s)ok=1;
		}
		printf("Case #%d: ",a);
		if(ok){
			F1(b,0,nn)ans[b]=(z[b]==0?'R':(z[b]==1?'P':'S'));
			tb=1;
			F4(b,n-1,0){
				//F1(c,0,nn)printf("%c",ans[c]);
				//printf(" ");
				ta=0;
				F1(c,0,(1<<b)){
					if(comp(ta,tb))F1(d,0,tb)swap(ans[ta+d],ans[ta+tb+d]);
					ta+=tb*2;
				}
				tb*=2;
			}
			F1(b,0,nn)printf("%c",ans[b]);
		}else printf("IMPOSSIBLE");
		printf("\n");
	}
	//system("pause");
	return 0;
}
