#include <iostream>
#include <ios>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <vector>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;
#define XINF INT_MAX
#define INF 0x3f3f3f3f
#define MAXN 0x7fffffff
#define eps 1e-10
#define zero(a) fabs(a)<eps
#define sqr(a) ((a)*(a))
#define MP(X,Y) make_pair(X,Y)
#define PB(X) push_back(X)
#define PF(X) push_front(X)
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define DEP(X,R,L) for(int X=R;X>=L;X--)
#define CLR(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define PI  acos(-1.0)
#define test puts("OK");
#define lowbit(X) (X&(-X))
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
typedef long long ll;
typedef pair<int,int> PII;
typedef priority_queue<int,vector<int>,greater<int> > PQI;
typedef vector<PII> VII;
typedef vector<int> VI;
#define X first
#define Y second

string str;
int a[10000+10];

int num[5][5]={0,0,0,0,0,
			   0,1,2,3,4,
			   0,2,-1,4,-3,
			   0,3,-4,-1,2,
			   0,4,3,-2,-1};
			   
int divi[5][5]={0,0,0,0,0,
				0,1,-2,-3,-4,
				0,2,1,4,-3,
				0,3,-4,1,2,
				0,4,3,-2,1};
			   
inline int solve(char c)
{
	if(c=='i') return 2;
	if(c=='j') return 3;
	if(c=='k') return 4;
}

inline int mul(int x,int y)
{
	bool flag=(x>0)^(y>0);
	return num[abs(x)][abs(y)]*(flag?-1:1);
}

inline int divid(int z,int x)
{
	bool flag=(z>0)^(x>0);
	return divi[abs(z)][abs(x)]*(flag?-1:1);
}

int main()
{_
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	REP(k,T)
	{
		str="";
		string temp;
		int l,x,len;
		cin>>l>>x>>temp;
		len=l*x;
		REP(i,x)
			str+=temp;
		int sum=1,pos1=-1;
		bool used=0;
		REP(i,len)
		{
			int res=mul(sum,solve(str[i]));
			a[i]=sum=res;
			if(!used && res==2 && i<=len-3)
			{
				used=1;
				pos1=i;
			}
		}
		if(pos1==-1)
		{
			printf("Case #%d: NO\n",k+1);
			continue;	
		}
		int end=sum,pos2=-1;
		for(int j=len-2;j>=pos1+1;j--)
		{
			int res=divid(end,a[j]);
			if(res==4)
			{
				pos2=j;
				break;
			}
		}
		if(pos2==-1)
		{
			printf("Case #%d: NO\n",k+1);
			continue;	
		}
		if(divid(a[pos2],a[pos1])!=3)
		{
			printf("Case #%d: NO\n",k+1);
			continue;	
		}
		printf("Case #%d: YES\n",k+1);
	}
	return 0;
}

