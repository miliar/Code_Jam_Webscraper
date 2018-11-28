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
int n,m;
int64 mod = 1000002013;
int64 cost(int a, int b,int c, int d)
{
    int64 cost1 = 0;
    if (b-a == 1) cost1 = n;
    else cost1 = ((n+n+1-(b-a))*(b-a))/2;
    cost1 %= mod;

    if (d-c == 1) cost1 += n;
    else cost1 += ((n+n+1-(d-c))*(d-c))/2;
    cost1 %= mod;

    return cost1;
}
int main()
{
	ifstream inp("A-small-attempt0.in");
    ofstream out; out.open("output.txt");

    int test;
    inp>>test;
    int64 icost = 0;
    int64 cnt = 0;
    for (int tt = 1; tt <= test; tt++)
    {
        icost = 0;
        cnt = 0;
        inp>>n>>m;

        map<pair<int, int>,int> A;
        A.clear();
        for (int i = 1; i <= m; i++)
        {
            int p,q,k;
            inp>>p>>q>>k;
            icost += ((cost(p,q,0,0)*k)%mod);
            A[MP(p,q)]+=k;
        }

        map<pair<int, int>,int>::iterator ii,pp;
        for (int i = 1; i <= 1; i++)
        {
            for (ii = A.begin(); ii != A.end(); ii++)
                for (pp = A.begin(); pp != A.end(); pp++)
                    if (ii != pp)
                    {
                        int a,b,c,d,v1,v2;
                        a = (*ii).first.first;
                        b = (*ii).first.second;
                        c = (*pp).first.first;
                        d = (*pp).first.second;
                        v1 = (*ii).second;
                        v2 = (*pp).second;

                        int64 choice = 1, res = cost(a,b,c,d);
                        if ((a<=c) && (c<=b) && (b<=d))
                        {

                            if (cost(a,d,c,b) < res)
                            {
                                res = cost(a,d,c,b);
                                choice = 3;
                            }
                        }

                            if (choice == 3)
                            {
                                cnt++;
                                int dif = min(v1,v2);
                                A[MP(a,b)]-=dif;
                                A[MP(c,d)]-=dif;
                                A[MP(a,d)]+=dif;
                                A[MP(c,b)]+=dif;
                            }
                        //cout<<a<<" "<<b<<" "<<c<<" "<<d<<" "<<v1<<" "<<v2<<" "<<choice<<endl;
                    }
        }

        int64 fcost = 0;
        for (ii = A.begin(); ii != A.end(); ii++)
        {
            int p,q,k;
            p = (*ii).first.first;
            q = (*ii).first.second;
            k = (*ii).second;
            //cout<<p<<" "<<q<<" "<<k<<endl;
            fcost += ((cost(p,q,0,0)*k)%mod);
        }

        int64 resu = icost - fcost;
        if (resu < 0) resu += mod;
        out<<"Case #"<<tt<<": "<<resu<<endl;

    }

    out.close();
	return 0;
}
