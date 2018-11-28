#include<iostream>
using namespace std;

typedef unsigned long long ull;

ull solve(ull A,ull B,ull K){
    ull ans=0;
    for(ull a=0;a<A;a++){
        for(ull b=0;b<B;b++){
            ans += ((a&b) < K);
        }
    }
    return ans;
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        ull A,B,K;
        cin >> A >> B >> K;

        cout << "Case #" << t << ": " << solve(A,B,K) << endl;
    }

    return 0;
}
