#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
using namespace std;
string a[200];
int n,m,c;
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
map<char,int> mp;
bool d[10],g;
int main() {
  int zz;
  cin>>zz;
  mp['^']=3;
  mp['v']=2;
  mp['<']=1;
  mp['>']=0;
  for (int zzz=1;zzz<=zz;zzz++) {
    cin>>n>>m;
    c=0;
    for(int i=0;i<n;i++)
      cin>>a[i];
    g=true;
    for(int i=0;i<n;i++) {
      for(int j=0;j<m;j++) {
        if (a[i][j]!='.') {
          memset(d,0,sizeof(d));
          //printf("%d %d\n",i,j);
          for(int k=0;k<4;k++) {
            int x=i+dx[k];
            int y=j+dy[k];
            while(x<n&&x>=0&&y<m&&y>=0) {
              //printf("%d %d\n",x,y);
              if (a[x][y]!='.') {
                d[k]=true;
                break;
              }
              x+=dx[k];
              y+=dy[k];
            }
          }
          int t=mp[a[i][j]];
          if (d[t]!=true) {
            c++;
          }
          //printf("%d %d ",i,j);
          /*for (int k=0;k<4;k++)
            printf("%d ",d[k]);
          printf("\n");*/
          if (d[0]==d[1]&&d[1]==d[2]&&d[2]==d[3]&&d[3]==false)
            g=false;
        }
      }
    }
    printf("Case #%d: ",zzz);
    if (g)
      printf("%d\n", c);
    else
      cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
