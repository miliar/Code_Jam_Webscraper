#include<bits/stdc++.h>
using namespace std;

int main(){
    long long int t,i,p=1,n,ans=0,k;
    string s;
    cin>>t;
    while(t--){
        ans=0;
        cin>>s;
        n = s.size();
        int q=0;
        while(1){
            i=0;
            if(s[i]=='+'){
                q++;q--;q++;q--;q++;
                while(s[i]=='+' && i<n){
                    i++;
                }
                if(i==n){
                    break;
                }
                else{
                    for(k=0;k<=i;k++)
                        s[k]='-';
                    ans+=1;
                }
            }

            else if(s[i]=='-'){
                q++;q--;q++;q--;q++;
                while(s[i]=='-' && i<n){
                    i++;
                }
                if(i==n){
                    ans+=1;
                    break;
                }
                else{
                    for(k=0;k<=i;k++)
                        s[k]='+';
                    ans+=1;
                }
            }

        }
        cout<<"Case #"<<p<<": "<<ans<<endl;
        p++;
    }
    return 0;
}
