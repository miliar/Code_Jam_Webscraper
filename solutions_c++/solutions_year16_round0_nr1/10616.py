//
//  main.cpp
//  counting_sheep
//
//  Created by Дмитрий Ткаченко on 09/04/16.
//  Copyright © 2016 Dmitry Tkachenko. All rights reserved.
//

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int calc(int x) {
    set<int> s;
    int count = 0;
    int y = x;
    
    while ((s.size() < 10) && (count < 1000)) {
        x = (count + 1) * y;
        count++;
        while (x > 0) {
            s.insert(x % 10);
            x /= 10;
        }
    }
    
    if (s.size() < 10) {
        return -1;
    }
    else {
        return count;
    }
}

int main() {
    
    //freopen("A-small-attemp0.in", "r", stdin);
    //freopen("A-small-attemp0.out", "w", stdout);
    
    vector<int> ans;
    for (int i = 0; i < 1e6 + 1; i++) {
        ans.push_back(calc(i));
    }
    
    int T, N;
    
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        cin >> N;
        if (ans[N] != -1) {
            cout << "Case #" << i + 1 << ": " << ans[N] * N << endl;
        }
        else {
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;

        }
        
    }
    
    //fclose(stdout);
    
    return 0;
}
