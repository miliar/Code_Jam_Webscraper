#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long int64;
typedef pair<int, int> ii;
#define MAX 110 //bit size

int pancakes[110];


void flip(int k){
    for ( int i = 0; i <= k; i++ ){
        pancakes[i] ^= 1;
    }
}

int main(){
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    for ( int k = 1; k <= t; k++ ){
        cout << "CASE #" << k << ": ";
        string pan;
        cin >> pan;
        int n = pan.size(), count = 0;
        int resp = 0;
        for ( int i = 0; i < n; i++ ){
            if ( pan[i] == '+' ) count++;
            pancakes[i] = (pan[i] == '+');
        }
        if ( count == n ) cout << 0 << endl;
        else{
            for ( int i = n-1; i >= 0; i-- ){
                if ( pancakes[i] ) continue;
                flip(i);
                resp++;
            }
            cout << resp << endl;
        }
    }
    return 0;
}