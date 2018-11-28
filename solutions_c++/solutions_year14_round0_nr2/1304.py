#pragma comment(linker,"/STACK:102400000,102400000")
#include <algorithm>
#include <iostream>
#include <fstream>
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

double C,F,X,Ans;

struct Node
{
	double nowVal,sp,timeVal;
	Node(){}
	Node(double a,double b,double c):nowVal(a),sp(b),timeVal(c){}
};

queue<Node>que;

inline void bfs()
{
	while(!que.empty()) que.pop();
	que.push(Node(0,2,0));
	Node now,next;
	double tmp;
	while(!que.empty())
	{
		now=que.front();que.pop();
		if(now.timeVal>=Ans) continue;
		tmp=now.timeVal+(X-now.nowVal)/now.sp;
		Ans=min(Ans,tmp);
		if(C>now.nowVal)
		{
			tmp=(C-now.nowVal)/now.sp;
			que.push(Node(C,now.sp,now.timeVal+tmp));
			que.push(Node(0,now.sp+F,now.timeVal+tmp));
		}
	}
}

inline void Run()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,tt=0;
	scaf(t);
	while(t--)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		Ans=INT_MAX*1.0;
		bfs();
		pf("Case #%d: %.7lf\n",++tt,Ans);
	}
}


int main()
{
	Run();
	return 0;
}
