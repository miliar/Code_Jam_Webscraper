#include <iostream>
#include <bits/stdc++.h>
#include <set>
using namespace std;

set<int> digits;

void get_digits(unsigned long long N){
    while(N>0){
        digits.insert(N%10);
        N /= 10;
    }
}

int main(){
    freopen("A-large.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OutputA.txt", "w", stdout);
    int T;
    unsigned long long N,ans;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>N;
        if(!N)
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else{
            int m = 1;
            ans = N;
            while(digits.size()<10){
                ans = m*N;
                get_digits(ans);
                m++;
            }
            cout<<"Case #"<<i<<": "<<ans<<endl;
        }
        digits.clear();
    }
    return 0;
}
