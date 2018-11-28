#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>

#include <thread>
#include <chrono>

#include <memory>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/stat.h>
#include <time.h>
#include <errno.h>
#include <Semaphore.h>

using namespace std;

int main() {
    freopen("/Users/lujcmss/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int kase = 0; kase < T; kase++) {
        string s;
        cin >> s;
        
        int len = (int)s.length();
        for (int i = 0; i < len; i++) {
            if (s[i] == '+') {
                s[i] = 1;
            } else {
                s[i] = 0;
            }
        }

        int ans = 0;
        while (true) {
            int left = 0, right = len;
            while (right > 0 && s[right-1] == 1) {
                right--;
            }
            if (right == 0) {
                break;
            }
            if (s[0] == 0) {
                string tmp = s;
                for (int i = 0; i < right; i++) {
                    s[i] = tmp[right - 1 - i] ^ 1;
                }
                ans++;
            } else {
                while (s[left] == 1) {
                    s[left] = 0;
                    left++;
                }
                ans++;
            }
        }
        
        printf("Case #%d: %d\n", kase+1, ans);
    }
    
    return 0;
}