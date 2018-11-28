#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <fstream>
#include <set>

using namespace std;

#define FOR(i, A, B) for(int i=(A); i<(B); i++)
#define REP(i, N) for(int i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define MP make_pair
#define PB push_back
#define VI vector<int>
#define VS vector<string>
#define PII pair<int, int>
#define X first
#define Y second

int aabs(int a) { return (a<0)?-a:a; }
int mmax(int a, int b) { return (a>b)?a:b; }
int mmin(int a, int b) { return (a<b)?a:b; }

#define ll long long

int N, M;
int sz;
pair< PII, int > arr[10100];

int calcCost(int a, int b) {
    int n = (b-a);
    return (N*(N+1) - (N-n)*(N-n+1))/2;
}

int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        cin >> N >> M;
        REP(i, M) {
            cin >> arr[i].X.X >> arr[i].X.Y >> arr[i].Y;
        }
        sz = M;
        
        int res = 0;
        while(1) {
            int best = 0, bi = 0, bj = 0;
            REP(i, sz) {
                FOR(j, i+1, sz) {
                    int oi = arr[i].X.X, ei = arr[i].X.Y;
                    int oj = arr[j].X.X, ej = arr[j].X.Y;
                    if( (oi >= oj and oi <= ej) or (oj >= oi and oj <= ei) ) {
                        
                        int cost1 = calcCost(oi, ei) + calcCost(oj, ej);
                        int cost2 = calcCost(oi, ej) + calcCost(oj, ei);
                        if(best < cost1-cost2) {
                            best = cost1-cost2;
                            bi = i;
                            bj = j;
                        }
                    }
                }
            }
            
            if(best <= 0) break;
            
            int p = mmin(arr[bi].Y, arr[bj].Y);
            
            arr[sz].X.X = arr[bi].X.X;
            arr[sz].X.Y = arr[bj].X.Y;
            arr[sz].Y = p;
            sz++;
            
            arr[sz].X.X = arr[bj].X.X;
            arr[sz].X.Y = arr[bi].X.Y;
            arr[sz].Y = p;
            sz++;
            
            arr[bi].Y -= p;
            if(arr[bi].Y == 0) swap(arr[bi], arr[sz-1]), sz--;
            
            arr[bj].Y -= p;
            if(arr[bj].Y == 0) swap(arr[bj], arr[sz-1]), sz--;
            
            res += best*p;
        }
        
        cout << "Case #" << caso+1 << ": " << res << endl;
    }
}
