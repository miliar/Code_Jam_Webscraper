#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)
using namespace std;
int main ()
{
Read("input.in");
Write("output.out");
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {int a,b;
    cin>>a;int c[4][4];int d[4][4];

    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            cin>>c[i][j];

        }
    }
    cin>>b;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            cin>>d[i][j];

        }
    }
    int aux=0;int con=0;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(c[a-1][i]==d[b-1][j])
            {
            aux=c[a-1][i];con++;
            }
        }
    }
    if(con>1)
    {cout<<"Case #"<<k<<": Bad magician!"<<endl;
    }
    else{
    if(con==0)
    cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
    else cout<<"Case #"<<k<<": "<<aux<<endl;
    }

    }
    return 0;
}
