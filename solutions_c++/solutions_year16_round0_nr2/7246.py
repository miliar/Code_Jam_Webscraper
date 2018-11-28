#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main(){
freopen("B-large.in","r",stdin);
freopen("output.txt","w",stdout);
int t;
string test;
cin>>t; int T=t;
long long int i=0,ans=0,len=0;
while(t--){
    cin>>test;
    if(test.length()==1) {
        if(test=="-") {
            ans = 1;
            cout<<"Case #"<<T-t<<": "<<ans<<endl;
            ans=0;
        } else {
            ans = 0;
            cout<<"Case #"<<T-t<<": "<<ans<<endl;
            ans=0;
        }
    }
    else if(test.length()==2){
            if(test=="++") {ans =0;}
            else if(test=="-+") {ans =1;}
            else if(test=="+-") {ans =2;}
            else if(test=="--") {ans =1;}
            cout<<"Case #"<<T-t<<": "<<ans<<endl;
                ans=0;
    }
    else
{
    long long int a[test.length()], even[test.length()];
    if(test[test.length()-1] == '-') {
        a[test.length()-1] = 1;
        even[test.length()-2] = 0;
    } else {
        a[test.length()-1] = 0;
        even[test.length()-2] = 1;
    }

    for(i=test.length()-2;i>0;i--){
        if((even[i]==1&&test[i]=='+')||(even[i]==0&&test[i]=='-')) {
            a[i]=0; even[i-1] = even[i];
        } else if ((even[i]==1&&test[i]=='-')||(even[i]==0&&test[i]=='+')) {
            a[i]=1; even[i-1] = 1 - even[i];
        }
    }

    if((even[0]==1&&test[0]=='+')||(even[0]==0&&test[0]=='-')) {
        a[0] = 0;
    } else if ((even[0]==1&&test[0]=='-')||(even[0]==0&&test[0]=='+')){
        a[0] = 1;
    }

    for(i=0;i<test.length();i++){
        if(a[i]==1) {
            ans = ans+1;
        }
    }
    cout<<"Case #"<<T-t<<": "<<ans<<endl;
    ans=0;
}

}
return 0;
}
