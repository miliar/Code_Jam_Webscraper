#pragma comment(linker,"/STACK:102400000,102400000")
#include <algorithm>
#include <iostream>
//#include <fstream>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define sf scanf
#define pf printf
#define fst first
#define scd second
#define pb push_back
#define mkp make_pair
#define cls(a,x) memset(a,x,sizeof a)
#define dt(x) cout<<#x<<"="<<x<<" ";
#define dte(x) cout<<#x<<"="<<x<<endl;

#if(_WIN32||__WIN32_)
typedef __int64 LL;
typedef unsigned __int64 ULL;
#else
typedef long long LL;
typedef unsigned long long ULL;
#endif

using namespace std;
template<class T>inline void scaf(T &v)
{
    char ch;
    while(ch=getchar())
        if(ch<='9' && ch>='0') break;
    v=ch-'0';
    while(ch=getchar())
        if(ch<='9' && ch>='0') v=(v<<1)+(v<<3)+ch-'0';
        else break;
}
typedef pair<int,int > PII;
const int MX=100010;
const LL mod=1000000007;
const double pi=3.14159265358979323846;

int a[5];
int b[5];

inline void Run()
{
//	freopen("A-small-attempt5.in","r",stdin);
//	freopen("A-small-attempt5.out","w",stdout);
	int t,tt=0;
	int i,j,x,n;
	scanf("%d",&t);
	while(t--)
	{
		int top=0;
		scanf("%d",&n);
		for(i=1;i<=4;++i)
		{
			for(j=1;j<5;++j)
			{
				scanf("%d",&x);
				if(n==i)
					a[top++]=x;
			}
		}
		top=0;
		scanf("%d",&n);
		for(i=1;i<=4;++i)
		{
			for(j=1;j<5;++j)
			{
				scanf("%d",&x);
				if(n==i)
					b[top++]=x;
			}
		}
		top=0;
		int Ans[5];
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				if(a[i]==b[j])
				{
					Ans[top++]=a[i];
				}
			}
		}
		pf("Case #%d: ",++tt);
		if(top>1) puts("Bad magician!");
		else if(1==top) pf("%d\n",Ans[0]);
		else puts("Volunteer cheated!");
	}
}


int main()
{
	Run();
	return 0;
}
