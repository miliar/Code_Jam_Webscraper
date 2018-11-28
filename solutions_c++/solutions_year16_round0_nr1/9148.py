/* Created by Anmol Varshney */

#include <stdio.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define ARRAY_SIZE(arr) sizeof(arr)/sizeof(arr[0])
#define INT_MIN -2147483647
#define INT_MAX 2147483647
#define INF 2000000000
#define INF_LL 9223372036854775807LL
#define PI acos(-1.0)
#define llu long long unsigned
#define ll long long int
#define ld long int
#define iter(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define REP(p,a,b) for(int p=a;p<b;p++)
#define mod 1000000007
#define getchar_unlocked getchar
#define pb(f) push_back(f)
#define pob(f) pop_back(f)
#define pf(f) push_front(f)
#define pof(f) pop_front(f)
#define mkp(a,b) make_pair(a,b)
#define fst first
#define snd second
#define pii pair<int,int>
#define ins(a) insert(a)

int gcd(int a,int b)
{
    if(b>a) return gcd(b,a);
    else if(b!=0) return (b,a%b);
    else return a;
}

set<int> s;

int main() {
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    int l,t;
    ll n,N,i;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        printf("Case #%d: ",l);
        i=2;
        s.clear();
        scanf("%lld",&n);
        if(n)
        {
            N=n;
            while(s.size()!=10)
            {
                while(N)
                {
                    s.ins(N%10);
                    N/=10;
                }
                N=n*i;
                i++;
            }
            N=n*(i-2);
            printf("%lld\n",N);
        }
        else printf("INSOMNIA\n");
    }
    return 0;
}
