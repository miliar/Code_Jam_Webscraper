#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAXN 110
int map[MAXN][MAXN];
bool vis[MAXN][MAXN];
int height, width;

void openFile(){
  freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
}

struct Point{
  int x,y,w;
  bool operator<(const Point& p)const{
    return w < p.w;
  }
};
Point pts[MAXN*MAXN];

bool checkx(int x, int y){
  for(int i = 0; i < width; i++){
    if(!vis[i][y] && map[i][y] > map[x][y]){
      return false;
    }
  }
  return true;
}

void notex(int x, int y){
  for(int i = 0; i < width; i++)
    vis[i][y] = true;
}

bool checky(int x, int y){
  for(int i = 0; i < height; i++){
    if(!vis[x][i] && map[x][i] > map[x][y]){
      return false;
    }
  }
  return true;
}

void notey(int x, int y){
  for(int i = 0; i < height; i++)
    vis[x][i] = true;
}

int main(){
  openFile();
  int ncase;
  int n, c;
  int no = 0;
  scanf("%d", &ncase);

  while(ncase > no){
    no++;
    scanf("%d %d", &width, &height);
    memset(vis, false, sizeof(vis));
    for(int i = 0; i < width; i++){
      for(int j = 0; j < height; j++){
        scanf("%d", &map[i][j]);
        //printf("%d ", map[i][j]);
        int id = i * height + j;
        pts[id].x = i;
        pts[id].y = j;
        pts[id].w = map[i][j];
      }
      //printf("\n");
    }
    sort(pts, pts + width*height);

    int ret ;

    if(width == 1 || height == 1)
      printf("Case #%d: YES\n", no);
    else{
      int i ;
      for(i = 0; i < width*height; i++){
        int xx = pts[i].x;
        int yy = pts[i].y;
        if(vis[xx][yy])continue;
        if(checkx(xx, yy)) {
          notex(xx, yy);
          //printf("%d %d [%d] x\n", xx, yy, map[xx][yy]);
        }
        else if(checky(xx, yy)){
          notey(xx, yy);
          //printf("%d %d [%d] y\n", xx, yy, map[xx][yy]);
        }
        else {
          //printf("%d %d [%d] o\n", xx, yy, map[xx][yy]);
          break;
        }
      }
      if(i == width * height){
        printf("Case #%d: YES\n", no);
      }
      else{
        printf("Case #%d: NO\n", no);
      }
    }
  }
  return 0;
}
