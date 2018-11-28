#include<iostream>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#define N 8
#define L 4

using namespace std;

bool pali(int n){
    string s="";
    while(n>0){
        s+=n%10+'0';
        n/=10;
    }
    string aux=s;
    reverse(aux.begin(),aux.end());
    if(s==aux)return true;
    return false;
}

bool val(int n){
    int raiz=(int)sqrt(1.*n);
    if(raiz*raiz!=n)return false;
    if(pali(raiz)&&pali(n))return true;
    return false;
}

int main(){
    int nc;
    cin>>nc;
    for(int caso=1;caso<=nc;caso++){
        int a,b;
        cin>>a>>b;
        int ct=0;
        for(int i=a;i<=b;i++)if(val(i))ct++;
        cout<<"Case #"<<caso<<": "<<ct<<endl;
    }
}
