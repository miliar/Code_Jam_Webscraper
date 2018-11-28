using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
 
#define foreach(x, v) for (typeof (v).begin() x=(v).begin(); x !=(v).end(); ++x)
#define forr(i, a, b) for (int i=(a); i<(b); ++i)
#define fore(i, a, b) for (int i=(a); i<=(b); ++i)
#define exists(e, v) find((v).begin(), (v).end(), (e))!=(v).end()
#define print(v) for (auto x=(v).begin(); x !=(v).end(); ++x) { cout << *x << " "; } cout << endl;  

typedef vector<int> vi;
 
int main(){
    freopen("A-small-attempt0.in","r", stdin);
    int T;
    cin >> T;
    fore(test, 1, T){
        int r1;
        cin >> r1;

        vi row(4);

        fore(i, 1, 4) {
            forr(j, 0, 4) {
                int c;
                cin >> c;
                if(i == r1)
                    row[j] = c;
            }
        }

        int r2;
        cin >> r2;

        int ans = 0;

        //print(row);

        fore(i, 1, 4) {
            forr(j, 0, 4) {
                int c;
                cin >> c;
                if ( exists(c, row) && i == r2){
                    if(ans == 0)
                        ans = c;
                    else if(ans > 0)
                        ans = -1;
                }
            }
        }
        string output = to_string(ans);
        if(ans == 0)
            output = "Volunteer Cheated!";
        else if(ans == -1)
            output = "Bad Magician!";
            
        cout << "Case #" << test << ": " << output << endl;
    }
    return 0;
}

