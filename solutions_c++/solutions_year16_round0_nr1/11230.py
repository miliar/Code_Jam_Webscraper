#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
long long  n,times,tmp;
int i,t,flag[11],sum;
bool solve(long long n){
    while(n){
        if(flag[n%10]==0){
            sum++;
            flag[n%10]=1;
        }
        n/=10;
    }
    if(sum==10)
        return true;
    else
        return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    i=1;
    while(i<=t){
        cin>>n;
        if(n==0){
          cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
          i++;
          continue;
        }
        sum=0;
        memset(flag,0,sizeof(flag));
        times=1;
        tmp=n;
        while(!solve(tmp)){
            times++;
            tmp=n*times;
        }
        cout<<"Case #"<<i<<": "<<tmp<<endl;
        i++;
    }
    return 0;
}
