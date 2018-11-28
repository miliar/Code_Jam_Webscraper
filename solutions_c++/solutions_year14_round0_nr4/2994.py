#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1000

using namespace std;

int n;
double a[MAX + 100];
double b[MAX + 100];

int game1()
{
    int left = 0,right = n-1;
    int pos = n-1;
    int ret = 0;
    while(true)
    {
        if(left > right) break;
        if(pos < 0) break;
        if(a[right] < b[pos])
        {
            left++;
        }
        else if(a[right] > b[pos])
        {
            right--;
            ret++;            
        }
        pos--;
    }
    return ret;    
}

int game2()
{
    int ret = 0;
    int pos1 = n-1,pos2 = n-1;
    while(true)
    {
        if(a[pos1] < b[pos2]) 
        {
            pos2--;
        }
        else
        {
            ret++;
        }
        pos1--;
        
        if(pos1 < 0 || pos2 < 0) break;
    }
    return ret;
}

void solve(int ca)
{
    scanf("%d",&n);
    FOR(i,0,n-1) scanf("%lf",&a[i]);
    FOR(i,0,n-1) scanf("%lf",&b[i]);    
    
    sort(a,a+n);
    sort(b,b+n);
    int x = game1();
    int y = game2();
    printf("Case #%d: %d %d\n",ca,x,y);
}

int main()
{
    int t;
    scanf("%d",&t);
    FOR(ca,1,t)
    {
        solve(ca);
    }
    return 0;
}
