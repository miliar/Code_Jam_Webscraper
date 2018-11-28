#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <limits.h>
//#include <sys/time.h>
//#include <time.h>
using namespace std;
#define ll long long
const int cent=1500;

int visited[cent*2][cent*2];
int dx[4]={1,0,-1,0};
int dy[4]={0,-1,0,1};
queue <vector <char> > path;
vector <char> result;
int X,Y;
#if 0
int dfs(int x,int y,int dep){
cout<<x<<";"<<y<<endl;
	if(x==X&&y==Y){
		result=path;
		done=true;
		return 0;
	}
	if(dep==499)return 0;
	for(int i=0;i<4;++i){
		int nx=x+dx[i]*dep;
		int ny=y+dy[i]*dep;
		
		if(nx<0||nx>=2000||ny<0||ny>=2000)continue;
		if(visited[nx][ny])continue;
		if(i==0){
			path.push_back('E');
		}else if(i==1){
			path.push_back('S');
		}else if(i==2){
			path.push_back('W');
		}else{
			path.push_back('N');
		}
		dfs(nx,ny,dep+1);
		if(done)return 0;

		path.pop_back();	
	}
}
#endif
int main(void)
{
	int T;
	cin>>T;
	for(int _t=1;_t<=T;++_t)
	
	{
		bool done=false;
		result.clear();
		while(!path.empty())path.pop();
		cin>>X>>Y;
		X+=cent;
		Y+=cent;
		memset(visited,0,sizeof(visited));
	//	dfs(cent,cent,1);
		queue <int> x,y,n;
		vector <char> emp;
		path.push(emp);
		x.push(cent);
		y.push(cent);
		n.push(1);
		visited[cent][cent]=1;
		while(!x.empty()){
			int xx=x.front();
			int yy=y.front();
			int nn=n.front();
			x.pop();
			y.pop();
			n.pop();
			vector <char> tmp=path.front();
			path.pop();

			bool done=false;
			for(int i=0;i<4;++i){
				vector <char> nxt=tmp;
				int nx=xx+dx[i]*nn;
				int ny=yy+dy[i]*nn;
			
				if(nx<0||nx>=cent*2||ny<0||ny>=cent*2)continue;
				if(visited[nx][ny])continue;
				if(i==0){
					nxt.push_back('E');
				}else if(i==1){
					nxt.push_back('S');
				}else if(i==2){
					nxt.push_back('W');
				}else{
					nxt.push_back('N');
				}
				
				if(nx==X&&ny==Y){
				//	cout<<nx<<";"<<ny<<endl;
					done =true;
					result=nxt;
					break;
				}	
				if(nn+1>500)continue;
				visited[nx][ny]=1;
				x.push(nx);
				y.push(ny);
				n.push(nn+1);
				path.push(nxt);
			}
		
			if(done)break;

		}

		cout<<"Case #"<<_t<<": ";//
		for(int i=0;i<result.size();++i)cout<<result[i];
		cout<<endl;
		cerr<<"cerr:"<<_t<<";"<<result.size()<<endl;
	}

}


//	cout.setf(ios::fixed);

