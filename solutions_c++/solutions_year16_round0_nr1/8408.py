#include<iostream>
#include<map>
#include<cstdio>
#include<vector>
using namespace std;
#define LL long long
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define LD long double
#define gc getchar_unlocked
#define pc putchar_unlocked
#define MOD 1000000007
#define MAXN 1000005
#define bitcount __builtin_popcount
#define INF 2000000000
#define EPS 1e-9
#define PI 3.14159265359
#define DEBUG 1
#define read(X) scanf("%lld",&X)
#define write(X) printf("%lld\n",&X)

template<typename T>T absll(T X)
{
    if(X<0)
        return -1*X;
    else
        return X;
}

int main()
{
    //std::clock_t start;
    //double duration;
    //start = std::clock();
    freopen("input.in","r",stdin);//redirects standard input
    freopen("output.out","w",stdout);//redirects standard output
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        LL N;
        scanf("%lld",&N);
        
        if(N==0)
        {
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        map<LL,LL> dig;
        LL num2=0;
        for(LL i=1;;i++)
        {
            LL num=i*N;
            num2=num;
            while(num>0)
            {
                dig[num%10]+=1;
                num/=10;
            }
            
            if(dig.size()==10)
            {
                break;
            }
        }
        printf("Case #%d: %lld\n",t,num2);
    }
    //duration=(clock()-start)/(double)CLOCKS_PER_SEC;
    //printf("\n\nDuration :- %0.9lf s",duration);
    return 0;
} 
