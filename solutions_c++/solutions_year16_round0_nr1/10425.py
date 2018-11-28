#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

int T, n;
map <int , int> m;
int mark, x;

int main() {
    freopen("a.in", "r", stdin);
    freopen("b.in", "w", stdout);
    cin >> T;
    while(T--){
        x++;
        cin >> n;
        if(n == 0){
            cout << "Case #" << x << ": " << "INSOMNIA" << endl;
            continue;
        }
        int i = 0;
        for(int i = 0; i <= 9; ++i){
            m[i] = 0;
        }
        mark = 1;
        while(mark){
            i++;
            int nn = n * i;
            while(nn != 0){
                m[nn % 10] =1;
                nn /= 10;
            }
            mark = 0;
            for(int i = 0; i <= 9; ++i){
                if(m[i] == 0) mark = 1;
            }
        }
        cout << "Case #" << x << ": " << n * i << endl;
    }

    return 0;
}