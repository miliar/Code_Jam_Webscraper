#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int t, kejs, i, n, r, s, p, N;
string best;

bool ok(string str) {
        while (str.size() > 1) {
                string n = "";
                for (int i = 0; i < (int) str.size(); i+=2) {
                        if (str[i]==str[i+1]) return false;
                        if (str[i]=='R' && str[i+1]=='S') n += 'R';
                        if (str[i]=='S' && str[i+1]=='R') n += 'R';
                        if (str[i]=='R' && str[i+1]=='P') n += 'P';
                        if (str[i]=='P' && str[i+1]=='R') n += 'P';
                        if (str[i]=='P' && str[i+1]=='S') n += 'S';
                        if (str[i]=='S' && str[i+1]=='P') n += 'S';
                }
                str = n;
        }
        return true;
}

int main() {
        scanf("%d", &t);

        for (kejs = 1; kejs <= t; kejs++) {
                                                                printf("Case #%d: ", kejs);
                scanf("%d%d%d%d",&n, &r, &p, &s);
                N = 1 << n;
                                                                best = "Z";
                                                                string str = "";
                                                                for (i = 0; i < p; i++) str += 'P';
                                                                for (i = 0; i < r; i++) str += 'R';
                                                                for (i = 0; i < s; i++) str += 'S';
                                                                do {
                                                                        if(ok(str) && best > str) best = str;
                                                                } while(next_permutation(str.begin(), str.end()));
                                                                if (best == "Z") printf("IMPOSSIBLE\n");
                                                                else printf("%s\n", best.c_str());
        }
        return 0;
}
