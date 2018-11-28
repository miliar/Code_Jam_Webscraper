#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>
#include <ctime>
#include <cstdio>
#include <stack>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <functional>
#include <sstream>
#include <map>
#include <set>

#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef long long ll;
typedef pair<int,int> pii;
int n, m, x;
string st;
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas=1;
	cin>>tc;
	while (tc--)
	{
		cin>>x>>n>>m;
		if((1+x-min(n+1, m+1))>=min(n+1, m+1) || x>=7 || (n*m)%x || (1+x-min(n+1, m+1))>=max(n, m))
		{
			PF("Case #%d: RICHARD\n", cas++);
			continue;
		}

		if(x==1)
		{
			PF("Case #%d: GABRIEL\n", cas++);
			continue;
		}
		if(x==2)
		{
			if((n*m)%2) PF("Case #%d: RICHARD\n", cas++);
			else PF("Case #%d: GABRIEL\n", cas++);
			continue;
		}
		if(x==3)
		{
			if(n%3==0 || m%3==0) PF("Case #%d: GABRIEL\n", cas++);
			else PF("Case #%d: RICHARD\n", cas++);
			continue;
		}
		if(min(n, m)>=x) 
		{
			PF("Case #%d: GABRIEL\n", cas++);
			continue;
		}
		if(n<m) swap(n, m);
		if(x==4)
		{
			if(n==4 && m==2) PF("Case #%d: RICHARD\n", cas++);
			else PF("Case #%d: GABRIEL\n", cas++);
			continue;
		}
		if(x==5)
		{
			PF("Case #%d: GABRIEL\n", cas++);
			continue;
		}
		if(m==3) PF("Case #%d: RICHARD\n", cas++);
		else PF("Case #%d: GABRIEL\n", cas++);
	}
	return 0;
}