#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define pi acos(-1.0)
#define EPS 1e-9
#define mem(n,x) memset(n,x,sizeof(n))
typedef long long ll;

using namespace std;

bool grid[20][20];

int dx[4]={1,0,0,-1};
int dy[4]={0,1,-1,0};

int r,c;

bool valid(int x,int y){
	if(x<0 || y<0 || x>=r || y>=c)return 0;
	return 1;
}

int calc(){
	set<pair<pair<int,int>,pair<int,int> > > st;
	for(int i=0;i<r;++i){
		for(int j=0;j<c;++j){

			if(!grid[i][j])continue;
			for(int d=0;d<4;++d){
				int a=i+dx[d],b=j+dy[d];
				if(valid(a,b) && grid[a][b]){
					pair<int,int> x=mp(i,j),y=mp(a,b);
					st.insert(mp(min(x,y),max(x,y)));
				}
			}
		}
	}
	return st.size();
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);


	int t,cs=0;cin>>t;
	while(t--){
		int n;cin>>r>>c>>n;

		int x=r*c,ans=INT_MAX;
		for(int mask=0;mask<(1<<x);++mask){
			if(__builtin_popcount(mask)!=n)continue;

			mem(grid,0);
			int ind=0;
			for(int i=0;i<r;++i){
				for(int j=0;j<c;++j){
					if(mask & (1<<ind))grid[i][j]=1;
					++ind;
				}
			}

			ans=min(ans,calc());
		}

		cout<<"Case #"<<++cs<<": "<<ans<<"\n";
	}
	return 0;
}
