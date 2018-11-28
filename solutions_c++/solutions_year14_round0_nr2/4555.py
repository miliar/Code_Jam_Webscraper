#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
#define FOR(i,l,n) for(int i=l;i<n;i++)
#define INT(c) int c;scanf("%d",&c);
#define LL(c) long long c;scanf("%ll",&c);
#define ULL(c) unsigned long long c;scanf("%llu",&c);
#define MOD 1000000007
#define Ull unsigned long long
#define Ll lnong long
#define chk(x) x%=MOD;
int main()
{
    INT(t)
    FOR(i,0,t)
    {
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double time_so_far=0;
        double current_rate=2.0;
        int reached=0;
        while(!reached)
        {
            if((x/current_rate)>((c/current_rate)+(x/(current_rate+f))))
            {
                time_so_far+=(c/current_rate);
                current_rate+=f;
            }
            else
            {
                time_so_far+=(x/current_rate);
                reached=1;
            }
        }
        printf("Case #%d: %.7lf\n",i+1,time_so_far);
    }
    return 0;
}


