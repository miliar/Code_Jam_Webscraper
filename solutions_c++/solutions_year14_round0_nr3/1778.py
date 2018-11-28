#include <iostream>
#include <vector>

using namespace std;

vector<bool> click(int i, vector<int> pos, vector<bool> visited, int R, int C)
{
	if(visited[i])
		return visited;
	visited[i] = true;
	bool adjacent = true;
	for(int j=0; j<9; j++)
	{
		int a = (j%3)-1;
		int b = (j/3)-1;
		if(pos[i]%R+a >= 0 && pos[i]%R+a < R && pos[i]/R+b >= 0 && pos[i]/R+b < C && (a!=0 || b!=0))
		{
			int newI = pos[i]+a+R*b;
			bool empty = false;
			for(int k=0; k<pos.size(); k++)
			{
				empty |= pos[k]==newI;
			}
			adjacent &= empty;
		}
	}
	if(adjacent)
	{
		for(int j=0; j<9; j++)
		{
			int a = (j%3)-1;
			int b = (j/3)-1;
			if(pos[i]%R+a >= 0 && pos[i]%R+a < R && pos[i]/R+b >= 0 && pos[i]/R+b < C && (a!=0 || b!=0))
			{
				int newI = pos[i]+a+R*b;
				int k=0;
				while(k<pos.size())
				{
					if(pos[k]==newI)
						break;
					k += 1;
				}
				visited = click(k, pos, visited, R, C);
			}
		}
	}
	return visited;
}

bool check(vector<int> pos, int R, int C)
{
	bool valid = false;
	int i = 0;
	while(!valid && i<pos.size())
	{
		vector<bool> visited;
		for(int j=0; j<pos.size(); j++)
			visited.push_back(false);
		visited = click(i, pos, visited, R, C);
		valid = true;
		for(int j=0; j<pos.size(); j++)
			valid &= visited[j];
		i += 1;
	}
	if(valid)
	{
		i -= 1;
		for(int j=0; j<R; j++)
		{
			for(int k=0; k<C; k++)
			{
				int t=0;
				while(t<pos.size() && pos[t] != j+R*k)
					t+= 1;
				if(t<pos.size())
					cout << (t!=i ? "." : "c");
				else
					cout << "*";
			}
			cout << endl;
		}
	}
	return valid;
}

bool generate(int prev, int n, vector<int> pos, int R, int C)
{
	int i = prev+1;
	bool found = false;
	while(!found && i<R*C-n+1)
	{
		vector<int> tmp = pos;
		tmp.push_back(i);
		if(n==1)
			found = check(tmp, R, C);
		else
			found = generate(i, n-1, tmp, R, C);
		i += 1;
	}
	if(prev==-1 && !found)
		cout << "Impossible" << endl;
	return found;
}

int main()
{
	int T;
	cin >> T;
	for(int num=1; num<=T; num++)
	{
		cout << "Case #" << num << ":" << endl;
		int R, C, M;
		cin >> R >> C >> M;
		/*if((M <= R*C-R && (M+1)%R != 0) || (M <= R*C-C && (M+1)%C != 0) || M == R*C-1)
		{
			if(M <= R*C-R && (M+1)%R != 0)
			{
				for(int i=0; i<R; i++)
				{
					for(int j=0; j<C; j++)
					{
						if(i+R*j<M)
							cout << "*";
						else if(i==R-1 && j==C-1)
							cout << "c";
						else
							cout << ".";
					}
					cout << endl;
				}
			}
			else
			{
				for(int i=0; i<R; i++)
				{
					for(int j=0; j<C; j++)
					{
						if(j+C*i<M)
							cout << "*";
						else if(i==R-1 && j==C-1)
							cout << "c";
						else
							cout << ".";
					}
					cout << endl;
				}
			}
		}
		else*/
		{
			generate(-1, R*C-M, vector<int>(), R, C);
		}
	}
	return 0;
}
