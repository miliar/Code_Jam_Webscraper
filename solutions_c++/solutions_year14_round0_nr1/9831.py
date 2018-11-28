#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>

#define ll long long
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define me(t, val) memset(t, val, sizeof(t))
#define pb(a) push_back(a)
#define mp make_pair

#define MAXN 100
#define MOD 1073741824

using namespace std;

int main(){
    int t, r1, r2, a, b, c, d, caso = 1;
    cin >> t;
    while(t--){
        cin >> r1;
        map <int, int> M;
        for(int i=0; i<4; i++){
            cin >> a >> b >> c >> d;
            if(i == r1-1){
                M[a]++;
                M[b]++;
                M[c]++;
                M[d]++;
            }
        }
        cin >> r2;
        for(int i=0; i<4; i++){
            cin >> a >> b >> c >> d;
            if(i == r2-1){
                M[a]++;
                M[b]++;
                M[c]++;
                M[d]++;
            }
        }
        int cont = 0, ans;
        for(int i=1; i<=16; i++){
            if(M[i] == 2){
                cont++;
                ans = i;
            }
        }
        cout << "Case #" << caso++ << ": ";
        if(cont == 0) cout << "Volunteer cheated!" << endl;
        else if(cont == 1) cout << ans << endl;
        else cout << "Bad magician!" << endl;
    }
}
