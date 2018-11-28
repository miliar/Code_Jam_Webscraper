#include<bits/stdc++.h>

using namespace std;

int Solve(int n, string str){
    //cout << str << endl;
    int add=0, hand=str[0]-'0';
    for(int i=1; i<n+1; i++){
        if(hand<i){
            add += i-hand;
            hand = i;
        }

        hand += str[i]-'0';
    }

    return add;
}

int main(){
    freopen("Ain.txt", "r", stdin);
    freopen("Alarge.out", "w", stdout);

    int T, n, t=0;
    string str;
    cin >> T;

    while(T--){
        cin >> n >> str;

        cout << "Case #" << ++t << ": " << Solve(n, str) << endl;
    }




    return 0;
}
