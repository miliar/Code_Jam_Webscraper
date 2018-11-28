#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

FILE *fin  = fopen("b.in",  "r");
FILE *fout = fopen("b.out", "w");

char temp[105];
int main() {
    int n; fscanf(fin, "%d", &n);
    for(int t = 1; t <= n; t++) {
        fscanf(fin, "%s", temp);
        string s = temp;
        int ans = 0;
        bool cur = (s[0] == '+');
        for(int i = 1; i < s.size(); i++) {
            if(s[i-1] != s[i]) {
                ans++;
                cur ^= 1;
            }
        }
        if(!cur) ans++;
        fprintf(fout, "Case #%d: %d\n", t, ans);
    }
    return 0;
}
