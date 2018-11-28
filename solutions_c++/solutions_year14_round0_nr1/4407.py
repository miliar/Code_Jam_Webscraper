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

const int MAX_R = 4;
const int MAX_C = 4;
const int N_CARDS = 16;

int T;

int R1, R2;

int cards1[MAX_R][MAX_C];
int cards2[MAX_R][MAX_C];

int main()
{
    freopen("/Users/tonynater/Downloads/A-small-attempt0.in", "r", stdin);
    freopen("/Users/tonynater/Tony/Computer/Xcode_repos/Miscellaneous/codejam2014/magictrick.out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> T;
    
    for(int t = 1; t <= T; t++)
    {
        cin >> R1;
        --R1;
        
        for(int i = 0; i < MAX_R; i++)
            for(int j = 0; j < MAX_C; j++)
                cin >> cards1[i][j];
        
        cin >> R2;
        --R2;
        
        for(int i = 0; i < MAX_R; i++)
            for(int j = 0; j < MAX_C; j++)
                cin >> cards2[i][j];
        
        int nPossible = 0, chosen = 0;
        for(int i = 1; i <= N_CARDS; i++)
        {
            bool found = false;
            for(int j = 0; j < MAX_C; j++)
                if(cards1[R1][j] == i)
                    found = true;
            
            if(!found) continue;
            
            found = false;
            for(int j = 0; j < MAX_C; j++)
                if(cards2[R2][j] == i)
                    found = true;
            
            if(!found) continue;
            
            ++nPossible;
            chosen = i;
        }
        
        cout << "Case #" << t << ": ";
        
        if(nPossible == 0) cout << "Volunteer cheated!\n";
        else if(nPossible == 1) cout << chosen << '\n';
        else cout << "Bad magician!\n";
    }
    
    return 0;
}