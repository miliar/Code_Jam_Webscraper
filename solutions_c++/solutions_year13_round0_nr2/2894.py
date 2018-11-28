#include<iostream>
using namespace std;

int N, M;
int lawn[100][100];
bool accounted[100][100];

bool canCut()
{
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			accounted[i][j] = false;
	
	//All rows
	for(int i = 0; i < N; i++)
	{
		int max_h = -1;
		for(int j = 0; j < M; j++)
			max_h = max(max_h, lawn[i][j]);
		for(int j = 0; j < M; j++)
			if(max_h == lawn[i][j])
				accounted[i][j] = true;
	}
	
	//All columns
	for(int j = 0; j < M; j++)
	{
		int max_h = -1;
		for(int i = 0; i < N; i++)
			max_h = max(max_h, lawn[i][j]);
		for(int i = 0; i < N; i++)
			if(max_h == lawn[i][j])
				accounted[i][j] = true;
	}
	
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			if(!accounted[i][j])
				return false;
	return true;
}

int main()
{
	int cases;
	cin >> cases;
	
	for(int t = 1; t <= cases; t++)
	{
		cin >> N >> M;
		for(int i = 0; i < N; i++)
			for(int j = 0; j < M; j++)
				cin >> lawn[i][j];
		cout << "Case #" << t << ": ";
		if(canCut())
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	
	return 0;
}
