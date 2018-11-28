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
    	double C, F, X, ans = 0;
    	scanf("%lf%lf%lf", &C, &F, &X);
    	int n = (X*F-2*C) / (C*F);
    	n = max(n, 0);
    	rep(i,1,n)
    		ans += C / ((i - 1)*F + 2);
    	ans += X / (n*F+2);
    	printf("%lf\n", ans);
    }
    void work()
    {
    	
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
