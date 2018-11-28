#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template <class T> T gcd(T a, T b) { return b==0 ? a : gcd(b,a%b) ; }
template <class T> T maxm(T a, T b) { return a > b ? a : b ; }
template <class T> T minm(T a, T b) { return a < b ? a : b ; }
template <class T> T abs(T a) { return a > 0 ? a : (-1)*a ; }
template <class T> T sq(T a) { return a * a ; }

#define clr(a) memset(a,0,sizeof(a))
#define set(a) memset(a,-1,sizeof(a))
#define R(a) freopen(a,"r",stdin)
#define W(t) while(t--)
#define forr(x, b, e)    for (int x = (b); x <= (e); x++)
#define S(n) scanf("%d",&n)
#define MAX 105


int main()
{
    int t,n,m,i,j,flag,mx,c=0;
    int a[MAX][MAX];
    int row[MAX],col[MAX];
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    S(t);
    W(t)
    {
        S(n);
        S(m);
        forr(i,0,n-1)
        {
            mx=0;
            forr(j,0,m-1)
            {
                S(a[i][j]);
                if(mx<a[i][j])
                {
                    mx=a[i][j];
                }
            }
            row[i]=mx;
        }

        forr(j,0,m-1)
        {
            mx=0;
            forr(i,0,n-1)
            {
                if(mx<a[i][j])
                {
                    mx=a[i][j];
                }
            }
            col[j]=mx;
        }

        flag=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]<row[i] && a[i][j]<col[j])
                {
                    flag=1;
                    break;
                }
            }
        }
        if(flag==1)
        {
            printf("Case #%d: NO\n",++c);
        }
        else
        {
            printf("Case #%d: YES\n",++c);
        }
    }
    return 0;
}
