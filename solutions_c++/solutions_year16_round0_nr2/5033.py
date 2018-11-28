#include<iostream>
#include<algorithm>
#include<string.h>
#include<cstdio>

using namespace std;

int main(){

    freopen("gcj2_input.txt","r",stdin);
    freopen("gcj2_output.txt","w",stdout);


    int t,k;
    cin>>t;
    for(k=1;k<=t;k++){
        string s;
        cin>>s;
        long long len,i,ans=0,j,cnt=0,found=0;
        len=s.length();
        for(i=len-1;i>=0;i--){
            if(s[i]=='+')continue;
            for(j=0;j<=i;j++){
                if(s[j]=='-')break;
                else {
                    cnt++;
                    s[j]='-';
                }
            }
            if(cnt>0)ans++;
            for(j=0;j<(i+1)/2;j++){
                found=1;
                swap(s[j],s[i-j]);
                if(s[j]=='+')s[j]='-';
                else s[j]='+';
                if(s[i-j]=='+')s[i-j]='-';
                else s[i-j]='+';
            }
            if((i+1)%2!=0){
                if(s[j]=='+')s[j]='-';
                else s[j]='+';
            }
            ans++;
            cnt=0;
        }
        cout<<"Case #"<<k<<": ";
        cout<<ans<<"\n";
    }
    return 0;





}
