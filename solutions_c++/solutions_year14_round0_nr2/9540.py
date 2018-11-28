#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
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
#include <fstream>
#include <climits>
#define LL long long
#define set_bit(aa,bb) (aa|(1<<bb))
#define check_bit(aa,bb) (aa&(1<<bb))
#define MX 120001
#define eps 1e-10



using namespace std;

/*

LL gcd(LL a,LL b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}

LL bigmod(LL p,LL e,LL M)
{
    if(e==0)return 1;
    if(e%2==0)
    {
        LL t=bigmod(p,e/2,M);
        return (t*t)%M;
    }
    return (bigmod(p,e-1,M)*p)%M;
}

LL modinverse(LL a,LL M)
{
    return bigmod(a,M-2,M);
}




bool is_prime[MAX];
L prime[MAX];

bool sieve()
{
    long i,j;
    prime[0]=2;
    int k=1;
    int sq=(sqrt(MAX));
    for(i=3; i<=sq; i+=2)
    {
        if(!is_prime[i])
        {
            for(j=i*i; j<=MAX; j+=(2*i))
                is_prime[j]=1;
        }
    }
    for(j=3; j<=MAX; j+=2)
    {
        if(!is_prime[j])
        {
            prime[k++]=j;
        }
    }
}


long NOD(long n)
{
    int  i,j,k;
    long sq=sqrt(n);
    long res=1;
    for(i=0; prime[i]<=sq; i++)
    {
        int cnt=1;
        if(n%prime[i]==0)
        {
            while(n%prime[i]==0)
            {
                cnt++;
                n=n/prime[i];
                if(n==1) break;
            }
            res*=cnt;
            sq=sqrt(n);
        }
    }
    if(n>1) res*=2;
    return res;
}
*/

double dp[100001];
double X,C,F;

int need(double a)
{
    return (double)a/(double)C;
}


double solve(int amount)
{
    //cout<<amount<<endl;
    if((amount)>=X) return X/((double)amount*F+2.0);
    double &ret=dp[amount];
    if(ret!=-1.0) return ret;
    ret=(double)X/((double)amount*F+2.0);
//    if((amount*F+2.0+xtra)>=C){
//        int a=need(amount*F+2.0+xtra);
//       // cout<<a<<endl;
//        ret=min(ret,  solve(amount+a, amount*F+2.0+xtra-C*a)+ 1.0);
//    }
//    else
    ret=min(ret,  solve(amount+1)+C/((double)amount*F+2.0));
   //   cout<<amount<<" "<<ret<<endl;
    return ret;
}




int main()
{
    FILE *fp;
    fp=fopen("out1.txt", "w");
    int i,j,k;
    int cases=1;
    int t;
    cin>>t;
    while(t--)
    {
        cin>>C>>F>>X;
        for(i=0; i<=100000; i++)
            dp[i]=(-1.0);
        double res=solve(0);
    fprintf(fp,"Case #%d: %.8lf\n",cases++, res+eps);
    }
    return 0;
}
/*

1
1 500 503


*/
