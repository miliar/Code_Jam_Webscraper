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
#include <fstream>
#include <string.h>
#include <climits>

#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)
#define pb push_back
#define full(v)	v.begin(),v.end()
#define VI vector<int>
#define VS vector<string>
#define LL long long
using namespace std;
int main()
{
    int test,cas=0;
    ifstream cin ("gcjin2small.in");
 //   ofstream cout ("gcjout2.txt");
    cin>>test;
    while(test-- && ++cas)
    {
        double c,f,x;
        cin>>c>>f>>x;
        double curr = 2.0;
        cout<<"Case #"<<cas<<": ";
        double thrunextfarm , thrucurrentrate;
        double sum = 0;
        while(1)
        {
            thrucurrentrate = x/curr;
            thrunextfarm = c/curr + x/(curr+f);
            if(thrucurrentrate < thrunextfarm)
            {
                sum+=x/curr;
                printf("%.6f\n",sum);
                break;
            }
            else
            {
                sum+=c/curr;
                curr+=f;
            }
        }
    }
    return 0;
}
