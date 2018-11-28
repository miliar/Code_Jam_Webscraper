#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<set>
using namespace std;
int grid[2][4][4];
int n[2];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,cas=1;
    scanf(" %d",&T);
    while(T--){
          scanf(" %d",&n[0]);
          set<int> ss;
          for(int i=0;i<4;i++){
                  for(int j=0;j<4;j++){
                          scanf(" %d",&grid[0][i][j]);
                          if(i==n[0]-1) ss.insert(grid[0][i][j]);
                  }
                  
          }
          scanf(" %d",&n[1]);
          vector<int> ans;
          for(int i=0;i<4;i++){
                  for(int j=0;j<4;j++){
                          scanf(" %d",&grid[1][i][j]);
                          if(i==n[1]-1&&ss.find(grid[1][i][j])!=ss.end()){
                                       ans.push_back(grid[1][i][j]);
                          }
                  }
          }
          if(ans.empty()){
                          printf("Case #%d: Volunteer cheated!\n",cas++);
          }else if(ans.size()==1){
                          printf("Case #%d: %d\n",cas++,ans[0]);
          }else{
                          printf("Case #%d: Bad magician!\n",cas++);
          }
    }
    return 0;
}
/*
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
*/   
          
               
     
