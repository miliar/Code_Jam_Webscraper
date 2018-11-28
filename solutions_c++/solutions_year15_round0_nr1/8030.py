#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("1_1large.out", "w", stdout);
    int t, n, slast = 0, k = 0;
    string s;
    cin >> t;
    for ( int i = 0; i < t; i++){
        cin >> n >> s;
        for ( int j = 0; j <= n; j++){
            if ( s[j] != '0'){
                if ( slast >= j  || j == 0){
                    slast += atol(s.substr(j, 1).c_str());
                    //cout << "slast=" << slast << endl;
                }

                else{
                    k += j-slast;
                    //cout << "k=" << k << endl;
                    slast += atol(s.substr(j, 1).c_str())+j-slast;
                }
            }
        }
        cout << "Case #" << i+1 << ": " << k << endl;
        slast = 0;
        k = 0;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
