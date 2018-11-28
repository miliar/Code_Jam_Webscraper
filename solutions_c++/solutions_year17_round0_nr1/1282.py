#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
//#include <unordered_map>
#include <list>
#include <bitset>
#include <utility>
#include <cassert>
#include <iomanip>
#include <ctime>
#include <fstream>
#include <bitset>

using namespace std;

const int me = 1025;

int T, N, K;
string s;


int main(int argc, const char * argv[]) {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    cin >> T;
    for(int c = 0; c < T; c ++){
        cin >> s >> K;
        N = (int)s.size();
        int result = 0;
        for(int i = 0; i + K - 1 < N; i ++)
            if(s[i] == '-'){
                result ++;
                for(int j = i; j < i + K; j ++)
                    s[j] = '+' + '-' - s[j];
            }
        for(int i = 0; i < N; i ++)
            if(s[i] == '-'){
                result = -1;
                break;
            }
        cout << "Case #" << c + 1 << ": ";
        if(result == -1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << result << endl;
    }
    
    return 0;
}
