#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int lim,cnt,n,ans;

bool a[30][30],f[30];

vector<int> worker;

bool dfs2(int k,int d){
	if (d>=worker.size()) return 1;
	int v=worker[d];
	for (int i=1;i<=n;i++) if (i!=k && a[v][i]){
		if (!f[i]){
			f[i]=1;
			if (dfs2(k,d+1)) return 1;
			f[i]=0;
		}
	}
	return 0;
}

bool check(int k){
	for (int i=1;i<=n;i++) f[i]=0;
	return dfs2(k,0);
}

void dfs(int d){
	//cerr <<"depth : "<< d << endl;
	if (d>lim){
		for (int j=1;j<=n;j++){
			worker.clear();
			for (int i=1;i<=n;i++)
				if (a[i][j])
					worker.push_back(i);
			if (worker.size()==0) return;
			if (worker.size()==n) continue;
			if (check(j)) return; 
		}
		if (cnt<ans){
			ans=cnt;
		}
		return;
	}

	int i=(d-1)/n+1;
	int j=(d-1)%n+1;
	dfs(d+1);
	if (cnt<ans && !a[i][j]){
		cnt++;
		//cerr << "teach : "<<i<<","<<j<<endl;
		a[i][j]=1;
		dfs(d+1);
		cnt--;
		a[i][j]=0;
	}
}

int main(){
	int tt;
	cin>>tt;
	char x;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			getchar();
			for (int j=1;j<=n;j++){
				x=getchar();
				//cerr<<"read "<<i<<" "<<j<<" : "<<x<<endl;
				a[i][j]=(x=='1');
			}
		}
		lim=n*n;
		cnt=0;
		ans=n*n+1;
		dfs(1);
		cout << ans <<endl;
		
	}

	return 0;
}