#include<bits/stdc++.h>
using namespace std;
struct point {int x;int y;};
bool operator <(const point &a,const point &b){return (a.x<b.x);}
int compare (const void * a, const void * b){return ( *(int*)a - *(int*)b );}
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) REP(i,0,b)
#define si(n) scanf("%d",&n)
//#define sort(arrr,n) qsort(arrr,n,sizeof(int),compare)
int gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}

long double C,F,X;
long double Time(int farms)
{
    long double sum=0.0;int i=0;
    for(i=0;i<farms;i++)
        sum += (C/((long double)(2+(long double)i*F)));
    sum += (X/((long double)(2+(long double)i*F)));
    return sum;
}

int main()
{
    int tc,t,mid;
    cin >> tc;
    rep(t,tc)
    {
        cin >> C >> F >> X;
        int low=0,high=10000;
        while(1)
        {
            mid = (low+high)/2;

            if(low==mid)
                break;
            if(Time(mid)<Time(mid-1))
                low=mid;
            else
                high=mid;
        }
        printf("Case #%d: %.7LF\n",t+1,Time(mid));
    }

	return 0;
}
