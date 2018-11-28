//
//  main.cpp
//  A
//
//  Created by LegaDyan on 16/4/9.
//  Copyright © 2016年 LegaDyan. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[]) {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        bool vis[10];
        memset(vis, 0, sizeof(vis));
        int time = 0;
        int sum = a;
        int times = 0;
        while (1) {
            times++;
            if (times > 1000000) break;
            char s[1000];
            sprintf(s, "%d", sum);
            int len = strlen(s);
            for (int j = 0; j < len; j++) {
                if (!vis[s[j] - '0']) vis[s[j] - '0'] = 1, time++;
            }
            if (time == 10) break;
            else sum += a;
        }
        if (times > 1000000) cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        else cout << "Case #" << i + 1 << ": " << sum << endl;
    }
    return 0;
}
