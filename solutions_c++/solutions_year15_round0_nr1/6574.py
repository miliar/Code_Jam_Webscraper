#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);

    for( int cs = 1; cs <= t; ++cs ) {
        int n;
        string str;

        cin >> n >> str;

        int cnt = 0, pre = str[0]-'0';

        for( int i = 1; i <= n; ++i ) {
            int curr = str[i]-'0';
            if( i <= pre ) {
                pre += curr;
            }
            else {
                if( !curr ) continue;
                cnt += (i-pre);
                pre += (i-pre)+curr;
            }
        }

        printf("Case #%d: %d\n", cs, cnt);
    }
}

