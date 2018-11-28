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
    #define trace1(x)           cout<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cout<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
#endif

using namespace std;


#define n_ 10004



 //0 gabriel.

bool cal(int l,int r,int x)
{

    if(x==1) return 0;

    if(x==2)
    {
        if((l*r)%2==0) return 0;
        else return 1;

    }

    if(x==3)
    {

        //3,2 2,3 ,3,3 3,4
        if((l%3==0&&r%2==0)||(l%2==0&&r%3==0)||(l==3&&r==3)) return 0;

        else return 1;


    }


    if(x==4)
    {
        //3,4 4,3 4,4
        if(l==3&&r==4||r==3&&l==4||r==4&&l==4)
        return 0;
        else return 1;


    }
}



int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,x,r,l;
    sd(test);
    int case_=1;
    while(test--)
    {

        sd(x);
        sd(l);
        sd(r);
        if(cal(l,r,x)) printf("Case #%d: RICHARD\n",case_);

        else  printf("Case #%d: GABRIEL\n",case_);
        case_++;
    }
    return 0;


}
