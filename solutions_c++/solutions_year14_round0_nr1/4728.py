#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main(void)
{
	int n;
	scanf("%d",&n);
	vector<int> line(4,0);
	int a1, a2;
	vector< vector<int> > board(4,line);
	vector< vector<int> > board2(4,line);
	for(int i=1; i<=n; i++)
	{
		vector<int> can;
		scanf("%d",&a1);
		for(int row=0; row<4; row++)
			for(int col=0; col<4; col++)
				scanf("%d",&board[row][col]);
		scanf("%d",&a2);
		for(int row=0; row<4; row++)
			for(int col=0; col<4; col++)
				scanf("%d",&board2[row][col]);
		
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				if(board[a1-1][j]==board2[a2-1][k])
					can.push_back(board2[a2-1][k]);
					
		if(can.size()==1)
			cout<<"Case #"<<i<<": "<<can[0]<<endl;
		else if(can.size()>1)
			cout<<"Case #"<<i<<": Bad magician!"<<endl;
		else if(can.size()==0)
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
	}
}