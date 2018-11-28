#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>

#define sqr(a) ((a)*(a))
#define ABS(A) ((a)>0 ? (a) : -(a))
#define MIN(a,b) ((a)>(b) ? (b) : (a))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define fi first
#define se second

typedef long long ll;

using namespace std;

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    ll t, i;
    cin>> t;
    for(i = 1;  i <= t; i++)
    {
        ll n, j, a[10], k, ot = 10, ost = 0;
        memset(a, 0, sizeof(a));
        cin>> n;
        for(j = 0; j < n; j++)
        {
            cin>> k;
            a[k]++;
        }

        if(a[9] == 1 && a[8] == 0 && a[7] == 0 && a[6] == 0 && a[5] == 0 && a[4] == 0)
        {
            ot = 5;
        }
            else
                if(a[9] == 1 && a[8] == 0 && a[7] == 0 && (a[6] + a[5] + a[4] == 1))
        {
            ot = 6;
        } else
        for(j = 9; j >= 1; j--)
        {
            if(a[j] > 0)
            {
                if(ot >= ost + j)
                    ot = ost + j;
                ost += a[j];
                a[j / 2] += a[j];
                a[j / 2 + j % 2] += a[j];
            }
        }
        cout<<"Case #"<<i<<": "<<ot<<endl;
    }
    return 0;
}


