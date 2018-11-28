//#include <bits/stdc++.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <numeric>
#include <stack>
#include <functional>
#include <bitset>
#include <iomanip>

#include <ctime>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>
#include <cstdlib>

#define _ ios_base::sync_with_stdio(0);
#define ms(ar,val) memset(ar,val,sizeof(ar))
#define all(s) (s).begin(),(s).end()
#define rp1(i,s,n) for(int i=s;i<n;++i)
#define rp(i,n) rp1(i,0,n)
#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define pb push_back
#define LL long long
#define Read(x) freopen(x,"r",stdin)
#define Write(x) freopen(x,"w",stdout)
#define st(N,pos) (sts[N]=sts[N] | (1<<pos))
#define check(N,pos) ((bool)(sts[N] & (1<<pos)))
#define i_s(num)  static_cast<ostringstream*>( &(ostringstream() << num) )->str();
#define inf INT_MAX
#define mp(a,b) make_pair(a,b)
#define pii pair<int,int>
#define PQ priority_queue
#define F first
#define S second
#define EPS 1e-11
#define hi 100010

///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;

double fun(double c,double f,double x,double cur)
{

    double t1 = x/cur;
    double t2 = (c/cur) + (x/(cur+f));
    if(t1<t2)return t1;
    else return c/cur + fun(c,f,x,cur+f);
}


int main()
{
#if defined( rifat_pc )
    Write("out.txt");
    Read("B-large.in");
    //Read("in.txt");
#endif
    int tst,cnt=1;
    cin>>tst;
    while(tst--)
    {
        double x,c,f;
        cin>>c>>f>>x;
        double ans=0;
        double cur =2;
        while(true)
        {
            double t1 = x/cur;
            double t2 = (c/cur) + (x/(cur+f));
            if(t1<t2){
                ans+=t1;
                break;
            }
            else{

                ans+= (c/cur) ;
                cur+=f;
            }
        }
        printf("Case #%d: %.7lf\n",cnt++,ans);
    }



    return 0;
}



