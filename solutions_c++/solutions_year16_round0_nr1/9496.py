#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

long long brute(long long x) {
    if (x == 0) {
        return -1;
    }
    
    bool seen[10] = {0,};
    for (int i = 1; i <= 1000; ++i) {
        long long t = x * i;
        
        while(t > 0) {
            seen[t%10] = true;
            t /= 10;
        }        
        
        for (int z = 0; z < 10; ++z) {
            if (!seen[z]) break;
            if (z == 9) {
                return x * i;
            }
        }
    }
    
    return -1;
}

int main(int argc, char **argv) {
    
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int t; cin >> t;
    
    for (int test = 1; test <= t; ++test) {
        
        int x;
        cin >> x;
        
        long long ans = brute(x);
        
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d: ", test);

        if (ans == -1) {
            cout << "INSOMNIA";
            cerr << "INSOMNIA";
        } else {
            cout << ans;
            cerr << ans;
        }
        cout << endl;
        cerr << endl;
    }
        
	return 0;
}
