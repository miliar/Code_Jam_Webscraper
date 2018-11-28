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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
bool is(string S)
{
    int i=0;
    int j=S.size()-1;
    while(i<j)
    {
        if(S[i++]!=S[j--])
            return 0;
    }
    return 1;
}
long long  P[]= {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    /* vector<long long >R;
     for (long long  i=1;i<=10000000;i++)
     {
         stringstream o,y;
         o<<i;
         if(is(o.str()))
         {
             y<<i*i;
             if(is(y.str()))
             {
                 R.push_back(i*i);
                 cout<<i<<" "<<i*i<<endl;
             }
         }

     }*/




    vector<long long >Q(P,P+39);
    int T;
    long long A,B;



    scanf("%d",&T);
    for (int i=1; i<=T; i++)
    {
        vector<long long >::iterator l,r;
        scanf("%lli %lli",&A,&B);
        if(A>4004009004004)
            printf("Case #%d: 0\n",i);

        else
        {
            l=lower_bound(Q.begin(),Q.end(),A);
            r=lower_bound(Q.begin(),Q.end(),B);
            if(*r>B)
                r--;

            printf("Case #%d: %lli\n",i,(long long )(r-l)+1);



        }



    }
}
