#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <ctime>
#include <deque>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i ++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define pi 3.1415926535897932384626433832795l

typedef long long ll;
typedef long double ld;

int ans[2];
int a[2][4][4];
set <int> s;

int main(){
#ifdef SG
    freopen ("input.txt","rt",stdin);
  freopen ("output.txt","wt",stdout);
#endif  
    int t;
    cin >> t;
    forn(qqq, t){
        s.clear();
        cout << "Case #" << qqq + 1 << ": ";
        forn(num, 2){
            cin >> ans[num];
            ans[num] --;
            forn(i, 4){
                forn(j, 4){
                    cin >> a[num][i][j];
                    a[num][i][j] --;
                }
            }
            }
            forn(i, 4){
                s.insert(a[0][ans[0]][i]);
            }
            int res = 0, result = -1;
            forn(i, 4)
                if (s.find(a[1][ans[1]][i]) != s.end()){
                    result = a[1][ans[1]][i];
                    res ++;
                }
            if (res == 0){
                cout << "Volunteer cheated!" << endl;
            } else if (res > 1){
                cout << "Bad magician!" << endl;
            } else {
                cout << result + 1 << endl;
            }           
        

    } 


    return 0;
}
