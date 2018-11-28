#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;

bool palin(long long n){
    long long a,b;
    a=n;
    b=0;
    while(a>0){
        b=b*10+a%10;
        a=a/10;
        }
    if(b==n)return true;
    return false;
    }

int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    long long tg,th,t,i,cases,s;
    vector<long long> v;
    for(i=1;i<10000000;i++){
        if(palin(i)&&palin(i*i)){
            v.push_back(i*i);
            }
        }
    cin>>t;
    for(cases=1;cases<=t;cases++){
        s=0;
        cout<<"Case #"<<cases<<": ";
        cin>>tg>>th;
        for(i=0;i<v.size();i++){
            if(tg<=v[i]&&v[i]<=th){
                s++;
                }
            }
        cout<<s<<endl;
        }
    }
