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
   	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for (int tt = 1; tt <= t; tt++)
    {
        int n;
        cin>>n;

        int a[5][5];
        memset(a,0,sizeof(a));

        bool b[17];
        memset(b,false,sizeof(b));

        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++) cin>>a[i][j];

        for (int i = 1; i <= 4; i++) b[a[n][i]] = true;

        vector<int> res; res.clear();

        cin>>n;

        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++) cin>>a[i][j];

        for (int i = 1; i <= 4; i++)
            if (b[a[n][i]]) res.PB(a[n][i]);


        cout<<"Case #"<<tt<<": ";

        if (res.size() == 0) cout<<"Volunteer cheated!"<<endl;
        else if (res.size() == 1) cout<<res[0]<<endl;
        else cout<<"Bad magician!"<<endl;
    }
	return 0;
}
