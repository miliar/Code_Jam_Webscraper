#include <bits/stdc++.h>
using namespace std;

int t,slvl;
char k;
string s;

void start(){
    for(int i=0;i<t;i++){
        cin>>slvl; cout<<"Case #"<<i+1<<": ";
        int pearson=0;
        int ans=0;
        for(int i=0;i<=slvl;i++){
            cin>>k; int tempo=k-'0';
            //cout<<slvl<<" "<<k<<" "<<tempo<<" "<<pearson<<" "<<ans<<endl;
            if(pearson<i && tempo>0){
                
                
                ans+=i-pearson;
                pearson+=i-pearson;
            }
            pearson+=tempo;
            
        }
        cout<<ans<<endl;
    }
}


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    while(cin>>t){
        start();
    }
    return 0;
}