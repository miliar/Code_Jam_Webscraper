#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main() {
    int T, N;
    char str[1001];
    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%s", str);
        int l = strlen(str);
        string s;
        s.push_back(str[0]);
        for (int i = 1; i < l; i++) {
            if(str[i] >= s.front()) {
                s.insert(0, 1, str[i]);
            }else {
                s.push_back(str[i]);
            }
        }
        printf("Case #%d: ", i + 1);
        cout << s << "\n";
    }
}