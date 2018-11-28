#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");
#define cin fin
#define cout fout

vector<int> box[30];
int need[30];
int now[1100000][30];
int res[1100000];
int dp[1100000];
int vis[1100000];
int op[30];
int n,k,t=26;
vector<int> v;

bool work()
{
	int opened=0;
	for(int i=0;i<n;i++){
		opened+=op[i]<<i;
	}
	if(opened==(1<<(n))-1){
		vis[opened]=1;
		res[opened]=1;
		return true;
	}
	if(vis[opened]) return res[opened];
	vis[opened]=1;
	for(int i=n-1;i>=0;i--){
		if(!op[i] && now[opened][need[i]]){
			if(!vis[opened+(1<<i)]){
				now[opened][need[i]]--;
				for(int j=0;j<box[i].size();j++)
					now[opened][box[i][j]]++;
				for(int j=0;j<t;j++)
					now[opened+(1<<i)][j]=now[opened][j];
				for(int j=0;j<box[i].size();j++)
					now[opened][box[i][j]]--;
				now[opened][need[i]]++;
			}
			op[i]=1;
			if(work()){
				res[opened]=1;
				dp[opened]=i;
			}
			op[i]=0;
		}
	}
	return res[opened];
}

int main()
{
	int nn;
	cin>>nn;
	for(int x=1;x<=nn;x++){
		for(int i=0;i<30;i++) box[i].clear();
		memset(now,0,sizeof now);
		memset(need,0,sizeof need);
		memset(op,0,sizeof op);
		memset(res,0,sizeof res);
		memset(vis,0,sizeof vis);
		memset(dp,0,sizeof dp);
		v.clear();
		int m;
		cin>>m>>n;
		for(int i=0;i<m;i++){
			int tmp;cin>>tmp;now[0][tmp]++;
		}
		for(int i=0;i<n;i++){
			cin>>need[i];
			int tmp;
			cin>>tmp;
			for(int j=0;j<tmp;j++){
				int tmp2;
				cin>>tmp2;box[i].push_back(tmp2);
			}
		}
		cout<<"Case #"<<x<<": ";
		bool can=work();
		if(can){
			int now=0;
			for(int i=1;i<n;i++){
				cout<<dp[now]+1<<' ';
				now+=1<<dp[now];
			}
			cout<<dp[now]+1<<endl;
		}
		if(!can) cout<<"IMPOSSIBLE"<<endl;
	}
}