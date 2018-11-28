#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

long long mult_mod(long long a,long long b,long long c)
{
    a%=c;
    b%=c;
    long long ret=0;
    while(b)
    {
        if(b&1){ret+=a;ret%=c;}
        a<<=1;
        if(a>=c)a%=c;
        b>>=1;
    }
    return ret;
}

long long pow_mod(long long x,long long n,long long mod)//x^n%c
{
    if(n==1)return x%mod;
    x%=mod;
    long long tmp=x;
    long long ret=1;
    while(n)
    {
        if(n&1) ret=mult_mod(ret,tmp,mod);
        tmp=mult_mod(tmp,tmp,mod);
        n>>=1;
    }
    return ret;
}  

bool check(long long a,long long n,long long x,long long t)
{
    long long ret=pow_mod(a,x,n);
    long long last=ret;
    for(int i=1;i<=t;i++)
    {
        ret=mult_mod(ret,ret,n);
        if(ret==1&&last!=1&&last!=n-1) 
            return true;
        last=ret;
    }
    if(ret!=1) 
        return true;
    return false;
}

bool Miller_Rabin(long long n)
{
    if(n<2)return false;
    if(n==2)return true;
    if((n&1)==0) return false;
    long long x=n-1;
    long long t=0;
    while((x&1)==0){x>>=1;t++;}
    for(int i=0;i<10;i++)
    {
        long long a=rand()%(n-1)+1;
        if(check(a,n,x,t))
            return false;
    }
    return true;
}

int main(){
    int N,J,roll=0;
    cin>>N;
    cin>>N>>J;
    long long bi_base=pow(2,N-1)+1;
    long long bi_limit=pow(2,N)-1;
    //cout<<"b/t"<<bi_base<<" "<<bi_limit<<endl;
    cout<<"Case #1:"<<endl;
    while(bi_base<=bi_limit){
        long long tmp=bi_base;
        long long base=0;
        int fang=0;
        while(tmp!=0){
            base+=(tmp%2)*pow(10,fang++);
            tmp/=2;
        }
        //cout<<"base:"<<base<<endl; 
        int i=1;
        int flag=1;
        long long reals[9]={0};
        while(++i<=10){
            long long tmbase=base;
            long long realnum=0;
            int mi=0;
            do{
                int a=tmbase%2;
                realnum+=a*pow(i,mi++);
            }
            while((tmbase/=10)!=0);
            if(Miller_Rabin(realnum)){
               flag=0; 
               break;
            }else{
                //cout<<"Done check on "<<i<<" base"<<endl;
            }
            reals[i-2]=realnum;
        }
        if(flag==1){
            cout<<base<<" ";
            for(int i=1;i<10;i++){
                long long s=2;
                while(reals[i-1]%++s!=0){}
                cout<<s<<" ";
            }
            cout<<endl;
            roll++;
        }
        if(roll==J){
            break;
        }
        bi_base+=2;
    }
}

