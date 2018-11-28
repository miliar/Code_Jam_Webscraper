#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <deque>

using namespace std;

int main (){
    freopen("a.in","r", stdin);
    freopen("a.out","w", stdout);
    
    int T;
    cin >> T;
    
    for (int cas = 1; cas <= T; ++cas){
        long long n;
        cin >> n;
        long long e = n;
        cout <<"Case #"<< cas <<": "; 
        if (0 == n) {
            puts("INSOMNIA");
            continue;
        }

        int res = 0, cnt = 0;
        vector < bool > have(10, false);
        while (cnt != 10){
           long long tmp = n; 
            while (tmp){ 
                if (!have[tmp%10]){
                    ++cnt;
                    have[tmp%10] = true;
                }
                tmp /= 10;
            }
            n += e;
            ++res;
        }
        cout << res * e << endl; 
    }
    return 0;
}



