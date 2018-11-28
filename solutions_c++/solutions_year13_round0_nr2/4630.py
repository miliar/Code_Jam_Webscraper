#include<iostream>
#include<vector>
using namespace std;

typedef pair<int,int> PII;

int a[105][105];
bool b[105][105];
int N,M;
vector<PII> V;

bool cmp(PII p,PII q){
	return a[p.first][p.second]<a[q.first][q.second];
}

void solve(){
	cin>>N>>M;
	V.clear();
	memset(b,false,sizeof(b));
	for (int i=0;i<N;i++)
		for (int j=0;j<M;j++) {
			cin>>a[i][j];
			V.push_back(make_pair(i,j));
		}
	sort(V.begin(),V.end(),cmp);
	for (int k=0;k<int(V.size());k++) {
		int x=V[k].first,y=V[k].second;
		for (int i=0;i<N;i++)
			for (int j=0;j<M;j++) 
				if (a[i][j]<=a[x][y]) b[i][j]=true;
		bool t1=true,t2=true;
		for (int i=0;i<N;i++) if (b[i][y]!=true) t1=false;
		for (int j=0;j<M;j++) if (b[x][j]!=true) t2=false;
		if (t1==false&&t2==false) {
			cout<<"NO\n";
			return ;
		}
	}
	cout<<"YES\n";
}

int main(){
	
	freopen("b-large.in","r",stdin);
	freopen("b-large.out","w",stdout);
	
	int T;
	cin>>T;
	for (int cs=1;cs<=T;cs++) {
		cout<<"Case #"<<cs<<": ";
		solve();
	}
	
	return 0;
}
