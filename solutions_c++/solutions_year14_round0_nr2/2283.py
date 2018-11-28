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
#include <queue>

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



int64 pow(int64 x, int64 y, int64 z)
{
    if (y == 0) return 1%z;
    if (y == 1) return x%z;
    if (y & 1) return (x*pow(x,y-1,z))%z;
    int64 temp = pow(x,y>>1,z);
    return (temp*temp)%z;
}
*/

int main()
{
   	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    for (int tt = 1; tt <= t; tt++)
    {
        double c,f,x;
        cin>>c>>f>>x;

        double cur_t = 0, cur_s = 0,cur_g = 2.0;
        double min_t = -1.0;

        while (true)
        {
            double need = (x - cur_s)/cur_g;

            double new_t = cur_t + need;

            if (min_t < 0) min_t = new_t;
            else
            {
                if (min_t - new_t < 1e-9) break;
                min_t = min(min_t,new_t);
            }

            //cout<<min_t<<endl;
            // buy

            double need_c = (c - cur_s)/cur_g;
            cur_s = 0;
            cur_g += f;
            cur_t += need_c;
        }

        printf("Case #%d: %.7lf\n",tt,min_t);
        //cout<<"Case #"<<tt<<": "<<min_t<<endl;

    }
	return 0;
}
