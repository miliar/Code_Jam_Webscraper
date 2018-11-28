#include <iostream>
#include <algorithm>
#include <cstdio>
#include <fstream>
#include <queue>
#include <math.h>
#include <limits.h>
#include <cstdlib>
#include <string.h>
#include <vector>
#include <iomanip>
#include <map>
#include <stack>
using namespace std;
//mehulagarwal
#define ll         long long
#define S(x)       scanf("%d", &x)
#define Sl(x)      scanf("%lld", &x)
#define Sd(x)      scanf("%lf", &x)
#define P(x)       printf("%d\n", x)
#define Pl(x)      printf("%lld\n", x)
#define Pd(x)      printf("%lf\n", x)
#define Pblank()   printf(" ")
#define mem(x,y)   memset(x,y,sizeof(x))
#define F(x,y,z,i) for (x = y; x < z; x = x + i)
#define mod 1000000007
using namespace std;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    ll int t,val,flag,n,i,j;
    map<ll int,ll int>m;

    cin >> t;

    for (int cid = 1; cid <= t; cid++) {
        cout << "Case #" << cid << ": ";

        cin >> n;

        if (n == 0) {
            cout << "INSOMNIA\n";
            continue;
        }

        for (i = 1; i <= 1000000; i++) {
            val = n*i;
          //  cout << val << " -> ";
            while (val > 0) {
                ll int rem = val % 10;
               // cout << rem << endl;
                val = val / 10;
                m[rem]++;
            }
            flag = 0;
            for (j = 0; j < 10; j++) {
                if (m[j] == 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                flag = 2;
                val = n * i;
                break;
            }
        }
        if (flag == 2) {
            cout << val << endl;
        } else {
            cout << "INSOMNIA\n";
        }

        m.clear();
    }

    return 0;
}
