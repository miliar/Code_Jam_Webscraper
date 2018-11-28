#include <bits/stdc++.h>
#include <sstream>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <fstream>
#include <numeric>
#include <cstring>
using namespace std;
template<class T1> void deb(T1 e1)
{
    cout<<e1<<endl;
}
template<class T1,class T2> void deb(T1 e1,T2 e2)
{
    cout<<e1<<" "<<e2<<endl;
}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3)
{
    cout<<e1<<" "<<e2<<" "<<e3<<endl;
}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;
}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;
}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;
}


#define    pb   push_back
#define    pp   pop_back
#define    pi   2*acos(0.0)
#define    pf   printf
#define    sf   scanf
#define    EPS  1e-10
#define    clr(a)       memset(a,0,sizeof(a))
#define    full(a)      memset(a,63,sizeof(a))
#define    max3(a,b,c)  max(a,max(b,c))
#define    min3(a,b,c)  min(a,min(b,c))
#define    sf1(a)       scanf("%d",&a)
#define    sf2(a,b)     scanf("%d%d",&a,&b)
#define    sf3(a,b,c)   scanf("%d%d%d",&a,&b,&c)
#define    sf1l(a)      scanf("%lld",&a)
#define    sf2l(a,b)    scanf("%lld%lld",&a,&b)
#define    sf3l(a,b,c)  scanf("%lld%lld%lld",&a,&b,&c)
#define    sf1d(a)      scanf("%lf",&a)
#define    sf2d(a,b)    scanf("%lf%lf",&a,&b)
#define    sf3d(a,b,c)  scanf("%lf%lf%lf",&a,&b,&c)
#define    READ(f)      freopen(f, "r", stdin)
#define    WRITE(f)     freopen(f, "w", stdout)
#define        boost    ios_base::sync_with_stdio(0)
#define    sr_pr(s1)    printf("%s",s1.c_str())
#define    fo(i,n)      for(i=0;i<n;i++)
#define    MAX
#define    MOD

typedef long long ll;
typedef unsigned long long ull;
/*bitmask
int set( int n, int pos ){
    return n = n|( 1<<pos );
}
bool check( int n, int pos ){
    return (bool)( n&( 1<<pos ) );
}
int reset( int n, int pos ){
    return n = n&~( 1<<pos );
}*/

//int dx[]= {0,0,1,-1};
//int dy[]= {-1,1,0,0};
//int dx[]= {1,1,0,-1,-1,-1,0,1};/*8 move*/
//int dy[]= {0,1,1,1,0,-1,-1,-1};/*8 move*/
//int dx[]={1,1,2,2,-1,-1,-2,-2};/*knight move*/
//int dy[]={2,-2,1,-1,2,-2,1,-1};/*knight move*/
int ans[]={0,10,90,30,92,90,90,70,96,90,90,110,156,104,238,180,256,119,90,190,900,189,198,207,456,900,390,189,476,203,270,310,576,330,918,560,396,370,190,390,920,369,378,301,396,360,506,470,576,490,900,459,936,424,594,495,672,570,290,590,900,549,558,504,576,715,726,469,952,345,560,710,792,730,518,900,912,539,390,790,960,729,574,830,924,680,946,609,792,801,450,910,552,930,564,665,576,970,784,990,900,909,918,721,936,945,954,749,972,545,990,1110,896,904,798,805,1276,819,590,1071,1560,968,976,1107,2356,9000,1890,889,896,903,1040,1048,792,1064,938,945,952,1096,690,1390,2380,987,1136,1001,1296,1160,730,1176,1036,1043,1800,1208,912,918,924,1085,936,1099,790,1590,2560,1127,1458,1304,1476,2475,5478,1169,3192,1352,1190,1197,1892,1038,870,2625,1936,1239,890,1253,900,905,910,1098,920,1665,930,1309,940,1701,1520,1910,960,1930,970,2145,980,1970,990,1990,9000};
int main()
{
    boost ;
    ifstream fin;
    ofstream fout;
    fin.open("inputa.txt");
    fout.open("outputa.txt");
    int t,i1;
    fin>>t;
    for(i1=1;i1<=t;i1++)
    {
        vector<int> ans;
        int a,now=0,i,j,k;
        fin>>a;
        if(a==0)
        {
            fout<<"Case #"<<i1<<": INSOMNIA"<<endl;
            continue;
        }
        set<int> st;
        for(j=1; ; j++)
        {
            now+=a;
            int temp=now;
            stringstream ss;
            ss << temp;
            string str = ss.str();
            int len=str.size();
            for(k=0;k<len;k++)
            {
                st.insert(str[k]-'0');
            }
            if(st.size()==10)
            {
                ans.pb(now);
                break;
            }
            //fout<<str;
        }
        /*if(a==0) fout<<"Case #"<<i1<<": INSOMNIA"<<endl;
        else*/
        fout<<"Case #"<<i1<<": "<<ans[0]<<endl;
        //for(int i=1;i<=100;i++) fout<<i*a<<" ";
        //fout<<a+10<<endl;*/
    }
    return 0;
}
