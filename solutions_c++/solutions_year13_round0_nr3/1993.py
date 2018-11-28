#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>

using namespace std;

map<int,int> map1;
map<int,int>::iterator it;

int checkPalindrome(long long num)
{
    long long temp = num,revNum=0,xchg;
    while (temp > 0)
    {
         xchg = temp % 10;
         revNum = revNum * 10 + xchg;
         temp = temp / 10;
    }
    return num==revNum;
}

void preCal()
{
    long long limit=1;
    int n=7;
    map1[0]=0;
    while(n--)
        limit*=10;
    long long sqr;
    for(long long i=1,n=0;i<=limit;++i)
    {
        sqr=i*i;
        if(checkPalindrome(i)&&checkPalindrome(sqr))
        {
            //cout<<i<<" : "<<sqr<<endl;
           map1[i]=++n;
        }
    }
}

int main()
{
    int i,j,k,l;
    int T,t;
    preCal();
    freopen("C-large-1.in","r",stdin);
    freopen("output-C.txt","w",stdout);

    cin>>T;
    for(t=1;t<=T;++t)
    {
        long long A,B;
        cin>>A>>B;
        long long a,b;
        a=sqrt(A);
        b=sqrt(B);
        if(a*a<A)
            a++;
        it=map1.upper_bound(b);
        it--;
        long long ans=(*it).second;
        it=map1.lower_bound(a);
        it--;
        ans-=((*it).second);
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
