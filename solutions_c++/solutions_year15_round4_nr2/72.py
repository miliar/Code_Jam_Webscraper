/*.....................
Author : PTY
Time : 15/05/01
Desprition :
Analyse : 
Attention : 
.....................*/
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <map>
using namespace std;
#define rep(i,l,r) for(int i=l;i<=r;i++)
#define drep(i,r,l) for(int i=r;i>=l;i--)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define LL long long
#define Travel(E, u) for(int i=E.start[u],v;v=E.e[i].a,i;i=E.e[i].next)
#define sqr(x) ((x)*(x))
#define pb push_back
#define read() (strtol(ipos, &ipos, 10))
#define pb push_back
#define pi 3.1415926535897

int n;
double V, X;
struct arr
{
	double v, x;
	bool operator<(const arr &t)const
	{
		return x < t.x;
	}
}a[10008];
double Least;
struct Tprogram
{
    void open()
    {
        freopen("", "r", stdin);
        freopen("", "w", stdout);
    }
    void close()
    {
        fclose(stdin);
        fclose(stdout);
    }
    void init()
    {
    	scanf("%d", &n);
    	scanf("%lf%lf", &V, &X);
    
    	rep(i,1,n)
    		scanf("%lf%lf", &a[i].v, &a[i].x);
    	sort(a+1, a+n+1);
    }
    bool check(double m)
    {
    	if (m < Least) return 0;
    	double V1 = 0, X1 = 0;
    	drep(i,n,1)
    	{
    		if (V1 + m*a[i].v <= V)
    		{
    			V1 += m*a[i].v;
    			X1 += m*a[i].v*a[i].x;
    		}
    		else
    		{
    			double t = (V - V1) / a[i].v;
    			X1 += t * a[i].v*a[i].x;
    			break;
    		}
    	}
    	if (X1/X <1-1e-12) return 0;
		V1 = 0; X1 = 0; 
    	rep(i,1,n)
    	{
    		if (V1 + m*a[i].v <= V)
    		{
    			V1 += m*a[i].v;
    			X1 += m*a[i].v*a[i].x;
    		}
    		else
    		{
    			double t = (V - V1) / a[i].v;
    			X1 += t * a[i].v*a[i].x;
    			break;
    		}
    	}
    	if (X1/X > 1+1e-12) return 0;
    	return 1;
    }
    void work()
    {
    	X *= V;
    	double t = 1e15, sum = 0;
    	rep(i,1,n)
    		t = min(t, a[i].v), sum += a[i].v;
    	double l = V / sum, r = V / t;
    	Least = V / sum;
		bool flag = 0; 
    	rep(i,1,100)
    	{
    		double m = (l + r) / 2;
    		if (check(m))
    		{
    			r = m;
    		}
    		else
    			l = m;
    	}
    	printf("%.10lf\n", l);
    }
}Program;
int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(i,1,T)
	{
    //Program.open();
    	printf("Case #%d: ", i);
    	Program.init();
    	bool flag1 = 0, flag2 = 0;
    	rep(i,1,n)
    	{
    		if (a[i].x > X - 1e-12) flag1 = 1;
			if (a[i].x < X + 1e-12) flag2 = 1;
		}
		if (!flag1 || !flag2)
			printf("IMPOSSIBLE\n");
		else
    	Program.work();
    }
    //Program.close();
    return 0;
}
