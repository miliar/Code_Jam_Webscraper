#include<bits/stdc++.h>
using namespace std;
bool isprime[100000001];
int prim[5761455];
void sieve(){
    isprime[0]=1;isprime[1]=1;
    for(int i=2;i<=10000;i++){
        for(int j=i*i;j<=100000000;j+=i){
            isprime[j]=1;
        }
    }
    int cnt=0;
    for(int i=2;i<=100000000;i++){
        if(isprime[i]==false){
            prim[cnt]=i;
            cnt++;
        }
    }
    return;
}
long long base[11];
bool chk_prime(long long n){
    long long sq=sqrt(n);
    if(n<=100000000)
        return !isprime[n];
    for(int i=0;i<5761455 and prim[i]<=sq;i++){
        if(n%prim[i]==0)
        return false;
    }
    return true;
}
long long fac(long long n){
    long long sq=sqrt(n);
    for(int i=0;i<5761455 and prim[i]<=sq;i++){
        if(n%prim[i]==0)
        return prim[i];
    }
}
int main(){
    int t;
    t=1;//cin>>t;
    sieve();
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<":\n";
        long long n,st,fin;
        int cnt=0,j;
        n=16;j=50;//cin>>n>>j;
        fin=(long long)1<<n;st=fin/2;st++;
        for(long long num=st;num<fin;num+=2){
            bool flag=true;
            string s;
            long long tmp=num;
            int siz=n;
            while(tmp>0){
                s.push_back(tmp%2+'0');
                tmp=tmp>>1;
            }
            for(long long bas=2;bas<=10;bas++){
                base[bas]=0;
                long long po=1;
                for(int i=0;i<siz;i++){
                    base[bas]+=(po*(s[i]-'0'));
                    po*=bas;
                }
                if(chk_prime(base[bas])==true){
                    flag=0;
                    break;
                }
            }
            if(flag){
                for(int i=0;i<siz;i++)
                    cout<<s[siz-i-1];
                cout<<" ";
                for(int bas=2;bas<=10;bas++){
                    cout<<fac(base[bas])<<" ";
                }
                cout<<endl;
                cnt++;
            }
            if(cnt==j){
                break;
            }
        }
    }
}
