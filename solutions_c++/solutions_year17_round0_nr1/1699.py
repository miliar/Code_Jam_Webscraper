#include <stdio.h>
#include <iostream>

using namespace std;

int main(){

    int T;

    cin >> T;

    for (int t = 1 ; t<= T ; t++){
        string S;
        cin >> S;
        int K;
        cin >> K;

        printf("Case #%d: ",t);

        //printf("%s %d %d\n",S.c_str(),K,S.length());


        int l = S.length();
        bool H[1001];
        for (int i = 0 ; i <l ; i++){

            H[i] = S[i] == '+';
        }

        int ans = 0;
        for (int i = 0 ;i  <= l-K; i++){
            if (!H[i]) {
                for (int j = i ; j < i+K; j++){
                    H[j] = !H[j];
                }
                ans++;
            }

        }

        for (int i = l-K+1;  i < l ; i++){

            if (!H[i]) {
                ans = -1;
                break;
            }
        }


        if (ans == -1) {
            printf("IMPOSSIBLE\n");

        } else {
            printf("%d\n",ans);
        }
    }


}
