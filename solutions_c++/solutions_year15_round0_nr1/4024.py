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

    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);

    ll t, i;
    cin>> t;
    for(i = 0;  i < t; i++)
    {
        ll n, j, k, ot = 0;
        char c;
        cin>>n;
        n++;
        k = 0;
        for(j = 0; j < n; j++)
        {
            cin>> c;
            if(c != '0')
                if( k < j) ot += j - k, k = j;
            k += (c - '0');
        }
        cout<<"Case #"<<i + 1<<": "<<ot<<endl;

    }
    return 0;
}


