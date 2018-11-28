//tonynater - CodeChef 2014

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define sz(x) ((int) x.size())

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const double pi = acos(-1);
const double tau = 2*pi;
const double epsilon = 1e-6;

int T;

ld C, F, X;

int main()
{
    freopen("/Users/tonynater/Tony/Computer/Xcode_repos/Miscellaneous/codejam2014/B-large.in", "r", stdin);
    freopen("/Users/tonynater/Tony/Computer/Xcode_repos/Miscellaneous/codejam2014/ccalpha.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> T;
    
    for(int t = 1; t <= T; t++)
    {
        cin >> C >> F >> X;
        
        double k = X/C - 1.0 - 2.0/F;
        int bound = ceil(k);
        if(bound < 0) bound = 0;
        
        ld time = 0.0;
        for(int i = 0; i < bound; i++)
            time += C/(2.0+ld(i)*F);
        time += X/(2.0+ld(bound)*F);
        
        cout << "Case #" << t << ": " << fixed << setprecision(9) << time << '\n';
    }
    
    return 0;
}