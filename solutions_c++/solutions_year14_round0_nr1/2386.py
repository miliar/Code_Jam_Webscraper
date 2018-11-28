/* In the name of ALLAH, most gracious, most merciful */

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <ctime>
#include <iomanip>
#include <cstring>
#include <map>
 
using namespace std;
typedef long long ll;
typedef pair< int, int > pi;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
#endif
    
    int T, R, t = 1, x;
    cin >> T;
    while(T--){
        cin >> R;
        --R;
        set< int > S;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> x;
                if(i == R){
                    S.insert(x);
                }
            }
        }
        cin >> R;
        --R;
        int n;
        int total = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> x;
                if(i == R && S.count(x) > 0){
                    ++total;
                    n = x;
                }
            }
        }
        cout << "Case #" << t++ << ": ";
        if(total == 0){
            cout << "Volunteer cheated!" << endl;
        }else if(total == 1){
            cout << n << endl;
        }else{
            cout << "Bad magician!" << endl;
        }
        
    }
    
    return 0;
}