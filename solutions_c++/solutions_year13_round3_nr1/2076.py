#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cassert>
using namespace std;

bool app(char c){
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int deal(string s, int n){
    int rst = 0, len = s.length();
    bool fir = true;

    for (int i = 0; i <= len-n; i++){
        bool ok = true;
        int j = i, cnt = 0;
        for (; j < len; j++){
            if (app(s[j])){
                cnt = 0;
            }
            else
                cnt++;

            if (cnt == n)
                break;
        }

        if (cnt == n){
            //cout << i << " " << j << endl;
            rst += (len-j);
        }
    }

    return rst;
}

int main(){
#ifdef HOME
    //freopen("infile", "r", stdin);
    freopen("A-small-attempt.in", "r", stdin);
    freopen("rst.out", "w", stdout);
#endif

    int t, cs = 1;
    cin >> t;

    while (t--){
        int n;
        string s;
        cin >> s >> n;
        printf("Case #%d: %d\n", cs++, deal(s, n));
    }
    
#ifdef HOME
    //printf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
#endif

    return 0;
}
