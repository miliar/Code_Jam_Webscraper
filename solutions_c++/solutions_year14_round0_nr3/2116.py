#include<stdio.h>
#include<queue>
using namespace std;
char mtx[6][6];
char backup[6][6];
int row,col;
bool visit[6][6];
void init_mtx() {
  for(int i=1;i<=row;i++)
    for(int j=1;j<=col;j++) 
      mtx[i][j]='.';
}
void save_mtx() {
  for(int i=1;i<=row;i++)
    for(int j=1;j<=col;j++)
      backup[i][j]=mtx[i][j];
}
void recover_mtx() {
  for(int i=1;i<=row;i++)
    for(int j=1;j<=col;j++)
      mtx[i][j]=backup[i][j];
}
int count_mines(int x,int y) {
  int count = 0;
  if(x-1>=1) {
    if(mtx[x-1][y]=='*')
      {count++;visit[x-1][y]=true;}
  }
  if(x+1<=row) {
    if(mtx[x+1][y]=='*')
    {count++;visit[x+1][y]=true;}
  }
  if(y-1>=1) { 
    if(mtx[x][y-1]=='*')
      {count++;visit[x][y-1]=true;}
  }
  if(y+1<=col) {   
    if(mtx[x][y+1]=='*')
      {count++;visit[x][y+1]=true;}
  }
  if(x-1>=1&&y-1>=1) {
    if(mtx[x-1][y-1]=='*')
      {count++;visit[x-1][y-1]=true;}
  }
  if(x-1>=1&&y+1<=col) {   
    if(mtx[x-1][y+1]=='*')
      {count++;visit[x-1][y+1]=true;}
  }
  if(x+1<=row&&y-1>=1) {  
    if(mtx[x+1][y-1]=='*')
      {count++;visit[x+1][y-1]=true;}
  }
  if(x+1<=row&&y+1<=col) {
    if(mtx[x+1][y+1]=='*')
      {count++;visit[x+1][y+1]=true;}
  }
  return count;
}
bool judge_mtx() {
  int count = 0;
  for(int i=1;i<=row;i++)
    for(int j=1;j<=col;j++)
      if(mtx[i][j]=='.')
        count++;
  if(count == 0)
    return true;
  return false;
}
void push_around(int x,int y,queue<pair<int,int>> &q) {
  int count = 0;
  if(x-1>=1&&visit[x-1][y]==false) {
    visit[x-1][y]=true;
    count = count_mines(x-1,y);
    mtx[x-1][y] = '0'+count;
    q.push(make_pair(x-1,y));
  }
  if(x+1<=row&&visit[x+1][y]==false) {
    visit[x-1][y]=true;
    count = count_mines(x+1,y);
    mtx[x+1][y] = '0'+count;
    q.push(make_pair(x+1,y));
  }
  if(y-1>=1&&visit[x][y-1]==false) { 
    visit[x][y-1]=true;
    count = count_mines(x,y-1);
    mtx[x][y-1] = '0'+count;
    q.push(make_pair(x,y-1));
  }
  if(y+1<=col&&visit[x][y+1]==false) {   
    visit[x][y+1]=true;
    count = count_mines(x,y+1);
    mtx[x][y+1] = '0'+count;
    q.push(make_pair(x,y+1));
  }
  if(x-1>=1&&y-1>=1&&visit[x-1][y-1]==false) {
    visit[x-1][y-1]=true;
    count = count_mines(x-1,y-1);
    mtx[x-1][y-1] = '0'+count;
    q.push(make_pair(x-1,y-1));
  }
  if(x-1>=1&&y+1<=col&&visit[x-1][y+1]==false) {   
    visit[x-1][y+1]=true;
    count = count_mines(x-1,y+1);
    mtx[x-1][y+1] = '0'+count;
    q.push(make_pair(x-1,y+1));
  }
  if(x+1<=row&&y-1>=1&&visit[x+1][y-1]==false) {  
    visit[x+1][y-1]=true;
    count = count_mines(x+1,y-1);
    mtx[x+1][y-1] = '0'+count;
    q.push(make_pair(x+1,y-1));
  }
  if(x+1<=row&&y+1<=col&&visit[x+1][y+1]==false) {
    visit[x+1][y+1]=true;
    count = count_mines(x+1,y+1);
    mtx[x+1][y+1] = '0'+count;
    q.push(make_pair(x+1,y+1));
  }
}
bool solve_mtx() {
  save_mtx();
  queue<pair<int,int>> q;
  pair<int,int> cur;
  int count;
  for(int i=1;i<=row;i++)
    for(int j=1;j<=col;j++) {
      if(mtx[i][j]=='*')
        continue;
      recover_mtx();
      memset(visit,false,sizeof(visit));
      cur.first = i;cur.second = j;
      if(q.empty())
        mtx[i][j] = 'c';
      visit[i][j]=true;
      count = count_mines(i,j);
      q.push(cur);
      while(!q.empty()) {
        cur = q.front();q.pop();
        if(mtx[cur.first][cur.second]=='0'||count==0)
          push_around(cur.first,cur.second,q);
        count = -1;
      }
      if(judge_mtx())
        return true;
    }
  recover_mtx();
  return false;
}
void place_mine(int idx,char ch) {
  int r = (idx+col-1)/col;
  int c = idx%col;
  if(c==0)
    c=col;
  mtx[r][c]=ch;
}
bool place_mtx(int nmines,int nth,int idx) {
  if(nth==0)
  {mtx[1][1]='c';return true;}
  if(nmines == 0) {
    return solve_mtx();
  }
  for(int i=idx;i<=row*col-nmines+1;i++) {
    place_mine(i,'*');
    if(place_mtx(nmines-1,nth,i+1))
      return true;
    place_mine(i,'.');
  }
  return false;
}
void print_mtx() {
  for(int i=1;i<=row;i++) {
    for(int j=1;j<=col;j++) {
      if(mtx[i][j]!='*'&&mtx[i][j]!='c')
        mtx[i][j]='.';
      printf("%c",mtx[i][j]);
    }
    printf("\n");
  }
}
int main()
{
  freopen("C-small-attempt1.in","r",stdin);
  freopen("a.out","w",stdout);
  int T,nmines,begin;
  scanf("%d",&T);
  for(int t=1;t<=T;t++) {
    scanf("%d %d %d",&row,&col,&nmines);
    init_mtx();
    if(nmines==0)
      begin = 0;
    else 
      begin = 1;
    bool ret = place_mtx(nmines,begin,1);
    printf("Case #%d:\n",t);
    if(ret)
      print_mtx();
    else
      printf("Impossible\n");
  }
  return 0;
}