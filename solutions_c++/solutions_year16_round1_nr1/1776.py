#include<cstdio>
#include<iostream>
#include<string>

using namespace std;

int t, casei;

int main() {
    casei = 0;
    scanf("%d", &t);
    while(t--) {
        char s[1002];
        scanf("%s", s);
        int i = 1;
        string res;
        res.push_back(s[0]);
        while(s[i] != '\0') {
            if(s[i] >= res[0])
                res.insert(res.begin(), s[i]);
            else
                res.push_back(s[i]);
            ++i;
        }
        cout << "case #" << ++casei << ": " << res << "\n";
    }
    return 0;
}
