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
        int K,C,S;
        cin>>K>>C>>S;

        cout<<"Case #"<<i+1<<": ";
        unsigned long long int sum=0,sq=1;
        for(int j=0;j<C;j++){
            sum+=sq;
            sq*=K;
        }

        cout<<1;
        unsigned long long int ans=1+sum;
        for(int j=0;j<K-1;j++){
            cout<<" "<<ans;
            ans+=sum;
        }
        cout<<endl;
    }

    return 0;
}
