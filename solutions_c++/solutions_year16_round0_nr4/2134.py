// template.cpp : Defines the entry point for the console application.
//
#include <climits>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <list>
#include <tuple>
#include <ctime>
#include <cassert>
using namespace std;


//type shortcuts
typedef long long ll;
typedef vector<ll> VI;
typedef long double DOUBLE;
typedef vector<DOUBLE> VD;
typedef vector<VD> VVD;


//constants
const DOUBLE EPS=1e-9;
const DOUBLE PI = atan(1) * 4;
const ll M = 1000000007;


ll K,C,S;
ll building=0;
ll bitcount=0;
void push(int x)
{
    building=building*K+x;
    bitcount++;
}

bool full() {
    return (bitcount==C);
}

ll getvalue() {
    return building;
}

void clean(){
    building = 0;
    bitcount = 0;
}

int main()
{
    int TN;cin>>TN;
    for (int TI=1;TI<=TN;TI++){
        cin>>K>>C>>S;
        if (S*C<K) {
            printf("Case #%d: IMPOSSIBLE\n", TI);
            continue;
        }
        cout<<"Case #"<<TI<<":";
        ll i=0;
        while (true) {
            push(i);
            if (full()) {
                cout<<" "<<(getvalue()+1);
                clean();
                if (i==K-1) break;
            }
            if (i<K-1) ++i;
        }
        cout<<endl;
    }
    return 0;
}
