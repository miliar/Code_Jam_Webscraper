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

int t, cs=1;
double c, f, x, ans, tmp, r, p;

int main()
{
    scanf("%d", &t);
    while(t--)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        ans=(double)INF;
        tmp=0.0;
        r=2.0;
        p=0.0;
        while(1)
        {
            tmp=x/r;
            if(tmp+p<ans)
                ans=tmp+p;
            else
                break;
            p+=c/r;
            r+=f;
        }
        printf("Case #%d: %.7lf\n", cs++, ans);
    }
    return 0;
}