#include<fstream>
#include<utility>
#include<queue>
#include<algorithm>
using namespace std;

int t,n,m;
int a[100][100];
queue<pair<int,int> >que;
pair<int,int>s[100];
ifstream fin("input.in");
ofstream fout("output.out");

bool comp(pair<int,int>x,pair<int,int>y){return a[x.first][x.second]<a[y.first][y.second];}

int main(){
	fin>>t;
	for(int k=1;k<=t;k++){
		while(!que.empty())que.pop();
		fout<<"Case #"<<k<<": ";
		fin>>n>>m;
		for(int i=0;i<n;i++)for(int j=0;j<m;j++){
			fin>>a[i][j];
			s[i*m+j]=make_pair(i,j);
		}
		sort(s,s+n*m,comp);
		for(int i=0;i<n*m;i++)que.push(s[i]);
		bool works=true;
		while(!que.empty()){
			int x=que.front().first;
			int y=que.front().second;
			que.pop();
			if(!a[x][y])continue;
			bool part=true;
			for(int i=0;i<m;i++)if(a[x][i]>a[x][y])part=false;
			if(part){
				for(int i=0;i<m;i++)a[x][i]=0;
				continue;
			}
			part=true;
			for(int i=0;i<n;i++)if(a[i][y]>a[x][y])part=false;
			if(part){
				for(int i=0;i<n;i++)a[i][y]=0;
				continue;
			}
			works=false;
			break;
		}
		fout<<(works?"YES\n":"NO\n");
	}
}