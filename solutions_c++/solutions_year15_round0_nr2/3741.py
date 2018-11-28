#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<fstream>

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int icase=0;
    while(T--){
        icase++;
        int n;
        cin>>n;
        int a[1005];
        int maxx=0;
        for(int i=0;i<n;i++){
            cin>>a[i];
            if(a[i]>maxx) maxx=a[i];
        }
        int res=0;
        int minres=1005;
        for(int i=1;i<=maxx;i++){
            res=0;
            for(int j=0;j<n;j++){
                res+=(a[j]-1)/i;
            }
            res+=i;
            if(res<minres) minres=res;
        }
        cout<<"Case #"<<icase<<": "<<minres<<endl;
    }
    return 0;
}
