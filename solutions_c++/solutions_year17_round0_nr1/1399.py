#include<bits/stdc++.h>
using namespace std;
void swtch(char *c){
    *c = (*c=='+')? '-' : '+';
}
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;cin>>tc;
    for(int t=1;t<=tc;t++){
        int x;
        string in;cin>>in>>x;
        int ans = 0;
        for(int i=0;i+x<=in.size();i++){
            if(in[i]=='-'){
                    ans++;
                for(int k=0;k<x;k++){
                    swtch(&in[k+i]);
                }

            }
        }
        bool ok = 1;
        for(auto i:in)
        if(i=='-'){
            ok=0;
            break;
        }
        cout<<"Case #"<<t<<": ";
        if(ok)cout<<ans<<endl;
        else cout <<"IMPOSSIBLE"<<endl;

    }
}
