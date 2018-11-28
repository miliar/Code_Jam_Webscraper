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

const int MAX_N = 1100;

int T;

int N;

double naomi[MAX_N];
double ken[MAX_N];
bool usedken[MAX_N];

int main()
{
    freopen("/Users/tonynater/Tony/Computer/Xcode_repos/Miscellaneous/codejam2014/D-large.in", "r", stdin);
    freopen("/Users/tonynater/Tony/Computer/Xcode_repos/Miscellaneous/codejam2014/dwar.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> T;
    
    for(int t = 1; t <= T; t++)
    {
        cin >> N;
        
        for(int i = 0; i < N; i++)
            cin >> naomi[i];
        
        for(int i = 0; i < N; i++)
            cin >> ken[i];
        
        sort(naomi, naomi+N);
        sort(ken, ken+N);
        
        int nDWar = 0;
        for(int i = 0, idx = 0; i < N; i++)
            if(naomi[i] > ken[idx])
            {
                ++nDWar;
                ++idx;
            }
        
        int nWar = 0;
        memset(usedken, 0, sizeof(usedken));
        for(int i = 0; i < N; i++)
        {
            bool found = false;
            for(int j = 0; j < N; j++)
                if(!usedken[j] && ken[j] > naomi[i])
                {
                    usedken[j] = true;
                    found = true;
                    break;
                }
            
            if(!found) ++nWar;
        }
        
        cout << "Case #" << t << ": " << nDWar << ' ' << nWar << '\n';
    }
    
    return 0;
}