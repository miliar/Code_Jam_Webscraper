#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<utility>
#include<string>

using namespace std;

int solve() {
    int s;
    cin >> s;

    int counter = 0;
    int friends = 0;

    char c;
    scanf("%c", &c);

    for(int i=0; i<=s; i++) {

        scanf("%c", &c);
        int d = c - '0';
//        printf("%d\n", d);

        if(i > counter) {
            friends += i-counter;
            counter = i;
        }
        counter += d;
    }

    return friends;
}

int main() {
    freopen("Ain.txt", "r", stdin);
    freopen("Aout.txt", "w", stdout);
    int T;
    cin >> T;

    for(int i=1; i<=T; i++) {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
