#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<map>
#include<list>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<set>




#define FOREACH(it,c) for(auto it=(c).begin();it!=(c).end();++it)
#define all(s) s.begin(),s.end()
#define pb push_back
#define mp make_pair
#define sd(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define pd(x) printf("%d",x)
#define ll long long
const int mod = ((1E9)+7);
const int intmax = ((1E9)+7);




#ifndef ONLINE_JUDGE
#define TRACE
#endif
#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
#endif

using namespace std;



int a[10005];






int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    int test,b,c,n;
    sd(test);
    int case_=1;
    while(test--)
    {

              sd(n);
               for(int i=0;i<n;i++)
               {

                   sd(a[i]);
               }



        ll summin=0;
        ll upperlimit=0;
        ll max_=-1;
        for(int i=0;i<n-1;i++)
        {
            max_=max((ll)a[i]-(ll)a[i+1],max_);

            if(a[i+1]<a[i])
            {
                summin+=(ll)a[i]-a[i+1];
            }
        }


        upperlimit=a[n-2]-a[n-1];

        upperlimit=max_;



        ll summax=0;
        ll eat;

        for(int i=0;i<n-1;i++)
        {


                 eat =min((ll)a[i],upperlimit);


            summax+=eat;

        }
        printf("Case #%d: %lld %lld\n",case_,summin,summax);
        case_++;
    }


    return 0;


}
