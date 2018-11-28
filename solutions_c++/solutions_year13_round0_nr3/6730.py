#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<numeric>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<deque>
#include<algorithm>
#include<iterator>
#include<utility>

using namespace std;

#define Abs(n) (n<0 ? -n: n)
#define Max(a,b) (a>b?a:b)
#define Min(a,b) (a<b?a:b)
#define Square(x) (x*x)
#define Memset(a,b) memset(a,b,sizeof(a))
#define Memcopy(a,b) memcopy(a,b,sizeof(a))

#define eps 1e-9
#define Pi 2*acos(0.0)
#define INF 0x7f7f7f7f

#define Read(f) freopen(f,"r",stdin);
#define Write(f) freopen(f,"w",stdout);

long ans [1005];

bool isPalin(long num)
{
    long x = num;
    long rev=0,rem;

    while(x>0)
    {
        rem=x%10;
        x=x/10;
        rev=(rev*10)+rem;
    }
    if(rev == num)
    return true;

    else
    return false;
}

bool isSquare(long n)
{
    long Sqrt = sqrt(n);

    if((Sqrt*Sqrt) == n)
    return true;

    else
    return false;
}

void dp()
{
    ans[0]=0;
    long i;

    for(i=1; i<=1000; i++)
    {
        if(isPalin(i) && isSquare(i))
        {
            long sqr = sqrt(i);

            if(isPalin(sqr))
            {
                ans[i]=ans[i-1]+1;
                //cout<<i<<" "<<ans[i]<<endl;
            }
            else
            ans[i]=ans[i-1];

        }
        else
        ans[i]=ans[i-1];

        //cout<<i<<" "<<ans[i]<<endl;
    }

}

int main()
{
    dp();

    long T,xx=1,a,b;

    //Read("c.IN");
    //Write("c.out");

    cin>>T;

    while(T--)
    {
        cin>>a>>b;

        if(a>b)
        swap(a,b);

        a=a-1;

        long number = ans[b]-ans[a];

        printf("Case #%ld: %ld\n",xx++,number);
    }
    return 0;
}
