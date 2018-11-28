#include <iostream>
#include<fstream>
using namespace std;
#define LL long long
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    LL m, b;
    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> b >> m;
        LL mx = (1ll << (b - 2ll));
        int res[52][52] = {0};
        if(m > mx)
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        else{
            LL p = mx / 2ll;
            for(int j = 1; j < b; j++)
                for(int k = j + 1; k < b; k++)
                    res[j][k] = 1;
            int a = b - 1;
            while(p){
                if(m >= p){
                    res[a][b] = 1;
                    m -= p;
                }
                p /= 2ll;
                a--;
            }
            if(m == 1){
                res[1][b] = 1;
            }
            cout << "Case #" << i + 1 << ": POSSIBLE" << endl;
            for(int j = 1; j <= b; j++){
                for(int k = 1; k <= b; k++)
                    cout << res[j][k];
                cout << endl;
            }
        }
    }
    return 0;
}

