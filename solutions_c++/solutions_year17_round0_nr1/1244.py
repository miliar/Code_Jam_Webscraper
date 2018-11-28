#include<bits/stdc++.h>
using namespace std;

int main(){
    int i,j,k,n,x,y,z,t,T;
    string str;

    cin>>T;
    t=1;
    while(t<=T){
        cin>>str;
        cin>>k;

        i=0;
        x=0;
        n=str.length();

        while(i<n && str[i]=='+'){
            i++;
        }

        while(i+k<=n){
            //flip k characters
            x++;
            j=0;
            while(j<k){
                if(str[i+j]=='+'){
                    str[i+j]='-';
                } else {
                    str[i+j]='+';
                }

                j++;
            }

            while(i<n && str[i]=='+'){
                i++;
            }
        }
        
        cout<<"Case #"<<t<<": ";
        if(i==n){
            cout<<x;
        } else {
            cout<<"IMPOSSIBLE";
        }
        cout<<endl;

        t++;
    }

    return 0;
}
