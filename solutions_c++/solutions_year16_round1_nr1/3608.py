#include<iostream>
#include<cstring>
#include<stdio.h>
using namespace std;
int main(){
    int t,i,j=1;
    string s,res;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    while(j<=t){
        cin>>s;
        i=1;
        res=s[0];
        while(i<s.size()){
            if((int)s[i]>=res[0]){
                res=s[i]+res;
            }
            else
                res=res+s[i];
            i++;
        }
        cout<<"Case #"<<j<<": "<<res<<endl;
        j++;
    }
    return 0;
}
