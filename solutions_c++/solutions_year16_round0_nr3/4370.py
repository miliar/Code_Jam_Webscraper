#include<cstdio>
#include<cstdlib>
#include<iostream>
#include <vector>
#include<cmath>
using namespace std;

#define loop(i,N) for(i=0;i<N;i++)
#define loop1(i,N) for(i=1;i<N;i++)
#define loop2(i,x,N) for(i=x;i<N;i++)

#define revloop(i,N) for(i=N;i>0;i--)
#define revloop2(i,x,N) for(i=x;i>N;i--)

#define s(n) scanf("%d",&n)
#define s2(n,k) scanf("%d %d",&n,&k)
#define p(n) printf("%d\n",n)
#define p2(n,k) printf("%d %d\n",n,k)

#define sl(n) scanf("%ld",&n)
#define sl2(n,k) scanf("%ld %ld" ,&n,&k)

#define pl(n) printf("%ld\n",n)
#define pl2(n,k) printf("%ld %ld\n",n,k)


#define sll(n) scanf("%lld",&n)
#define sll2(n,k) scanf("%lld %lld" ,&n,&k)

#define pll(n) printf("%lld\n",n)
#define pll2(n,k) printf("%lld %lld\n",n,k)


//#define sll(n) n=fastInput()

#define sc(n) scanf("%c",&n)
#define pc(n) printf("%c",n)

#define ss(n) scanf("%s",n)

#define sf(n) scanf("%f",&n)



#define MOD 1000000007

#define MAX9 100000000
#define MAX7 10000000
#define MAX6 1000000
#define MAX5 100000
#define MAX4 10000
#define MAX3 1000

typedef unsigned long long int ulli;
typedef signed long long int slli;
typedef unsigned long int uli;
typedef signed long int sli;
vector<uli> primes;
bool p_flag[MAX9]= {false};
ulli Powers[10][33];
ulli factor[MAX9]={0};
int test(ulli x)
{   ulli s;
    if(x&1)
    {
        if(x>=MAX9)
        {

            loop(s,primes.size())
            {
                if(!(x%primes[s]))
                    return primes[s];
            }
            return 0;
        }
        return factor[x];
    }
    else return 2;
}

void preecompute()
{
    uli i,j,k,ck=0;
    primes.push_back(2);
    for(i=3; i<MAX9; i+=2)
    {

        if(!p_flag[i])
        {
            primes.push_back(i);
            k=i+i;
            j=k+i;
            for(; j<MAX9; j+=k)
            {
                p_flag[j]=true;
                factor[j]=i;
            }

        }

    }
    for(i=2; i<=10; i++)
        for(j=0; j<19; j++)
            Powers[i][j]=pow(i,j);
}

int main()
{

    preecompute();
int Tst,N,J,t;
ulli temp,ans[11],i,j,k,ck=0;

    s(Tst);
    char str[33];
    Tst++;
    loop1(t,Tst)
    {
    s2(N,J);
    printf("Case #%d:\n",t);
    for(i=pow(2,N-1)+1; (i<pow(2,N)) && (J!=0); i+=2)
    {

        bool flag=false;
        for(j=2; j<11; j++)
        {
    temp=0;
            for(k=0; k<N; k++)
            {
                if(i&(1<<k))
                {
                    temp+=Powers[j][k];
                    str[k]='1';
                }
                else str[k]='0';
            }
            ans[j]=test(temp);
            if(!ans[j])
            {
flag=true;
j=11;
            }

//printf("( %d=%d)",j,ans);
        }


        str[k]='\0';
        if(!flag)
            {
            J--;
            k--;
            for(;k!=0;k--)
            pc(str[k]);
            pc(str[0]);
            for(k=2;k<11;k++)
            printf(" %lld",ans[k]);
            pc('\n');
            }



    }


}
    return 0;
}
