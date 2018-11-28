#include<bits/stdc++.h>

#define f(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define x first
#define y second
#define mp make_pair
#define pb push_back


using namespace std;

typedef pair<int,int> pii;

bool passable[110][510];
int xd[]={-1,0,1,0};
int yd[]={0,1,0,-1};
int w,h;
bool dfs(int xat,int yat,int pref)
{

	//cerr<<"AT "<<xat<<' '<<yat<<"\n";
	if(yat==h) return true;
	if(!passable[xat][yat]) return false;
	bool succ=false;
	passable[xat][yat]=false;
	for(int j=pref;j<4+pref;j++)
	{
		int i=(j+40000)&3;
		if(xat+xd[i]<0||yat+yd[i]<0||xat+xd[i]>=w) continue;
		succ=(succ||dfs(xat+xd[i],yat+yd[i],i-1));
		if(succ) break;
	}
	return succ;
}
int main()
{
	ifstream fin("C-small-attempt1.in");
	ofstream fout("C2.out");
	int cases;
	fin>>cases;
	for(int cas=1;cas<=cases;++cas)
	{
		fout<<"Case #"<<cas<<": ";
		int b;
		fin>>w>>h>>b;
		f(i,0,w)
		{
			f(j,0,h)
			{
				passable[i][j]=true;
			}
		}
		f(i,0,b)
		{
			int i0,j0,i1,j1;
			fin>>i0>>j0>>i1>>j1;
			f(i,i0,i1+1)
			{
				f(j,j0,j1+1)
				{
					//cerr<<i<<' '<<j<<'\n';
					passable[i][j]=false;
				}
			}
		}
		int ans=0;
		f(i,0,w)
		{
			//cerr<<"next\n";
			if(dfs(i,0,0)) ans++;
		}
		fout<<' '<<ans<<'\n';
	}
	return 0;
}
