#include<iostream>
#include<fstream>
#include<cmath>
#include<cstdlib>
#include<cstring>
using namespace std;
int pow10(int x){
    if(x==0)return 1;
    int a=10;
    for(int i=1;i<x;++i)
        a*=10;
    return a;
}
bool isp(int x){
    char a[20];
    itoa(x,a,10);
    int t=strlen(a);
    for(int i=0;i<t/2;++i)
        if(a[i]!=a[t-i-1])
            return 0;
    return 1;
}

int main()
{
    int T;
    double Ain,Bin;
    int a,b;
    int result;
    ifstream tin("inC");
    ofstream tout("outC");
    tin>>T;
    for(int count=1;count<=T;++count){
        result=0;
        tin>>Ain>>Bin;
        a=(int)sqrt(Ain);
        if(sqrt(Ain)!=a)++a;
        b=(int)sqrt(Bin);
        for(int i=a;i<=b;++i){
            if(isp(i)&&isp(i*i)){
                ++result;
            }
        }
        tout<<"Case #"<<count<<": "<<result<<endl;
    }
    return 0;
}
