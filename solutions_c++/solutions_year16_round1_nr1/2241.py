#include <set>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <vector>
#include <limits>
#include <utility>
#include <map>
#include <sstream>
#include <queue>

using namespace std;

#define MAXN 106
#define MAXD 50
#define MOD 1000000007

typedef long long ll;

ll T,n, x, y;

string s;

int main(){


    cin >> T;
    for (int cse = 1; cse <= T; cse++){
        cin >> s;
        string res = "";
        for (int i = 0; i < s.size(); i++){
            if (!i){
                res += s[i];
            }
            else {
                if (s[i] >= res[0]){
                    res = s[i] + res;
                }
                else
                    res = res + s[i];
            }
        }
        cout << "Case #" << cse << ": " << res << endl;
    }

    return 0;

}


