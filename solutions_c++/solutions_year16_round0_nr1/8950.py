//
//  main.cpp
//  cj2016_qr1
//
//  Created by DongJiaming on 4/9/16.
//  Copyright © 2016 NYU. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    
    freopen("/Users/JiamingDong/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/JiamingDOng/Documents/cj2016/qr/A-large.out", "w", stdout);
    
    int n;
    cin >> n;
    for (int tt = 0; tt < n; tt++) {
        int x;
        cin >> x;
        bool visit[10];
        for (int i = 0; i < 10; i++) {
            visit[i] = false;
        }
        int total_visit = 0;
        if (x == 0) {
            total_visit = 10;
        }
        int step = x;
        while (total_visit < 10) {
            //cout << x << " " << total_visit << endl;
            int tmp = 0;
            int tmp_x = x;
            while (tmp_x > 0) {
                tmp = tmp_x % 10;
                tmp_x /= 10;
                if (!visit[tmp]) {
                    total_visit++;
                    visit[tmp] = true;
                }
            }
            if (total_visit < 10) {
                x += step;
            }
        }
        cout << "Case #" << tt + 1 << ": ";
        if (x == 0) {
            cout << "INSOMNIA";
        } else {
            cout << x;
        }
        cout << endl;
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
