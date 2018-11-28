#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list> 
#include <numeric>
#include <regex.h>  
#include <algorithm>
using namespace std; 
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs;
#define pb push_back 
#define sz(v) ((int)(v).size()) 
 
int K, N; 

map<int, int> dp_keysets[1<<20];
vi dp_sols[1<<20];

 
int main()
{
  int i=0,j=0,k=0; char buf[100000]="";

  int run,runs;
  scanf("%d",&runs);

  for(run=1;run<=runs;run++) {  
    int to_open[20];
    vi keys_in[20];
    scanf("%d %d",&K, &N);

    for(i=0;i<(1<<N);i++) {
      dp_keysets[i].clear();
      dp_sols[i].clear();
    }

    for(k=0;k<K;k++) { scanf("%d",&j); dp_keysets[0][j]++; }

    for(j=0;j<N;j++) {
      int ki;
      scanf("%d %d", &to_open[j], &ki);
      for(i=0;i<ki;i++) {
        scanf("%d",&k);
        keys_in[j].pb(k);
      }
    }


    
    for(int s=0;s<(1<<N);s++) {
      if(s==0||sz(dp_sols[s])>0) {
        for(int c=0;c<N;c++) if(!(s&(1<<c))) { //closed chest
          int needed = to_open[c];
//          printf("need key %d to open chest %d\n",needed,c);
          if(dp_keysets[s][needed]>0) { //we have it
            vi wouldbe = dp_sols[s]; wouldbe.pb(c);
            int s2 = s|(1<<c);
            if(sz(dp_sols[s2])==0||wouldbe<dp_sols[s2]) {
              dp_sols[s2]=wouldbe;
              dp_keysets[s2]=dp_keysets[s];
              dp_keysets[s2][needed]--;
              for(i=0;i<sz(keys_in[c]);i++) {
                dp_keysets[s2][keys_in[c][i]]++;
              }
            }
          }
        }
      }
    }

    printf("Case #%d:", run);
    int sss = (1<<N)-1;
    if(sz(dp_sols[sss])==0) {
      printf(" IMPOSSIBLE\n");
    } else {
      for(j=0;j<sz(dp_sols[sss]);j++) 
        printf(" %d",dp_sols[sss][j] + 1);
      printf("\n");
    }
  }



  return 0;
}
