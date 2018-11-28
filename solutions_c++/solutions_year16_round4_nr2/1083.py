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

double p[210];
double allyes[65540], allno[65540];

vector<int> v;
vector<int> v1;

int main() {
    freopen("/Users/lujcmss/Downloads/B-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/b-out.txt", "w", stdout);
    
    int T;
    cin >> T;
    
    for (int kase = 0; kase < T; kase++) {
        int n, k;
        cin >> n >> k;
        
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        
        
        
        double ret = 0;
        for (int comb = 1; comb < (1 << n); comb++) {
            int tmp = comb;
            int idx = 0;
            double ally = 1;
            double alln = 1;
            while (tmp > 0) {
                if (tmp&1) {
                    ally *= p[idx];
                    alln *= (1 - p[idx]);
                }
                tmp /= 2;
                idx++;
            }
            allyes[comb] = ally;
            allno[comb] = alln;
        }
        
        for (int comb = 3; comb < (1 << n); comb++) {
            v.clear();
            int tmp = comb;
            int idx = 0;
            while (tmp > 0) {
                if (tmp&1) {
                    v.push_back(idx);
                }
                tmp /= 2;
                idx++;
            }
            if (v.size() != k) {
                continue;
            }
            
            double even = 0;
            for (int i = 1; i < (1 << v.size()); i++) {
                v1.clear();
                int tmp1 = i;
                int idx1 = 0;
                
                while (tmp1 > 0) {
                    if (tmp1&1) {
                        v1.push_back(v[idx1]);
                    }
                    tmp1 /= 2;
                    idx1++;
                }
                if (v1.size() != v.size() / 2) {
                    continue;
                }
                
                int ally = 0;
                for (int j = 0; j < v1.size(); j++) {
                    ally += (1 << v1[j]);
                }
                int alln = comb - ally;
                
                even += allyes[ally] * allno[alln];
            }
            
            ret = max(ret, even);
        }
        
        printf("Case #%d: %f\n", kase + 1, ret);
    }
    return 0;
}