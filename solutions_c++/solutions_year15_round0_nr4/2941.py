#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <string.h>
#include <numeric>
using namespace std;

 typedef vector<int> vi;
 typedef vector<vi> vvi;
 typedef pair<int,int> ii;
 typedef long long ll;
 #define sz(a) int((a).size())
 #define pb push_back
 #define all(c) (c).begin(),(c).end()
 #define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
 #define present(c,x) ((c).find(x) != (c).end())
 #define cpresent(c,x) (find(all(c),x) != (c).end())


int main()
{
    //freopen("a.in","r",stdin);
    freopen("c.out","w",stdout);
    int test,n,x,r,c;
    scanf("%d",&test);
    int cases = 0;
    while(test)
    {
        cases ++;
        int flag = 0;
        scanf("%d%d%d",&x,&r,&c);
        int mini = min(r,c);
        int area = r*c;
        int k = area % x;
        if(k == 0) flag = 1;
        else flag = 0;
        if(flag == 1)
        {
                if(mini < x-1)
                {
                    flag = 0;
                }
        }
        if(flag == 0) printf("Case #%d: RICHARD\n",cases);
        else printf("Case #%d: GABRIEL\n",cases);
        test --;
    }
    return 0;
}
