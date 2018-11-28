/*.....................
Author : PTY
Time : 14/04/02
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
double a[100008], b[100008];
struct Tprogram
{
    void open()
    {
        freopen("1.in", "r", stdin);
        freopen("1.out", "w", stdout);
    }
    void close()
    {
        fclose(stdin);
        fclose(stdout);
    }
    void init()
    {
    	scanf("%d", &n);
    	rep(i,1,n)
    		scanf("%lf", &a[i]);
    	rep(i,1,n)
    		scanf("%lf", &b[i]);
    	sort(a+1, a+n+1);
    	sort(b+1, b+n+1);
    }
    void work()
    {
    	int j = 1, tmp = 0;
    	rep(i,1,n)
    	{
    		if (j <= n && a[i] > b[j]) tmp++, j++;
    	}
    	printf("%d ", tmp);
    	tmp = 0; j = 1;
    	//rep(i,1,n)
    	//	printf("%lf %lf\n", a[i], b[i]);
    	rep(i,1,n)
    	{
    		if (j <= n && b[i] > a[j]) tmp++, j++;
    	}
    	printf("%d\n", n - tmp);
    }
}Program;
int main()
{
    Program.open();
    int t;
    scanf("%d", &t);
    rep(i,1,t)
    {
    	printf("Case #%d: ", i);
   		Program.init();
    	Program.work();
	}
    Program.close();
    return 0;
}
