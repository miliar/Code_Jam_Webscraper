#include<iostream>
#include<cmath>
#include<string>
using namespace std;
string numToStr(long long a){
    string str="";
    while(a){
        str+=char(a%10+48);
        a/=10;
    }
    return str;
}
bool check(long long a){
    string in=numToStr(a);
    string b="";
    for(int i=in.length()-1;i>=0;i--){
        b+=in[i];
    }
    if(in==b)return true;
    return false;
}
int main(){
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        long long a,b;
        cin>>a>>b;
        long long ans=0;
        long long s=sqrt(a);
        if(s*s<a)s++;
        for(;s*s<=b;s++){
            if(check(s)&&check(s*s)){
                ans++;
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
}
