#include <bits/stdc++.h>
using namespace std;

int T;


int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas<=T; cas++){
        printf("Case #%d: ", cas);

        string s;
        cin >> s;
        int c = 0;
        for(int i = 0; i<s.length(); i++){
            if (s[i] == '-'){
                if (i == 0) c++;
                else if (s[i-1] == '+') c+=2;
            }
        }

        printf("%d\n", c);

    }





}
