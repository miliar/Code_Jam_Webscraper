#include<bits/stdc++.h>

using namespace std;

#define INF 100000000
#define MAX 1050
typedef pair<int,int> ii;
typedef vector<int> vi;

int main() {
    int t;
    //freopen("A-large.in", "r", stdin);
    //freopen("saida2.txt", "w", stdout);
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        int n;
        scanf("%d", &n);
        int r = 0, total = 0, a;
        string s;
        cin >> s;
        for (int j = 0 ; j <= n; j++) {
            int a = s[j] - '0';
            if(a > 0) {
                if(total >= j) {
                    total += a;
                } else {
                    r += j -  total;
                    total = j + a;
                }
            }
        }
        printf("Case #%d: %d\n", i+1, r);
    }
    return 0;
}
