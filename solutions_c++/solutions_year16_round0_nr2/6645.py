#include <bits/stdc++.h>

using namespace std;

int main(){
    freopen("B-large.in","r", stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    for(int caso=1;caso<=T;caso++){
        string S;
        cin>>S;
        int n=0, ind=0;
        char ant;
        while(ind<S.size()){
            ant=S[ind];
            while(ind<S.size()&&S[ind]==ant) ind++;
            n++;
        }
        int res;
        if(n%2==0){
            if(S[0]=='-'){
                res=n-1;
            } else {
                res=n;
            }
        } else {
            if(S[0]=='-'){
                res=n;
            } else {
                res=n-1;
            }
        }
        cout<<"Case #"<<caso<<": "<<res<<endl;
    }
    return 0;
}
