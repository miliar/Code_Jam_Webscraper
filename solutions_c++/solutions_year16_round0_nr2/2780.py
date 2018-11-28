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


#define oppo(x) (((x)=='+')?('-'):('+'))

char buf[101];
ll calc(int n, char g){
    int i=n-1;
    for (;i>=0&&buf[i]==g;--i);
    if (i==-1) return 0;
    return 1+calc(i+1, oppo(g));
}
int main()
{
    int TN;cin>>TN;
    for (int TI=1;TI<=TN;TI++){
        scanf("%s",buf);
        int n=char_traits<char>::length(buf);
        ll ans = calc(n,'+');
        printf("Case #%d: %d\n", TI, ans);
    }
    return 0;
}
