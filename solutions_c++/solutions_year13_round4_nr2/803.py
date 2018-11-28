#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <math.h>
#include <cmath>

#define PB push_back
#define MP make_pair
#pragma comment(linker, "/STACK:16777216")

typedef long long int64;
typedef unsigned long long uint64;

using namespace std;

/*
inline int read_int()
{
    register char c;
    while ((c=getchar_unlocked()) < 48 || c > 57);
    int p = c-48;
    while ((c=getchar_unlocked()) >= 48 && c <= 57) p=p*10+c-48;
    return p;
}
*/

/*
struct matrix
{
    int64 a[2][2];
};

matrix mul(matrix A,matrix B)
{
    matrix C;
    memset(C.a,0,sizeof(C.a));
    for (int i = 0; i <= 1;i ++)
        for (int j = 0; j <= 1; j++)
            for (int k = 0; k <= 1; k++)
                C.a[i][j] = (C.a[i][j] + A.a[i][k] * B.a[k][j]) % md;
    return C;
}

matrix pow(matrix A, int64 p)
{
    if (p == 1) return A;
    if (p & 1) return mul(A,pow(A,p-1));
    matrix X = pow(A,p >> 1);
    return mul(X,X);
}

*/

int main()
{
	ifstream inp("B-small-attempt0.in");
    ofstream out; out.open("output.txt");

    int test;
    inp>>test;
    for (int tt = 1; tt <= test; tt++)
    {
        int64 n,p;
        inp>>n>>p;
        p--;
        int64 low = 0, high = 1;
        for (int i = 1; i <= n; i++) high*=2;
        high--;
        int64 mm = high;
        int64 out1 = -1;
        while (low <= high)
        {
            int64 mid = (low+high)/2;

            int64 bit0 = 0,bit1 = 0;

            int64 cc = mid+1;
            while (cc > 1)
            {
                cc/=2;
                bit1++;
            }

            cc = 1;
            int64 pos = 0;
            bit1 = n-bit1;
            for (int i = 1; i <= bit1; i++)
            {
                pos += cc;
                cc*=2;
            }
            //cout<<pos<<endl;
            pos = mm-pos;

            //cout<<mid<<" "<<bit1<<" "<<pos<<" "<<p<<endl;
            if (pos > p) high = mid-1;
            else
            {
                out1 = max(out1,mid);
                low = mid+1;
            }
        }

        int64 out2 = -1;
        low = 0, high = mm;
        while (low <= high)
        {
            int64 mid = (low+high)/2;

            int64 bit0 = 0,bit1 = 0;

            int64 cc = mm+1-mid;
            while (cc > 1)
            {
                cc/=2;
                bit1++;
            }

            cc = 1;
            int64 pos = 0;
            bit1 = n-bit1;
            for (int i = 1; i <= bit1; i++)
            {
                cc*=2;
            }
            bit1 = n-bit1;
            for (int i = 1; i <= bit1; i++)
            {
                pos+=cc;
                cc*=2;
            }
            //cout<<pos<<endl;
            pos = mm-pos;

            //cout<<mid<<" "<<bit1<<" "<<pos<<" "<<p<<endl;
            if (pos > p) high = mid-1;
            else
            {
                out2 = max(out2,mid);
                low = mid+1;
            }
        }

        out<<"Case #"<<tt<<": "<<out1<<" "<<out2<<endl;
    }
	return 0;
}
