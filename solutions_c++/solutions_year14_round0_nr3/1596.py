#include <vector>
#include <iostream>
using namespace std;
bool dfs(vector<vector<char> > & ar, int x, int y, int num )
{
	if(num == 0) return true;
	else if (num < 0) return false;
	else{
		vector<int> neighbor;
		for(int i=-1; i <= 1; i ++)
		{
			for(int j =-1; j <=1 ;j ++)
			{
				if(i ==0 && j == 0) continue;
				else if( x+i < 0 || x+i >= ar.size() || y +j < 0 || y+j >= ar[0].size()) continue;
				else if(ar[x+i][y+j] == '*'){ 					
					neighbor.push_back(x+i);
					neighbor.push_back(y+j);
				}
			}
		}
		if(neighbor.size()/2 > num) return false;
		else{
			for(int i = 0;i < neighbor.size(); i += 2)
			{
				ar[neighbor[i]][neighbor[i+1]] = '.';
			}
			
			for(int i =0; i < neighbor.size(); i += 2)
			{
				if(dfs(ar, neighbor[i], neighbor[i+1], (num - neighbor.size()/2))) return true;				
			}
			for(int i = 0;i < neighbor.size(); i += 2)
			{
				ar[neighbor[i]][neighbor[i+1]] = '*';
			}
		}
	}
	return false;
}
void weep(int r, int c, int m)
{
	vector<vector<char> > ar(r, vector<char>(c, '*'));
	ar[0][0] ='c';
	int num = r*c - m -1;
	if(dfs(ar,0,0,num)){
		for(int i=0;i < r;i ++)
		{
			for(int j=0;j < c; j ++)
			{
				cout<<ar[i][j];
			}
			cout<<endl;
		}
	}else cout<<"Impossible"<<endl;
}
int main()
{

	int num;
	cin >>num;
	for(int i =1; i <= num; i ++)
	{
		int row, col, mine;
		cin >> row;
		cin >> col;
		cin >> mine;
		cout<<"Case #"<<i<<": "<<endl;
		weep( row,  col,  mine);
	}
	return 0;
}