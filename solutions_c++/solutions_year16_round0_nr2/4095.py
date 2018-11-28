#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
using namespace std;
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("Out.out", "w", stdout);
    int tt, cont;
    int p;
    string s;
    cin >> tt;
    for(int c = 0; c < tt; c++) {
        cont = 0;
        cout << "Case #" << c + 1 << ": ";
        cin >> s;
        for(int i = s.size() - 1; i >= 0; i--){
            if(s[i] == '-'){
                if(s[0] == '+'){
                    p = 0;
                    while(s[p] == '+'){
                        p++;
                    }
                    for(int j = 0; j < p; j++){
                        s[j] = '-';
                    }
                    cont++;
                }
                cont++;
                reverse(s.begin(), s.begin() + i + 1);
                for(int j = 0; j < s.size(); j++) {
                    s[j] = (s[j] == '-') ? '+' : '-';
                }
            }
        }
        cout << cont << endl;
    }
    return 0;
}
