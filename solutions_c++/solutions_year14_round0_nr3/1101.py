#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 55;

const int N = 5;
char ans[N + 1][N + 1][N * N][N][N];
bool solved[N + 1][N + 1][N * N];
char mp[N][N],res[N][N];

int qx[N * N],qy[N * N];
bool vis[N][N];

bool check(int n,int m,int cnt)
{
  auto check_adjacent = [&] (int x,int y) -> bool
    {
      for(int i = -1; i <= 1; i++)
	for(int j = -1; j <= 1; j++)
	  {
	    const int nx = x + i,ny = y + j;
	    if (0 <= nx && nx < n && 0 <= ny && ny < m)
	      {
		if (mp[nx][ny] == '*') return false;
	      }
	  }
      return true;
    };

  int l = 0,r = 0;
  auto push = [&] (int nx,int ny)
    {
      vis[nx][ny] = true;
      qx[r] = nx,qy[r] = ny;
      r++;
    };

  auto add_queue = [&] (int x,int y)
    {
     for(int i = -1; i <= 1; i++)
	for(int j = -1; j <= 1; j++)
	  {
	    const int nx = x + i,ny = y + j;
	    if (0 <= nx && nx < n && 0 <= ny && ny < m && !vis[nx][ny])
	      {
		push(nx,ny);
	      }
	  }
    };

  memset(vis,false,sizeof(vis));

  int px,py;
  bool flag = true;

  for(int i = 0; i < n && flag; i++)
    for(int j = 0; j < m && flag; j++)
      {
	if (mp[i][j] == '.') px = i,py = j;
	if (check_adjacent(i,j))
	  {
	    push(i,j);
	    flag = false;
	  }
      }

  while(l < r)
    {
      if (check_adjacent(qx[l],qy[l]))
	{
	  add_queue(qx[l],qy[l]);
	}
      l++;
    }

  if (r == n * m - cnt || cnt == n * m - 1)
    {
      memcpy(res,mp,sizeof(res));
      res[px][py] = 'c';
      return true;
    }
  else return false;
}

void search(int n,int m,int i,int j,int cnt)
{
  if (j == m) 
    {
      i++;
      j = 0;

      if (i == n)
	{
	  if (cnt < n * m && !solved[n][m][cnt] && check(n,m,cnt))
	    {
	      solved[n][m][cnt] = true;
	      memcpy(ans[n][m][cnt],res,sizeof(res));
	    }
	  return ;
	}
    }
  mp[i][j] = '*';
  search(n,m,i,j + 1,cnt + 1);
  mp[i][j] = '.';
  search(n,m,i,j + 1,cnt);
}

void init()
{
  for(int i = 1; i <= 5; i++)
    for(int j = i; j <= 5; j++)
      search(i,j,0,0,0);
}

bool getAns(int n,int m,int k)
{
  if ( n > m ) swap(n,m);
  if (solved[n][m][k])
    {
      memcpy(res,ans[n][m][k],sizeof(res));
      return true;
    }
  else return false;
}

int main()
{
  init();

  int tcase;
  scanf("%d",&tcase);
  for(int tnum = 1; tnum <= tcase; tnum++)
    {
      int n,m,k;
      scanf("%d%d%d",&n,&m,&k);
   
      printf("Case #%d:\n",tnum);
      if (getAns(n,m,k))
	{
	  if (n < m) 
	    {
	      for(int i = 0; i < n; i++)
		{
		  for(int j = 0; j < m; j++)
		    putchar(res[i][j]);
		  putchar('\n');
		}
	    }
	  else
	    {
	      for(int i = 0; i < n; i++)
		{
		  for(int j = 0; j < m; j++)
		    putchar(res[j][i]);
		  putchar('\n');
		}
	    }
	}
      else puts("Impossible");
    }
  return 0;
}
