//tonynater - Google Code Jam 2013

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <ctype.h>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <math.h>
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

const double pi = 3.141592653589793;
const double tau = 6.283185307179586;
const double epsilon = 1e-6;

const int MAX_N = 110;
const int MAX_M = 110;

int T;

int N, M;

int lawn[MAX_N][MAX_M];

bool mowedRow[MAX_N];
bool mowedColumn[MAX_M];
int minHeight;
bool findMow()
{
    minHeight = 100;
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++)
            if(!mowedRow[i] && !mowedColumn[j])
                minHeight = min(lawn[i][j], minHeight);
    
    for(int i = 0; i < N; i++)
        if(!mowedRow[i])
        {
            bool isSameHeight = true;
            for(int j = 0; j < M; j++)
                if(!mowedColumn[j])
                    if(lawn[i][j] != minHeight)
                        isSameHeight = false;
        
            if(isSameHeight) return (mowedRow[i] = true);
        }
    
    for(int i = 0; i < M; i++)
        if(!mowedColumn[i])
        {
            bool isSameHeight = true;
            for(int j = 0; j < N; j++)
                if(!mowedRow[j])
                    if(lawn[j][i] != minHeight)
                        isSameHeight = false;
            
            if(isSameHeight) return (mowedColumn[i] = true);
        }
    
    return false;
}


int main (int argc, const char * argv[])
{
    freopen("/Users/tonynater/Downloads/B-large.in", "r", stdin);
    freopen("/Users/tonynater/Tony/Computer/Xcode_repos/Miscellaneous/codejam2013/output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> T;
    
    for(int t = 1; t <= T; t++)
    {
        cin >> N >> M;
        
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                cin >> lawn[i][j];
        
        fill_n(mowedRow, MAX_N, false);
        fill_n(mowedColumn, MAX_M, false);
        
        while(findMow());
        
        cout << "Case #" << t << ": ";
        
        if(minHeight == 100) cout << "YES\n";
        else cout << "NO\n";
    }
    
    return 0;
}