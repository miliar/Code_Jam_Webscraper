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
#include "fstream"

#define sz(X) ((int)X.size())
#define FOR(i,x,y) for(int i=x; i<y; ++i)
#define FORE(i,x,y) for(int i=x; i<=y; ++i)
char buf[50]; std::string itos(int x) {sprintf(buf,"%d",x); return buf;}

using namespace std;

int main()
{
    //ofstream cout ("output.txt");
    ifstream cin ("input.txt");

    int T;
    cin>>T;

    FOR(i,1,T+1)
    {
        double C,F,X; cin>>C>>F>>X;
        double ans = X;
        bool shouldContinue = true;
        int nf = 0; //number of farms
        double currentRate = 2.0;
        double time_to_buy_farms = 0;
        while (shouldContinue)
        {
            double tans = time_to_buy_farms + X / currentRate;

            if(tans < ans)
            {
                ans = tans;
                time_to_buy_farms = time_to_buy_farms + C / currentRate;
                currentRate += F;
            }
            else break;
        }


        printf("Case #%d: %.7f\n",i,ans);
//        cout<<"Case #"<<i<<": "<<ans<<endl;
    }

    return 0;
}