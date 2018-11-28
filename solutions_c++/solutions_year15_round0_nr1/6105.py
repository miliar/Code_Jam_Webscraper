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
    freopen("b.out","w",stdout);
    int test,n;
    scanf("%d",&test);
    int cases = 0;
    string s;
    while(test)
    {
        cases ++;
        scanf("%d",&n);
        cin >> s;
        int sum = s[0] - '0' ;
        int needed = 0;
        for(int i=1 ;i<s.size() ;i++)
        {
           if(sum < i)
           {
               needed = needed + (i-sum);
               sum = sum + (i-sum);
           }
           sum = sum + (s[i] - '0');
        }
        printf("Case #%d: %d\n",cases,needed);
        test --;
    }

    return 0;
}
