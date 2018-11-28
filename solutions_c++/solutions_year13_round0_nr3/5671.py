#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
long long isSquare(long long);
long long isPal(long long);
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);
    long long t,a,b,k,i,j,aux;
    cin>>t;
    bool ans;
    for(k=1;k<=t;k++){
        cin>>a>>b;
        ans=false;
        aux=0;
        for(i=a;i<=b;i++){
            ans=isSquare(i)&&isPal(i)&&isPal((int)sqrt(i));
            if(ans)aux++;
        }
        cout<<"Case #"<<k<<": "<<aux<<endl;
    }
}

long long isSquare(long long n){
    long long r;
    r=(long long)sqrt(n);
    if(n==(r*r)){
        return true;
    }
    return false;
}

long long isPal(long long n){
    long long num=n;
    long long inv=0,d,p=0;
    d=num;
    while(d>0){
        inv=inv*10+d%10;
        d/=10;
    }
    if(num==inv)return true;
    return false;
}
