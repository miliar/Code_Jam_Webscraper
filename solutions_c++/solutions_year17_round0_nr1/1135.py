#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int cases, caseno = 0;
    scanf("%d", &cases);
    while(cases--){
        string str;
        int k;
        cin >> str;
        scanf("%d", &k);
        int cnt = 0;
        for(int i=0; i<=str.length()-k; i++){
            if(str[i] == '-'){
                cnt++;
                for(int j=i;j<(i+k);j++){
                    if(str[j] == '-') str[j] = '+';
                    else if(str[j] == '+') str[j] = '-';
                }
            }
        }
        for(int i=str.length()-1; i>=(k-1); i--){
            if(str[i] == '-'){
                cnt++;
                for(int j=i; j>(i-k); j--){
                    if(str[j] == '-') str[j] = '+';
                    else if(str[j] == '+') str[j] = '-';
                }
            }
        }
        int flag = 0;
        for(int i=0; i<str.length(); i++){
            if(str[i] == '-') flag = 1;
        }
        if(flag == 1) cout << "Case #" << ++caseno << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << ++caseno << ": " << cnt << endl;
    }
}
