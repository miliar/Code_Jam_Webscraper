#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define PB push_back
#define MP make_pair
#define clr(a,b)	(memset(a,b,sizeof(a)))
#define rep(i,a)	for(int i=0; i<(int)a.size(); i++)

const int INF = 0x3f3f3f3f;
const double eps = 1E-8;

double c,x,f;
int T;

int main()
{


	freopen("D:\\B-large.in","r",stdin);


	freopen("D:\\out.txt","w",stdout);

	int cas = 1;
	scanf("%d",&T);
	while(T--)
	{
		double ans = 1e30;
		double per = 2.0;
		double pretime = 0;

		scanf("%lf%lf%lf",&c,&f,&x);
		while(1)
		{
			double cur = x / per + pretime;
			if(cur > ans)	break;
			ans = min(ans, cur);
			pretime += c / per;
			per += f;
		}
		printf("Case #%d: %.7f\n",cas++,ans);
	}

	return 0;
}
