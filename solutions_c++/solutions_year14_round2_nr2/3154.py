#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
int i;
long long l, n,p;
int t;
int ans;
long long a,b,k;

    cin >> t;
    for (i = 1; i <= t; i++){
        cin >> a; //3
        cin >> b; //4
        cin >> k; //2


        ans = 0;
        for (n = a-1; n >= 0; n--){ //3
            for(p = b-1; p >= 0; p--){ //4
                for (l = k-1; l >= 0; l--){ //2
                    if ((n&p) == l) ans ++;
                }
            }
        }


        cout << "Case #" << i << ": " << ans << endl;
    }



    return 0;
}
