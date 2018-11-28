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
        string str;
        cin>>str;
        
        bool flag=true;
        int N=str.length();
        int negpos=-1;
        for(int i=0;i<N;i++)
        {
            if(str[i]=='-')
            {
                flag&=false;
                break;
            }
        }
        
        if(flag)
        {
            printf("Case #%d: 0\n",t);
        }
        else
        {
            LL cnt=0;
            while(1)
            {
                negpos=-1;
                for(int i=N-1;i>=0;i--)
                {
                    if(str[i]=='-')
                    {
                        negpos=i;
                        break;
                    }
                }
                
                if(negpos==-1)
                {
                    break;
                }
                
                for(int i=0;i<=negpos;i++)
                {
                    if(str[i]=='+')
                    {
                        str[i]='-';
                    }
                    else
                    {
                        str[i]='+';
                    }
                }
                ++cnt;
            }
            printf("Case #%d: %lld\n",t,cnt);
        }
    }
    //duration=(clock()-start)/(double)CLOCKS_PER_SEC;
    //printf("\n\nDuration :- %0.9lf s",duration);
    return 0;
} 
