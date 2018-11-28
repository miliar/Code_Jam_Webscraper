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
    int i,t,len;
    string str,s,ts;

    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin >> t;
    for (int cid = 1; cid <= t; cid++) {
        cin >> str;
        cout << "Case #" << cid << ": ";
        len = str.length();

        s = "";
        s.push_back(str[0]);
        for (i = 1; i < len; i++) {
            if (str[i] >= s[0]) {
                ts = "";
                ts.push_back(str[i]);
                ts = ts + s;
                s = ts;
            } else {
                s.push_back(str[i]);
            }
        }
        cout << s << endl;
    }

    return 0;
}
