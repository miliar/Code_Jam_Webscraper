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
const int maxn=1e3+10;
char s[maxn];
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T,len;
	scanf("%d",&T);
	int ka=1;
	while(T--){
		scanf("%d%s",&len,s);
		int sum=0;
		int i;
		sum+=s[0]-'0';
		int ans=0;
		rep(i,1,len){
			int c=s[i]-'0';
			if(c){
				if(sum<i){
					ans+=i-sum;
					sum+=(i-sum);
				}
			}
			sum+=c;
		}
		printf("Case #%d: %d\n",ka++,ans);
	}
	return 0;
}