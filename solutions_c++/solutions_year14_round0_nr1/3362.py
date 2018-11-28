#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int t,r,a[5][5],l,val2,idx;
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for ( int l = 1; l <= t; l++ ) {
        cin >> r;
        int cnt[18];
        memset(cnt, 0, sizeof(cnt));
        for ( int i = 1; i <= 4; i++ ) {
            for ( int j = 1; j <= 4; j++ ) cin >> a[i][j];
        }
        for ( int j = 1; j <= 4; j++ ) cnt[a[r][j]]++;
        cin >> r;
        for ( int i = 1; i <= 4; i++ ) {
            for ( int j = 1; j <= 4; j++ ) cin >> a[i][j];
        }
        for ( int j = 1; j <= 4; j++ ) cnt[a[r][j]]++;
        idx = -1;
        val2 = 0;
        for ( int i = 1; i <= 16; i++ ) {
            if ( cnt[i] == 2 ) {
                 val2++;
                 idx = i;
            }
        }
        cout << "Case #" << l << ": ";
        if ( val2 == 1 ) cout << idx << endl;
        else if ( val2 == 0 ) cout << "Volunteer cheated!" << endl;
        else cout << "Bad magician!" << endl;
    }
    return 0;
}
