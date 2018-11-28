#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstdio>
using namespace std;

int dobar(long long unsigned a,FILE *f){
    char b;
    fseek(f, a, SEEK_SET);
    fread(&b,1,1,f);
    return b>'0';
}


int main(){
    int t;
    FILE *f=fopen("data.bin","rb");
    cin>>t;
    for (int tt=1; tt<t+1; ++tt){
        unsigned long long r=0,a,b;
        cin>>a>>b;
        for (long long unsigned i=a; i<=b; ++i){
            r+=dobar(i,f);
        }
        cout<<"Case #"<<tt<<": "<<r<<endl;
    }
    return 0;
}
