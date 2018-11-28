#include <bits/stdc++.h>
using namespace std;

int n , a , b , c;

void work() {
    cin >> n >> b >> a >> c;
    string A = "P" , B = "R" , C = "S";
    for (int i = 0 ; i < n ; ++ i) {
        string aa , bb , cc;
        aa = min(A + B , B + A);
        bb = min(B + C , C + B);
        cc = min(C + A , A + C);
        A = aa , B = bb , C = cc;
    }
    string S[3] = {A , B , C};
    sort(S , S + 3);
    for (int i = 0 ; i < 3 ; ++ i) {
        int AA = 0 , BB = 0 , CC = 0;
        for (int j = 0 ; j < S[i].size() ; ++ j) {
            if (S[i][j] == 'P') ++ AA;
            if (S[i][j] == 'R') ++ BB;
            if (S[i][j] == 'S') ++ CC;
        }
        if (AA == a && BB == b && CC == c) {
            puts(S[i].c_str());
            return;
        }
    }
    puts("IMPOSSIBLE");
}

int main() {
    int ca = 0 , T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
