#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <iomanip>


using namespace std;

#define INFY 1000000000


int main() {
    cout.precision(10);
    freopen("/Users/arunamahesh/B-large.in","r",stdin);
    freopen("/Users/arunamahesh/GCJ_output.txt","w",stdout);
    int T; cin>>T;
    for(int t = 1;t <= T;t++) {
        double c,f,x;
        cin>>c>>f>>x;
        double best = INFY;
        double rate = 2;
        double timeTaken = 0;
        while(timeTaken + x / rate < best) {
            best = timeTaken + x / rate;
            timeTaken+= c/rate;
            rate+=f;
        }
        cout<<"Case #"<<t<<": "<<best<<endl;
    }
}