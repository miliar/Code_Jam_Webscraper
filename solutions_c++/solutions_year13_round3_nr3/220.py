#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

int d[1000], k[1000], w[1000], e[1000], s[1000], delta_d[1000], delta_p[1000], delta_s[1000];
int h[100000] = {0};
const int zero = 50000;

int main(){
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    
	int T;
	cin >> T;
    
	for (int t = 0; t < T; t++){
		int n;
        cin >> n;
        
        int cnt = 0;
        
        for (int i = 0; i < n; i++){
            cin >> d[i] >> k[i] >> w[i] >> e[i] >> s[i] >> delta_d[i] >> delta_p[i] >> delta_s[i];
            w[i] += zero;
            e[i] += zero;
        }
        
        for (int i = 0; i < 100000; i++)
            h[i] = 0;
        
        while (1){
            int mind = 1000000000;
            
            for (int i = 0; i < n; i++){
                if (k[i] > 0){
                    mind = min(d[i], mind);
                }
            }
            
            if (mind == 1000000000)
                break;
            
            for (int i = 0; i < n; i++){
                bool is = false;
                if (k[i] > 0 && d[i] == mind){
                    for (int j = w[i]; j < e[i]; j++){
                        if (h[j] < s[i])
                            is = true;
                    }
                }
                if (is)
                    cnt++;
            }
            
            for (int i = 0; i < n; i++){
                if (k[i] > 0 && d[i] == mind){
                    for (int j = w[i]; j < e[i]; j++){
                        h[j] = max(h[j], s[i]);
                    }
                    d[i] += delta_d[i];
                    s[i] += delta_s[i];
                    w[i] += delta_p[i];
                    e[i] += delta_p[i];
                    k[i]--;
                }
            }
            
            
        }
        
		cout << "Case #" << t + 1 << ": ";
        cout << cnt << endl;
	}
}
