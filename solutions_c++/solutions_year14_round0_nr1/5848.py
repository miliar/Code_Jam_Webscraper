#define DEBUG
#ifndef DEBUG
#include <bits/stdc++.h>
using namespace std;
#else
#include "header.h"
#endif
#define SS(n) scanf("%s",n)
#define pn putchar('\n')
#define ps putchar(' ')
#define sz(s) int((s).size())
#define rep(i,a,b) for(int(i)=a;(i)<=(b);++(i))
#define per(i,b,a) for(int(i)=b;(i)>=(a);--(i))
#define clr(a) memset(a,0,sizeof(a))
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#ifdef DEBUG
#include "debug.h"
#else
#define ck1
#define ck2
#define ck3
#define dir
#define show(x)
#define show2(x,y)
#define show3(x,y,z)
#define show4(x,y,z,w)
#endif
typedef long long LL; typedef vector <int> vi; typedef pair<int,int> pii; typedef map <int,int> mii; template <class T> inline T max(T a,T b,T c) {return (max(max(a,b),c));} template <class T> inline T min(T a,T b,T c) {return (min(min(a,b),c));} template <class T> inline T sqr(T x) {return x*x;} inline int inp() {int n=0,s=1;char p=getchar();if(p=='-')s=-1;while((p<'0'||p>'9')&&p!=EOF&&p!='-')p=getchar();if(p=='-')s=-1,p=getchar();while(p>='0'&&p<='9')n=(n<<3)+(n<<1)+(p-'0'),p=getchar();return n*s;} void out(int x){if(x<0)putchar('-'),x=-x;int ll=0,dd[10];while(x)dd[ll++]=x%10,x/=10;if(!ll)dd[ll++]=0;while(ll--)putchar(dd[ll]+48);} inline int ins(int x,int y,int m,int n){return (x>=1&&x<=m&&y>=1&&y<=n);} template <class T> inline T gcd(T a,T b){return (!b? a : gcd(b,a%b));} template <class T> inline T ABS(T x){return ((x)>0?(x):(-(x)));}
const int N = 1e5 + 11;
const int inf = INT_MAX;

int main()
{
	#ifdef DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int testCase, t=inp();
	for(testCase=1; testCase<=t; ++testCase)
	{
		int a=inp();
		bool hush[24] = {false};
		for(int i=1; i<=4; ++i) {
			for(int j=1; j<=4; ++j) {
				int x = inp();
				if(i == a) hush[x] = 1;
			}
		}
		int b = inp();
		int cnt=0;
		int save=0;
		for(int i=1; i<=4; ++i) {
			for(int j=1; j<=4; ++j) {
				int x = inp();
				if(i == b && hush[x] == 1) {
					++cnt;
					save = x;
				}
			}
		}
		printf("Case #%d: ",testCase);
		if(cnt == 1) cout << save << endl;
		else if(cnt == 0) cout << "Volunteer cheated!\n";
		else cout << "Bad magician!\n";
	}
}
