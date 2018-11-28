#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
#include<stdlib.h>
using namespace std;
int main(){
long long int t,c,i,j,k,l,m=0,s=0,n;
long long int a,b;
cin>>t;
while(t--){
    m++;
    cin>>a>>b>>k;
    cout<<"Case #"<<m<<": ";
    int s=0;
    for(i=0;i<a;i++){
        for(j=0;j<b;j++){
            long long int x=i&j;
            //cout<<i<<' '<<j<<' '<<x<<'\t';
            if(x<k)
                s++;
        }
    }
    cout<<s<<'\n';
}

return 0;}

