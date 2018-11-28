#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define For(i,N) for(int i=0; i<N; i++)
#define FOR(i,j,k) for(int i=j; i<k; i++)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

using namespace std;

typedef long long ll;
typedef long double ld;

void solve(){
    int n, all=0;
    scanf("%d", &n);
    
    priority_queue<pair<int, int> > Q;
    for(int i=0; i<n; i++){
        int pi;
        scanf(" %d", &pi);
        Q.push(mp(pi, i));
        all += pi;
    }

    while(!Q.empty()){
        pair<int, int> party1 = Q.top(); Q.pop();
        party1.ff--;
        all--;
        printf(" %c", char('A' + party1.ss));

        if (!Q.empty() && Q.top().ff > all/2){
            pair<int, int> party2 = Q.top(); Q.pop();
            party2.ff--;
            all--;
            printf("%c", char('A' + party2.ss));
            if (party2.ff != 0)
                Q.push(party2);
        }

        if (party1.ff != 0)
            Q.push(party1);
    }

    printf("\n");
}

int main(){
  int T;
  scanf(" %d", &T);
  For(t,T){
    printf("Case #%d:",t+1);
    solve();
  }
  return 0;
}