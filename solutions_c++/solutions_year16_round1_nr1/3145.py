#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e5+10;
char s[1005];
char t[4005];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, ca = 1;
    scanf("%d", &T);
    while(T--){
        scanf("%s", s);
        memset(t, 0, sizeof(t));
        int l = 1005, r = 1005;
        t[--l] = s[0];
        for(int i = 1; s[i]; i++){
            if(s[i] > t[l])
                t[--l] = s[i];
            else if(s[i] < t[l])
                t[r++] = s[i];
            else {
                int tag = 0;
                for(int j = l+1; j < r&&tag != 0; j++)
                    tag = t[j]-t[j-1];
                if(tag == 1)
                    t[r++] = s[i];
                else t[--l] = s[i];
            }
        }
        printf("Case #%d: %s\n", ca++, t+l);
    }
	return 0;
}

