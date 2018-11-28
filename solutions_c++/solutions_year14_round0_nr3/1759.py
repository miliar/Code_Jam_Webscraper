#include<iostream>
#include<cstdio>
#include<cmath>
#include<queue>
#include<utility>

using namespace std;

#define ii pair<int, int>

int R, C, M, m, D;
char board[51][51];

void print(int a, int b)
{
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		if(i == a && j == b)
		cout<<'c';
		else
		cout<<board[i][j];
		cout<<endl;
	}
}
/*
void solve()
{
	int M, A, B, c, D;
	cin>>R>>C>>M;
	D = R*C - M;
	//cout<<D<<endl;
	if(D == 1)	print();
	else if(R == 1)
	{
		for(int i = 1; i < D; i++)
		board[0][i] = '.';
		print();
	}
	else if(C == 1)
	{
		for(int i = 1; i < D; i++)
		board[i][0] = '.';
		print();
	}
	else if(D == 2 || D == 3 || D == 5 || D == 7)
	cout<<"Impossible\n";
	else
	{
		int A = -1, B = -1, c = -1, L = min(R, C), H = max(R, C);
		for(int i = H; i >= 2; i--)
		{
			if(D%i != 1)
			if((D%i != 0 && D/i < L) || (D%i == 0 && D/i <= L))
			{
				A = i;
				B = D/i;
				c = D%i;
			}
		}
		if(A == -1)
		cout<<"Impossible\n";
		else
		{
			//cout<<A<<" "<<B<<" "<<c<<endl;
			for(int i = 0; i < A; i++)
			for(int j = 0; j < B; j++)
			if(R == H)
			{
				board[i][j] = '.';
			}
			else 
			{
				board[j][i] = '.';
			}
			
			for(int j = 0; j < c; j++)
			if(R == H)
			board[j][B] = '.';
			else
			board[B][j] = '.';
			
			board[0][0] = 'c';
			
			print();
		}
	}
}
*/
int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};
bool vis[51][51];
	
int solve3(ii top)
{
	if(m == D)
	return true;
	if(m > D)
	return false;
	
	vis[top.first][top.second] = true;
	
	vector<ii> localstack;
	for(int i = 0; i < 8; i++)
	{
		int x = top.first, y = top.second;
		for(int i = 0; i < 8; i++)
		{
			int x2 = x + dx[i], y2 = y + dy[i];
			if(x2 >= 0 && x2 < R && y2 >= 0 && y2 < C)
			{
				if(board[x2][y2] == '*')
				{
					board[x2][y2] = '.';
					localstack.push_back(ii(x2, y2));
					m++;
				}
			}
		}
	}
	
	for(int i = 0; i < R; i++)
	for(int j = 0; j < C; j++)
	{
		if(board[i][j] == '.' && !vis[i][j])
		if(solve3(ii(i, j))) return true;
	}
	
	for(int i = 0; i < localstack.size(); i++)
	{
		board[localstack[i].first][localstack[i].second] = '*';
		m--;
	}
	vis[top.first][top.second] = false;
	return false;
}
/*
void solve2()
{
	cin>>R>>C>>M;
	int D = R*C-M, m = 1;
	queue<ii> Q;
	board[0][0] = 'c';
	Q.push(ii(0, 0));
	while(!Q.empty())
	{
		if(m >= D)
		break;
		ii top = Q.front();
		Q.pop();
		int x = top.first, y = top.second;
		for(int i = 0; i < 8; i++)
		{
			int x2 = x + dx[i], y2 = y + dy[i];
			if(x2 >= 0 && x2 < R && y2 >= 0 && y2 < C)
			{
				if(board[x2][y2] == '*')
				{
					board[x2][y2] = '.';
					Q.push(ii(x2, y2));
					m++;
				}
			}
		}
	}
	if(m != D)
	cout<<"Impossible\n";
	else
	print();
}
*/
int main(void)
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T, t = 1;
	cin>>T;
	while(T--)
	{
		cout<<"Case #"<<t++<<":\n";
		for(int i = 0; i < 50; i++)
		for(int j = 0; j < 50; j++)
		{
			board[i][j] = '*';
			vis[i][j] = false;
		}
		cin>>R>>C>>M;
		m = 1; D = R*C - M;
		bool flag = false;
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				board[i][j] = '.';
				if(solve3(ii(i, j)))
				{
					flag = true;
					print(i, j);
					break;
				}
				else
				board[i][j] = '*';
			}
			if(flag) break;
		}
		
		if(!flag)
		cout<<"Impossible\n";
		
	}
	return 0;
}
