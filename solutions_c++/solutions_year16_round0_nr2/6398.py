#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("P2.out","w",stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        string S;
        cin >> S;
        int C = 0;
        S +="+";
        for (int i = S.size()-1; i > 0; i--){
            C += S[i] != S[i-1];
        }
        printf ("Case #%d: %d\n",t,C);
    }
	return 0;
}

