#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
#include <cstring>
#include <iomanip>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
#include <list>
#include <string>
#include <vector>
#include <new>
#include <bitset>
#include <ctime>
#include <stdint.h>
#include <unistd.h>
 
 using namespace std;
 
#define ll long long int
#define INF 1000000000
#define PI acos(-1.0)
#define EPS 1e-9
 
template <typename X> X gcd(X a, X b){if(!b)return a; else return gcd(b, a%b);}
 
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ll, ll> llp;
typedef pair<double, double> dd;
typedef pair<char, int> ci;

int t, a, b, foo, ans, i, j, flag, cs=1;
int x[5], y[5];

int main()
{
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &a);
        for(i=1;i<=4;++i)
        {
            if(i==a)
                for(j=1;j<=4;++j)
                    scanf("%d", &x[j]);
            else
                for(j=1;j<=4;++j)
                    scanf("%d", &foo);
        }
        scanf("%d", &b);
        for(i=1;i<=4;++i)
        {
            if(i==b)
                for(j=1;j<=4;++j)
                    scanf("%d", &y[j]);
            else
                for(j=1;j<=4;++j)
                    scanf("%d", &foo);
        }
        flag=0;
        for(i=1;i<=4;++i)
            for(j=1;j<=4;++j)
                if(x[i]==y[j])
                {
                    flag++;
                    ans=x[i];
                    break;
                }
        if(flag==0)
            printf("Case #%d: Volunteer cheated!\n", cs++);
        else
        if(flag==1)
            printf("Case #%d: %d\n", cs++, ans);
        else
            printf("Case #%d: Bad magician!\n", cs++);
    }
    return 0;
}