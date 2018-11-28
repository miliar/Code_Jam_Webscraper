#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    for(int j=1;j<=t;j++){
        int smax, temp, res=0, sum=0;
        string inp;
        cin>>smax>>inp;
        for(int i=0;i<=smax;i++){
            if(inp[i]-'0' && i>sum){
                temp=i-sum;
                res+=temp;
                sum+=temp;
            }
            sum+=inp[i]-'0';
        }
        cout<<"Case #"<<j<<": "<<res<<endl;
    }
    return 0;
}
