#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <bitset>
using namespace std;

#define pi pair<int,int>
#define mp(x,y) make_pair(x,y)
#define fi first
#define se second
#define pl pair<long long,long long>
#define pb push_back
#define vi vector<int>
#define ll long long
#define ALL(c) c.begin(),c.end()
#define VAR(v,n) __typeof(n) v=(n)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)

const int MAXN=1005;
char t[MAXN];

int main ()
{
    int a,b,c,d,e,f,g,z,n,k;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%s%d", t, &k);
        b=0;
        for (n=0; t[n]; n++);

        for (c=0; c+k<=n; c++)
            if (t[c]=='-')
            {
                b++;

                for (d=c; d<c+k; d++)
                    if (t[d]=='-')
                        t[d]='+';
                    else
                        t[d]='-';
            }

        for (c<n; t[c]=='+'; c++);

        printf ("Case #%d: ", a);

        if (c<n)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", b);
    }

    return 0;
}
