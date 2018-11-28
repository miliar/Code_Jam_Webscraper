#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>

using namespace std;

#define LL long long
#define LD long double
#define ULL unsigned long long

#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))

int main(){
    int _T, __T;
    cin>>_T;
    __T = _T;
    while(_T--){
        cout<<"Case #"<<__T-_T<<": ";
        double c, f, x;
        cin>>c>>f>>x;
        double seconds = 0;
        double influx = 2;

        while( (c/influx) + x/(influx+f) < x/influx){
            seconds+= c/influx;
            influx+=f;
        }
        seconds+= x/influx;

        printf("%.7f", seconds);


        cout<<endl;
    }

    return 0;
}

