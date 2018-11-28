#include<bits/stdc++.h>

using namespace std;

const int MAXN = 100;

int n;
int cnt, ans;

int f[MAXN], g[MAXN];
int a[MAXN][MAXN];
int vis[MAXN], b[MAXN];
int fa[MAXN];
int fflag;

char s[MAXN];

void ddfs(int x){
	if (x > n){
		return ;
	}
	int p = b[x] - 1;
	int mmm = 0;
	for(int i = 0; i < n; i++)
		if (a[p][i] && !vis[i]){
			mmm = 1;
			vis[i] = 1;
			ddfs(x + 1);
			vis[i] = 0;
		}
//	cout<<"QAQ "<<x<<' '<<mmm<<endl;
	if (!mmm)
		fflag = 0;
}

char ch;

void dfs(int x, int y, int flag, int cnt){
	/*	for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++)
				cout<<a[i][j];
			cout<<endl;
		}
	cout<<x<<' '<<y<<' '<<flag<<' '<<cnt<<endl;*/
//	scanf("%c", &ch);
	if (x == 0 && y == 0 && flag != 0){
		for(int i = 1; i <= n; i++)
			b[i] = i;
		if (cnt > ans)
			return ;
		fflag = 1;
		do{
		//	for(int i = 1; i <= n; i++)
		//		cout<<b[i]<<' '; cout<<endl;
			for(int i = 0; i <= n; i++)
				vis[i] = 0;
			ddfs(1);
		//	cout<<flag<<endl;
			if (!fflag)
				break;
		}while(next_permutation(b + 1, b + n + 1));
		if (fflag){
		//	if (cnt == 1){
		/*		cout<<endl<<endl;
				for(int i = 0; i < n; i++){
					for(int j = 0; j < n; j++)
						cout<<a[i][j];
					cout<<endl;
				}*/
		//	}
			ans = min(ans, cnt);
		}
	}
	else{
	//	cout<<"QAQ "<<x<<' '<<y<<endl;
		int xx = x, yy = y + 1;
		if (yy == n){
			yy = 0, xx = (x+1) % n;
		}
	//	cout<<"TAT "<<xx<<' '<<yy<<endl;
		if (a[x][y] == 1){
			dfs(xx, yy, flag + 1, cnt);
		}
		else{
			dfs(xx, yy, flag + 1, cnt);
			a[x][y] = 1;
			dfs(xx, yy, flag + 1, cnt + 1);
			a[x][y] = 0;
		}
	}
}
/*
1
3
000
000
000
*/

int main(){
	freopen("Ds.in", "r", stdin);
	freopen("Ds.out", "w", stdout);

	int T;
	cin>>T;
	for(int o = 1; o <= T; o++){
		printf("Case #%d: ", o);
		cin>>n;
		for(int i = 0; i < n; i++){
			scanf("%s", s);
			for(int j = 0; j < n; j++)
				a[i][j] = (s[j] == '1');
		}
	/*	for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++)
				cout<<a[i][j];
			cout<<endl;
		}*/
		ans = n * n;
		dfs(0, 0, 0, 0);
		cout<<ans<<endl;
	}
	return 0;
}
