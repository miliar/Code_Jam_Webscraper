#include <bits/stdc++.h>
using namespace std;

int grid[32][32];
int n;

int main() {
  int t;cin>>t;for(int zz=1;zz<=t;zz++) {
    cin>>n;
    char c; for(int i=0;i<n;i++) for(int j=0;j<n;j++) cin>>c, grid[i][j]=c-'0';


    int ans=n*n+10000;
    for(int mask=1<<(n*n);--mask>=0;) {
      for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(mask&(1<<(i*n+j))) ++grid[i][j];

      int perm[]={0,1,2,3,4,5};
      do {
        int ass[]={0,1,2,3,4,5};
        do {
          for(int i=0;i<n;i++) {
            int ct=0;
            for(int j=0;j<n;j++) if(grid[perm[i]][j]) ++ct;
            for(int j=0;j<i;j++) if(grid[perm[i]][ass[perm[j]]]) --ct;
            if(!ct) goto die;
            if(!grid[perm[i]][ass[perm[i]]]) break;
          }
        } while(next_permutation(ass,ass+n));
      } while(next_permutation(perm,perm+n));

      //cout<<mask<<endl;
      ans=min(ans,__builtin_popcount(mask));
    die:
      for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(mask&(1<<(i*n+j))) --grid[i][j];
    }

    printf("Case #%d: %d\n",zz,ans);
  }
}
