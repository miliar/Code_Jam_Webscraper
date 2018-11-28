/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define pll pair < ll, ll >
#define pill pair< int, pll >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
typedef long long ll;
int S[10];
void mark(int x)
{
    while(x > 0)
    {
        int c = x%10;
        S[c] = 1;
        x /= 10;
    }
}
bool done(){
    for(int i=0;i<10;i++){
        if(S[i] == 0)
            return false;
    }
    return true;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        //int n = z;
        int n;
        scanf("%d",&n);
        printf("Case #%d: ", z);
        if(n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        for(int i=0;i<10;i++)
            S[i] = 0;
        int m = n;
        while(1)
        {
            mark(m);
            if(done())
            {
                printf("%d\n", m);
                break;
            }
            m += n;
        }
    }
    return 0;
}
