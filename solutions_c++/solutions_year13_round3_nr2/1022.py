using namespace std;
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;

struct st
{
	
	string str;
	int jump;
	int x,y;
	st(){;}
	st(int xx,int yy,int jj,string ss)
	{
		str=ss;
		x=xx;
		y=yy;
		jump=jj;
	}
}temp;

map <int, map<int,map <int,int> > > visited;
queue <st> q;
int dx,dy;

int check(int x,int y,int jump,string strr)
{
	
	if(visited[x][y][jump])return 0;
	visited[x][y][jump]=1;
	q.push(st(x,y,jump+1,strr));
}
	

string bfs()
{
	int x,y,jump;
	string str;

	
  while(!q.empty())
  {
	temp=q.front();q.pop();
	
	x=temp.x;
	y=temp.y;
	jump=temp.jump;
	str=temp.str;
	
	if(x==dx && y==dy)return str;
	
	check(x+(jump+1),y,jump,str+'E');
	check(x-(jump+1),y,jump,str+'W');
	check(x,y+(jump+1),jump,str+'N');
	check(x,y-(jump+1),jump,str+'S');
  }
}	
	
int main()
{
	int t,x,y,tt=1;
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	read(t);
	while(t--)
	{
		read(x);
		read(y);
		dx=x;
		dy=y;
		
		visited[0][0][0]=1;
		
		q.push(st(0,0,0,""));
		
        printf("Case #%d: ",tt++);
        cout<<bfs()<<endl;
		while(!q.empty())q.pop();
		visited.clear();
		
	}
//
}

