#include <bits/stdc++.h>
using namespace std;

int test;

long long pr(int I,int K,int C){
    if (C==0) return I;
    return I*K+pr(I,K,C-1);
}

void sol(){
    test++;
    int K,C,S;
    cin>>K>>C>>S;
    cout<<"Case #"<<test<<":";
    for (int i=0;i<K;i++)
    cout<<" "<<pr(i,K,C-1)+1;
    cout<<endl;
}

int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D0.txt","w",stdout);
    int t;
    cin>>t;
    while (t--){
        sol();
    }
    return 0;
}
