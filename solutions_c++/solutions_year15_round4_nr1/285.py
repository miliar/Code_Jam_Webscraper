#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int> pii;

int r,c;
pii grid[100][100];
pii dirs[4];

bool is_in(pii pos)
{ return pos.first >= 0 && pos.first < r && pos.second >= 0 && pos.second < c; }

bool is_ok(pii pos, pii dir)
{
  pos.first += dir.first;
  pos.second += dir.second;
  while(is_in(pos) && (grid[pos.first][pos.second]==make_pair(0,0)))
    {
      pos.first += dir.first;
      pos.second += dir.second;
    }
  return is_in(pos);
}

int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d: ",cas);
	// solution
	scanf("%d%d",&r,&c);
	dirs[0]=make_pair(0,-1);
	dirs[1]=make_pair(0,1);
	dirs[2]=make_pair(-1,0);
	dirs[3]=make_pair(1,0);
	for(int i=0;i<r;i++)
	  for(int j=0;j<c;j++)
	    {
	      //printf("%d %d\n",i,j);
	      char c=0;
	      while(c!='.' && c!='^' && c!='>' && c!='<' && c!='v')
		{
		  scanf("%c",&c);
		  //printf("%c\n",c);
		}
	      if(c=='.')
		grid[i][j]=make_pair(0,0);
	      if(c=='<')
		grid[i][j]=make_pair(0,-1);
	      if(c=='>')
		grid[i][j]=make_pair(0,1);
	      if(c=='^')
		grid[i][j]=make_pair(-1,0);
	      if(c=='v')
		grid[i][j]=make_pair(1,0);
	    }
	//printf("read done %d %d\n",r,c);
	int result=0;
	bool impo=false;
	for(int i=0;i<r;i++)
	  for(int j=0;j<c;j++)
	    if(grid[i][j]!=make_pair(0,0))
	      {
		//printf("test %d %d\n",i,j);
		if(is_ok(make_pair(i,j),grid[i][j]))
		  {
		    //printf("ok %d,%d\n",i,j);
		    continue;
		    
		  }
		bool passe=false;
		for(int k=0;k<4;k++)
		  if(is_ok(make_pair(i,j),dirs[k]))
		    passe=true;
		if(!passe)
		  impo=true;
		else
		  result++;
	      }
	if(impo)
	  printf("IMPOSSIBLE\n");
	else
	  printf("%d\n",result);
	      
	// end
    }
    return 0;
}
