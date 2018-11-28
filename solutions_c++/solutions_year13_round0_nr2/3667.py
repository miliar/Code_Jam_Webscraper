#include <iostream>
using namespace std;

int board[128][128];
int valid[128][128];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, n, m;
	cin>>T;
	memset(valid, -1, sizeof(valid));
	
	for(int tt = 0; tt < T; ++tt){
		cin>>n>>m;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				cin>>board[i][j];
		//for row
		for(int i = 0; i < n; ++i){
			int high = 1;
			for(int j = 0; j < m; ++j)
				if(board[i][j] > high)
					high = board[i][j];
			for(int j = 0; j < m; ++j)
				if(board[i][j] == high)
					valid[i][j] = tt;
		}
		//for colum
		for(int j = 0; j < m; ++j){
			int high = 1;
			for(int i = 0; i < n; ++i)
				if(board[i][j] > high)
					high = board[i][j];
			for(int i = 0; i < n; ++i)
				if(board[i][j] == high)
					valid[i][j] = tt;
		}
		
		int ans = 1;
		for(int i = 0; i < n; ++i)
			for(int j = 0; j < m; ++j)
				if(valid[i][j] != tt) ans = 0;
				
		cout<<"Case #"<<tt + 1<<": ";
		if(ans == 1)
			cout<<"YES"<<endl;
		else 
			cout<<"NO"<<endl;
		
	}
	return 0;
//	cout<<"hello world"<<endl;
//	system("pause");
} 
