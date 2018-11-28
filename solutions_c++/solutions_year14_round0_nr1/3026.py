#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef pair<int,int> ii;
typedef long long LL;
typedef vector <int> vi;

#define INF 2000000000
#define PI 3.14159265

#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,n) for(int i=a,_n=n; i<=_n; ++i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

#define ALL(v) (v).begin(), (v).end()

#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

int main()
{    
   freopen("a.in", "r", stdin);
   freopen("a.out", "w", stdout);     
   int tcase; scanf("%d", &tcase);
   
   REP (x, tcase) {
       int ans;
       int card[5][5];                     
       int possibleAns[5];
       int numAns = 0;
       int answerCard;
       
       scanf("%d", &ans);
       REP (i, 4) REP (j, 4) scanf("%d", &card[i][j]);             
       REP (i, 4) possibleAns[i] = card[ans-1][i];
       
       scanf("%d", &ans);
       REP (i, 4) REP (j, 4) scanf("%d", &card[i][j]);
       REP (i, 4) {
           int currentCard = card[ans-1][i];
           REP (j, 4) {    
               if ( possibleAns[j] == currentCard ) {
                  ++numAns;
                  answerCard = currentCard;
               }
           }    
       }
       
       printf("Case #%d: ", x+1);
       if ( numAns == 0 ) {
          puts("Volunteer cheated!");
       }
       else if ( numAns == 1 ) {
          printf("%d\n", answerCard);
       }
       else {
          puts("Bad magician!");            
       }
   }
   return 0;
}
