#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 100 + 10;
int n, m;

int a, b ,k;

int T,TT;

int main()
{
    freopen("R1B_2_in.txt", "r", stdin);
    freopen("R1B_2_out.txt", "w", stdout);

    cin >> T;
    TT = 1;

    while(T) {
        //memset(a,0,sizeof(a));
        //memset(ct,0,sizeof(ct));

        cin >> a >> b >> k;

        long long s = 0;
        for (int i = 0; i < a; i ++)
            for (int j = 0; j < b; j ++)
                if( (i & j) < k)
        {
            //cout << i << ' ' << j << endl;
            s ++;

        }

        cout << "Case #" << TT << ": " << s << endl;
        T --;
        TT ++;
    }

    return 0;
}

