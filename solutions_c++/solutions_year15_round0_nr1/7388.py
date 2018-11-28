// -------------------- Khai bao thu vien --------------------
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>

#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

using namespace std;

// -------------------- Khai bao cac container --------------------
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <string> vs;

typedef long long int64; //NOTES:int64
typedef unsigned long long uint64; //NOTES:uint64
typedef unsigned uint;

int main(){
    freopen("A-output-large", "w", stdout);
    freopen("A-large.in", "r", stdin);
    int t, smax, i, res, k, tmp;
    bool haveSlot = false;
    string s;
    scanf("%d", &t);
    for(i = 1; i <= t; i++){
        if (i > 1) cout << "\n";
        res = 0;
        scanf("%d", &smax);
        cin >> s;
        tmp = 0;
        for(k = 0; k < smax+1; k++){
            if (s[k] == '0') haveSlot = true;
            int a = s[k] - '0';
            if (tmp < k && haveSlot && k > 0) {
                res += k - tmp;
                tmp = k;
            }
            tmp += a;
        }
        printf("Case #%d: %d", i, res);// cout << "Case #" + i + ": " + res;
    }
    fclose(stdin);
    fclose(stdout);
}
