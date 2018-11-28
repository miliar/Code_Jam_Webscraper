#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++){
        int n,c=0;
        ll i=1,num,ans;
        cin>>n;
        vector<bool> dig(10,false);
        if(n==0){
            cout<<"Case #"<<j<<": INSOMNIA\n";
            continue;
        }
        while(c<10){
            num=i*n;
            ans=num;
            while(num>0){
                if(!dig[num%10]){
                    c++;
                    dig[num%10]=true;
                }
                num/=10;
            }
            i++;
        }
        cout<<"Case #"<<j<<": "<<ans<<"\n";
    }
}
