#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <malloc.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <stdint.h>
#include <unistd.h>
#include <ctime>
#include <climits>
using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define T           top()
#define P           pop()
#define NL 			printf("\n")

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vstr;
typedef long long LL;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("salida.out","w",stdout);
	int t;
	double c,f,x,sol,so,se,ga;
	cin>>t;
	F(i,t)
	{
		se=0.0;
		ga=2;
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		//printf("%lf %lf %lf\n",c,f,x);
		sol=x/ga;
		for(;;)
		{
			se+=c/ga;
			ga+=f;
			so=(x/ga)+se;
			if(sol < so)break;
			else
			{
				sol=so;
			}
		}
		printf("Case #%d: %.7lf\n", i+1,sol);
	}
}
