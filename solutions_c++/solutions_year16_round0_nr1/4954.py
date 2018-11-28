#include<iostream>
#include<stdio.h>

using namespace std;

#define lli long long int

lli nmbr;

int flag[15];

int check(){
        for(int i=0;i<10;i++){
                if(!flag[i]) return 0;
        }
        return 1;
}

void clr(){
        for(int i=0;i<10;i++){
                flag[i] = 0;
        }
}

void  point(lli n){
    while(n/10){
        flag[n%10]++;
        n = n/10;
    }
    flag[n%10]++;
}

lli trying(lli n){
    clr();
    point(n);
    lli t;
    for(int i=2;check()==0;i++){
        t = i*n;
        point(t);
    }
    return t;
}

void result(){
    for(int i=1;i<=1000000;i++){
        cout<<i<<" "<<trying(i)<<endl;
    }
}

int main(){
    freopen("A-large.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //result();
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        cin>>nmbr;
        cout<<"Case #"<<cas<<": ";
        if(nmbr==0) cout<<"INSOMNIA"<<endl;
        else cout<<trying(nmbr)<<endl;
    }
}
