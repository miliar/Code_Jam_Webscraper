#include<bits/stdc++.h>
using namespace std;
int main(){
    int t,n,x=0;
    string s;
    cin>>t;
    while(t--){
            x++;
        cin>>n>>s;
        int i=1,sum=s[0]-'0',sol=0;
        if( n==0 ){
            cout<<"Case #"<<x<<": "<<sol<<endl;
            continue;
        }
        while(s[i]){
            if(sum<i){
                    sol += i-sum;
                    sum=i;
            }
                sum += s[i]-'0';
                i++;
        }
        cout<<"Case #"<<x<<": "<<sol<<endl;

    }
    return 0;
}
