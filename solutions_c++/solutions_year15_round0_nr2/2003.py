#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include<cstdio>
#include<cmath>
#include <queue>

using namespace std;



int main() {
    int TC;
    int casenum = 1;
    cin >> TC;
    while(TC--){
        int D;
        cin >> D;
        int tmp;
        vector<int> v;
        for(int i = 0; i < D; i++){
            cin >> tmp;
            v.push_back(tmp);
        }
        int m = 1<<30;
        for(int h = 1; h <= 1000; h++) {
            int cur_m = 0;
            for(int i = 0; i < D; i++){
                if(v[i]%h == 0) cur_m += (v[i]/h)-1;
                else cur_m += (v[i]/h);
            }
            m = min(m, cur_m+h);
        }
        cout << "Case #" << casenum++ << ": " << m << endl;
    }
    
}
