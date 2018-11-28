#include <bits/stdc++.h>
using namespace std;
int digits[10];
void getdigits(int n){
    int b=n,c;
    while(b!=0){
        c=b%10;
        b/=10;
        digits[c]+=1;
    }
}

int main(){
    int n,i,t,a[1002],flag,p,j,ans;
    cin>>t;
    p=1;
    while(t--){
        cin>>n;
        for(i=0;i<10;i++)
            digits[i]=0;
        for(i=1;i<=1001;i++)
            a[i]=n*i;
        for(i=0;i<1002;i++){
            getdigits(a[i]);
            for(j=0;j<10;j++){
                if(digits[j]>0){
                    flag=0;
                }
                else{
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                ans=a[i];
                break;
            }
        }
        if(flag==0){
            cout<<"Case #"<<p<<": "<<ans<<endl;
        }
        else{
            cout<<"Case #"<<p<<": "<<"INSOMNIA"<<endl;
        }
        p++;
    }
    return 0;
}
