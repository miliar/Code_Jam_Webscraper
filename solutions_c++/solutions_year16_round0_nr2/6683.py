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

    ll int t,i,len,nflip,flag;
    string str;

    cin >> t;

    for (int cid = 1; cid <= t; cid++) {
        cin >> str;
        cout << "Case #" << cid << ": ";
        len = str.length();

        nflip = 0;
        while (1) {
            flag = 0;
            for (i = len-1; i >= 0; i--) {
                if (flag == 0) {
                    if (str[i] == '-') {
                        str[i] = '+';
                        flag = 1;
                    }
                } else {
                    if (str[i] == '+') {
                        str[i] = '-';
                    } else {
                        str[i] = '+';
                    }
                }
            }
            if (flag == 1) {
                nflip++;
            }
            flag = 0;
            for (i = 0; i < len; i++) {
                if (str[i] == '-') {
                    flag = 1;
                }
            }
            if (flag == 0) {
                break;
            }
        }
        cout << nflip << endl;
    }

    return 0;
}
