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
#include <limits>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define INF_LL 9223372036854775807
#define INF 2000000000
#define PI acos(-1.0)
#define EPS 1e-9
#define LL long long
#define mod 1000000007
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin >> t;
    int temp = t;
    while(t--)
    {
        double c,f,x,time=0,rate=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        while(c/rate+x/(rate+f) < x/rate)
        {
            time+=c/rate;
            rate+=f;
        }
        time+=x/rate;
        cout << "Case #" << temp-t << ": ";
        printf("%.7lf\n",time);
    }
    return 0;
}

/*
struct lady
{
    int beauty,smart,rich;
};

bool sorter1(lady a,lady b)
{
    return a.beauty < b.beauty;
}

bool sorter2(lady a,lady b)
{
    return a.beauty == b.beauty && a.smart < b.smart;
}

bool sorter3(lady a,lady b)
{
    return a.beauty == b.beauty && a.smart == b.smart && a.rich < b.rich;
}

int main()
{
    int n;
    cin >> n;
    lady ladies[n];
    for(int i=0;i<n;i++)
        scanf("%d",&ladies[i].beauty);
    for(int i=0;i<n;i++)
        scanf("%d",&ladies[i].smart);
    for(int i=0;i<n;i++)
        scanf("%d",&ladies[i].rich);
    sort(ladies,ladies+n,sorter1);
    sort(ladies,ladies+n,sorter2);
    sort(ladies,ladies+n,sorter3);
    for(int i=0;i<n;i++)
        printf("%d %d %d\n",ladies[i].beauty,ladies[i].smart,ladies[i].rich);
    return 0;
}
*/
