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
using namespace std; 
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs;
#define pb push_back 
#define sz(v) ((int)(v).size()) 
 
int main()
{
  int i=0,j=0,k=0; char buf[100000]="";

  int run,runs;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++) {
    int N, M;
    scanf("%d %d",&N,&M);
    vvi veld(N, vi(M,0));
    vi rowmax(N,0), colmax(M,0);
    for(j=0;j<N;j++) {
      for(i=0;i<M;i++) {
        scanf("%d",&veld[j][i]);
        rowmax[j] = max(rowmax[j],veld[j][i]);
        colmax[i] = max(colmax[i],veld[j][i]);
      }
    } 

    bool isokay=true;
    for(j=0;j<N;j++)
      for(i=0;i<M;i++)
        if(veld[j][i]<rowmax[j] && veld[j][i]<colmax[i])
          isokay=false;
  
    printf("Case #%d: %s\n", run,isokay ? "YES":"NO");
  
  }






  return 0;
}
