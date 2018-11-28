//
//  main.cpp
//  FractilesGCJ
//
//  Created by 莫润昌 on 16/4/9.
//  Copyright © 2016年 莫润昌. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, const char * argv[]) {
    int t, k, c, s, i;
    ios::sync_with_stdio(false);
    freopen("D-small-attempt0.in","r",stdin);
    freopen("a.txt","w",stdout);
    cin >> t;
    i = 1;
    while (i <= t) {
        cin >> k >> c >> s;
        cout << "Case #" << i << ": ";
        for (int j = 1; j <= s; j++) {
            cout << j;
            if (j != s)
                cout << " ";
        }
        cout << endl;
        i++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
