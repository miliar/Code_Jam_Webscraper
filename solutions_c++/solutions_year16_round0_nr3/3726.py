#include <iostream>
#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include <bitset>         // std::bitset
#include <math.h>       /* pow */

#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define LL long long

// http://www.zzzyk.com/show/3430e0fa066c28a3.htm

const int S=50;
const   int N =16;
const   int J =50;

using namespace std;

LL mult_mod(LL a,LL x,LL n)//返回(a*x) mod n,a,x,n<2^63
{
    a%=n;
    x%=n;
    LL ret=0;
    while(x)
    {
        if(x&1)
        {
            ret+=a;
            if(ret>=n)ret-=n;
        }
        a<<=1;
        if(a>=n)a-=n;
        x>>=1;
    }
    return ret;
}
LL pow_mod(LL a,LL x,LL n)//返回a^x mod n
{
    if(x==1)return a%n;
    int bit[70],k=0;
    while(x)
    {
        bit[k++]=(x&1?1:0);
        x>>=1;
    }
    LL ret=1;
    for(--k; k>=0; k--)
    {
        ret=mult_mod(ret,ret,n);
        if(bit[k])ret=mult_mod(ret,a,n);
    }
    return ret;
}
bool judge(LL a,LL n,LL x,LL t)//以a为基，n-1=x*2^t，检验n是不是合数
{
    LL ret=pow_mod(a,x,n),flag=ret;
    for(LL i=1; i<=t; i++)
    {
        ret=mult_mod(ret,ret,n);
        if(ret==1&&flag!=1&&flag!=n-1)return true;
        flag=ret;
    }
    if(ret!=1)return true;
    return false;
}
bool Miller_Rabin(LL n)
{
    if(n==2||n==5||n==7||n==11)return true;
    if(n%2==0||n%5==0||n%7==0||n%11==0)return false;
    LL x=n-1,t=0;
    while((x&1)==0)x>>=1,t++;
    bool flag=true;
    if(t>=1&&(x&1)==1)
    {
        for(int i=1; i<=S; i++)
        {
            LL a=rand()%(n-1)+1;
            if(judge(a,n,x,t))
            {
                flag=true;
                break;
            }
            flag=false;
        }
    }
    if(flag)return false;
    else return true;
}
//*******pollard_rho 算法进行质因数分解*****************
LL factor[100];//质因子
int tot;//质因子个数
LL gcd(LL a,LL b)
{
    if (a==0) return 1;
    if (a<0) return gcd(-a,b);
    while (b)
    {
        LL t=a%b;
        a=b;
        b=t;
    }
    return a;
}
LL Pollard_rho(LL x,LL c)
{
    LL i=1,x0=rand()%x,y=x0,k=2;
    while (1)
    {
        i++;
        x0=(mult_mod(x0,x0,x)+c)%x;
        LL d=gcd(y-x0,x);
        if (d!=1 && d!=x)
            return d;
        if (y==x0) return x;
        if (i==k)
        {
            y=x0;
            k+=k;
        }
    }
}
void find_factor(LL n) //递归进行质因数分解N
{
    if (tot>0) return;
    if (Miller_Rabin(n))
    {
        factor[tot++] = n;
        return;
    }
    LL p=n;
    while (p>=n) p=Pollard_rho(p,rand() % (n-1) +1);
    find_factor(p);
    find_factor(n/p);
}

void solve()
{
    string S;
    int j=0;
    unsigned LL n;
    n = (1<<(N-1)) + 1;

    while (j<J)
    {
        bool FOUND = true;
        std::bitset<N> bitsetn (n);
        string result="";
        result = bitsetn.to_string();
        for(int base=2; base<=10; base++)
        {
            LL n2=0;
            for (int i =0; i<N; i++)
            {
                if (bitsetn[i]>0)
                    n2 += pow(base,i) ;
            }

            if(Miller_Rabin(n2))
            {
                FOUND=false;
                break;
            }
            tot=0;
            char chartmp[90];
            find_factor(n2);
            sprintf(chartmp,"%lld", factor[0]);
            string stringtmp = chartmp;
            result = result + " " + stringtmp;
        }
        if (FOUND)
        {
            cout<<result<<endl;
            j++;
        }
        n +=2 ;
    }

}




int main()
{
    freopen("/home/happylife/programing/code_jam/C-small-attempt0.out","w",stdout);
    cout<<"Case #"<<1<<":" << endl;
    solve();

    return 0;
}
