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
bool used[1001];

int main()
{
   	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n;
        cin>>n;

        vector<double> A,B;

        for (int i = 1; i <= n; i++)
        {
            double x; cin>>x;
            A.PB(x);
        }

        for (int i = 1; i <= n; i++)
        {
            double x; cin>>x;
            B.PB(x);
        }

        sort(A.begin(),A.end());
        sort(B.begin(),B.end());

        int score1 = 0, score2 = 0;

        int j1 = 0, j2 = n - 1;

        for (int i = 0; i < A.size(); i++)
        {
            if (A[i] > B[j1])
            {
                score1++;
                j1++;
            }
        }

        memset(used,false,sizeof(used));

        for (int i = 0; i < A.size(); i++)
        {
            double min_v = -1;
            int idx = -1;
            for (int j = 0; j < B.size(); j++)
                if (!used[j] && B[j] > A[i])
                {
                    if (min_v == -1)
                    {
                        min_v = B[j];
                        idx = j;
                    }
                    else if (B[j] < min_v)
                    {
                        min_v = B[j];
                        idx = j;
                    }
                }

            if (idx != -1)
            {
                used[idx] = true;
            }
            else
            {
                score2++;
                for (int j = 0; j < B.size(); j++)
                    if (!used[j])
                    {
                        used[j] = true;
                        break;
                    }
            }
        }
        cout<<"Case #"<<tt<<": "<<score1<<" "<<score2<<endl;
    }
	return 0;
}
