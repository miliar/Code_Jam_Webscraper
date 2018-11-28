#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
    int t,tc=0,shymax;cin>>t;
    string s;
    while(t--){
        cin>>shymax>>s;
        int sum=s[0]-'0',sol=0;
        for(int i=1;i<s.size();i++){
            if(sum<i){
                sol += i-sum;
                sum += i-sum+(s[i]-'0');
            }else{
                sum+= s[i]-'0';
            }
        }
        cout<<"Case #"<<++tc<<": "<<sol<<endl;
    }
}
