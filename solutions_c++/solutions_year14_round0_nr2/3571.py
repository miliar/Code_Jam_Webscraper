#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>
#include <ctime>
#include <climits>
#include <iomanip>
#include <sstream>
using namespace std;

typedef long long LL;
#define tr(container, it)for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = (a); i < (int)(b); i++)

int GCD (int a, int b) { if (!a) return b; return GCD(b%a, a);}

int main() {
    clock_t startTime = clock();
    ios_base::sync_with_stdio(false);

    int T; cin>>T;
    REP(test, 1, T+1) {
        cout<<"Case #"<<test<<": ";
        double c, f, x;
        cin>>c>>f>>x;
        double curCookie = 0., curTime = 0., curRate = 2.0;
        double timeToWin = x / curRate;
        while (1) {
            double nowTimeToWin = (x - curCookie)/curRate + curTime;
            if (nowTimeToWin - timeToWin > 1e-9) break;
            timeToWin = nowTimeToWin;
            double timeToBuyFarm = (c - curCookie)/curRate + curTime;
            curTime = timeToBuyFarm;
            curRate += f;
        }
        cout<<setprecision(9)<<fixed<<timeToWin<<"\n";
    }

    clock_t endTime = clock();
    cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
    return 0;
}

