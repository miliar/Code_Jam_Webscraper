#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        long long k,c,s;
        cin>>k>>c>>s;
        if(s<((k+1)/2) or (s<k and c==1)){
            cout<<"IMPOSSIBLE\n";
            continue;
        }
        if(c==1){
            for(int i=0;i<k;i++){
                cout<<i+1<<" ";
            }
            cout<<endl;
            continue;
        }
        long long tmp=k,ans=0;
        for(int i=1;i<c;i++){
            ans+=tmp;
            tmp*=k;
        }
        for(int i=1;i<=k;i+=2){
            if(i!=k){
                cout<<(i-1)*ans+(i+1)<<" ";
            }
            else{
                cout<<(i-1)*ans+(i)<<" ";
            }
        }
        cout<<endl;
    }
}
