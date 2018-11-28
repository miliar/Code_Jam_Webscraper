#include<iostream>
#include<cstring>
using namespace std;

char q[2500];
char s[1100];
int main() {
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas++) {
        cin >> s;
        int a, b;
        a = b = 1100;
        q[--a] = s[0];
        for(int i = 1; i < strlen(s); i++) {
            if(q[a] <= s[i]) q[--a] = s[i];
            else q[b++] = s[i];
        }
        cout << "Case #" << cas << ": ";
        for(int i = a; i < b; i++) cout << q[i];
        cout << "\n";
    }
}
