#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define clean(a,b) memset(a,b,sizeof(a))
#define oo 1<<20
#define dd double
#define ll long long
#define ull unsigned long long
#define ff float
#define EPS 10E-6
#define fr first
#define sc second
#define MAXX 10000100
#define PRIME_N 1000000
#define INFI 1<<30
#define SZ(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define MODD 1000000007

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1};   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull

dd sum[MAXX];

dd chk(int step,dd f, dd x)
{
    return sum[step]+(x/(2.0 +((step)*f) ));
}

dd find_sol(dd c,dd f,dd x)
{
    int l = 0 , h = 1000000;

    sum[0] = 0;
    for(int i = 1 ; i<=1000000 ; i++)
        sum[i] = sum[i-1]+ ((c/(2.0+ (i-1)*f)));
    int cnt = 50;
    while(cnt-- && l<h)
    {
//        cout<<l<<" - "<<h<<endl;
        int m1 = (l+h)/3;
        int m2 = (2*(l+h))/3;

        dd v1 = chk(m1,f,x);
        dd v2 = chk(m2,f,x);
        if(v1<v2)
            h =m2;
        else l = m1;
    }
    dd sol = x/2.0;
    for(int i = l ; i<=h ; i++)
        sol = min(sol , chk(i , f,x));

    return sol;
}

int main()
{
    freopen("inpBL.txt" , "r+" , stdin);
    freopen("outBL.txt" , "w+" , stdout);
    int tcase,cas=1;

    scanf(" %d" , &tcase);

    while(tcase--)
    {
        dd c,f,x;

        scanf(" %lf %lf %lf",&c,&f,&x);
        dd tmpsol = find_sol(c,f,x);

//        dd sol = x/2.0;
//        dd extra = c/2.0;
//        for(int i = 1 ;  ; i++)
//        {
//            dd tmp = extra + (x/(2.0+i*f));
//            if(tmp<sol) sol = tmp;
//            else break;
//            extra += (c/(2.0+i*f));
//        }


//        bool flag = 0;
//
//
//        if(fabs(sol - tmpsol)<EPS) flag =1;

        printf("Case #%d: %.7lf\n",cas++,tmpsol);
//        if(flag) printf("YES\n");
//        else printf("NO\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


