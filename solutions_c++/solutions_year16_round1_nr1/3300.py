#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include<cstring>
using namespace std;
#define rep(i,n) for(int i = 0; i < n; ++i)
#define pii pair<int,int>

int main(){
    int M;
    cin>>M;
    rep(i,M){
        string S;
        cin>>S;
        string ans;

        rep(j,S.size()){
            if(S[j]+ans>ans+S[j]){
                ans=S[j]+ans;
            }
            else{
                ans.push_back(S[j]);
            }
        }

        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }

    return 0;
}
