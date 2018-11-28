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

int N;
ll P;

int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        cin >> N >> P;
        ll tot = (1LL<<N);
        
        ll y, z;
        ll a, b;
        
        a = 0, b = tot-1;
        while(a < b) {
            ll x = (a+b)/2;
            int wins=0;
            while(1) {
                if( (1LL<<wins) > tot-x ) break;
                wins++;
            }
            wins--;
            
            ll bestpos = tot-1;
            if(wins > 0) bestpos = (1LL << (N-wins)) - 1;
            
            //cout << x << " ---  " << bestpos << "   ---- " << wins << endl;
            
            if(bestpos < P) a = x+1;
            else b = x;
        }
        
        z = a-1;
        if(P == tot) z = tot-1;
        
        a = 0, b = tot-1;
        while(a < b) {
            ll x = (a+b)/2;
            int losses=0;
            while(1) {
                if( (1LL<<losses) > x+1 ) break;
                losses++;
            }
            losses--;
            
            ll worstpos = 0LL;
            REP(i, losses) {
                worstpos |= (1LL << (N-1-i));
            }
            
            if(losses == N) worstpos = tot-1;
            
            if(worstpos >= P) b = x;
            else a = x+1;
        }
        
        y = a-1;
        if(P == tot) y = tot-1;
        
        
        cout << "Case #" << caso+1 << ": " << y << " " << z << endl;
    }
}
