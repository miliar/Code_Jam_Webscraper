#include <iostream>
#include <algorithm>
#include <climits>
#include <memory.h>
#include <cstdio>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <set>
#include <map>
using namespace std;
#define SS(n) scanf("%s",n)
#define pn puts("");
#define ps putchar(' ')
#define s(n) int n; scanf("%d",&(n))
#define s2(n,m) int (n),(m); scanf("%d %d",&(n),&(m))
#define sz(s) int((s).size())
#define rep(i,a,b) for(int(i)=a;(i)<=(b);++(i))
#define per(i,b,a) for(int(i)=b;(i)>=(a);--(i))
#define clr(a) memset(a,0,sizeof(a))
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
typedef long long LL;
typedef vector <int> vi;
typedef pair<int,int> pii;
typedef map <int,int> mii;
template <class T> inline T max(T a,T b,T c) {return (max(max(a,b),c));}
template <class T> inline T min(T a,T b,T c) {return (min(min(a,b),c));}
inline int inp() {int n=0,s=1;char p=getchar();if(p=='-')s=-1;while((p<'0'||p>'9')&&p!=EOF&&p!='-')p=getchar();if(p=='-')s=-1,p=getchar();while(p>='0'&&p<='9')n=(n<<3)+(n<<1)+(p-'0'),p=getchar();return n*s;} 
void out(int x){if(x<0)putchar('-'),x=-x;int ll=0,dd[10];while(x)dd[ll++]=x%10,x/=10;if(!ll)dd[ll++]=0;while(ll--)putchar(dd[ll]+48);} inline int ins(int x,int y,int m,int n){return (x>=1&&x<=m&&y>=1&&y<=n);} 
template <class T> inline T sqr(T x) {return x*x;}
template <class T> inline T ABS(T x){return ((x)>0?(x):(-(x)));}
const int N = 1e2 + 11;
const int inf = INT_MAX;
//#include "debug.h"

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int testCase, t=inp();
	for(testCase=1; testCase<=t; ++testCase)
	{
		printf("Case #%d: ",testCase);
		int n = inp();
		string s1,s2;
		cin >> s1 >> s2;
		vector <char> v1,v2;
		vector <int> a1,a2;
		v1.pb(s1[0]);
		int cnt=1;
		for(int i=1; s1[i]; ++i) {
			if(s1[i] == s1[i-1]) cnt++;
			else {
				a1.pb(cnt);
				v1.pb(s1[i]);
				cnt=1;
			}
		}
		if(cnt > 0) a1.pb(cnt);
		cnt=1;
		v2.pb(s2[0]);
		for(int i=1; s2[i]; ++i) {
			if(s2[i] == s2[i-1]) cnt++;
			else {
				a2.pb(cnt);
				v2.pb(s2[i]);
				cnt=1;
			}
		}
		if(cnt > 0) a2.pb(cnt);
		cnt=0;
		
		/*
		for(char ch:v1) show(ch);
		for(int i:a1) show(i);
		pn;
		for(char ch:v2) show(ch);
		for(int j:a2) show(j);
		*/
		
		if(sz(v1) != sz(v2)) {
			puts("Fegla Won");
			continue;
		}
		bool ok = 1;
		
		for(int i=0; i<sz(v1); ++i) {
			if(v1[i] != v2[i]) {
				ok=0;
				break;
			}
		}
		
		int ans=0;
		for(int i=0; i<sz(a1); ++i) {
			ans += ABS(a1[i] - a2[i]);
		}
		if(ok) cout<<ans<<endl;
		else puts("Fegla Won");
	}
}		

// removed debug && lzip ?? 
