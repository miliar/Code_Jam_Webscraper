#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 1

using namespace std;

set<int> card1;

void solve(int ca)
{
    int x;
    int row;
    scanf("%d",&row);
    card1.clear();
    FOR(i,1,4)
    {
        FOR(j,1,4)
        {
            scanf("%d",&x);  
            if(i == row) card1.insert(x);
        }
    }
    scanf("%d",&row);
    vector<int> v;
    int num = 0;
    int ans = 0;
    FOR(i,1,4)
    {
        FOR(j,1,4)
        {
            scanf("%d",&x);
            if(i == row)
            {
                if(card1.find(x) != card1.end())
                {
                    ans = x;
                    num++;     
                }
            }
        }
    }
    printf("Case #%d: ",ca);
    if(num == 0) puts("Volunteer cheated!");
    else if(num > 1) puts("Bad magician!");
    else printf("%d\n",ans);
    
}

int main()
{
    int t;
    scanf("%d",&t);
    FOR(ca,1,t)
    {
        solve(ca);
    }
    return 0;
}
