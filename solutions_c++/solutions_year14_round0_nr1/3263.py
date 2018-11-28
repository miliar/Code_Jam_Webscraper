#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;

vector<string> candidate;
#define MAX 17
#define BAD 18
#define CHEAT 0
#define SMALL

int solve(int (& grid1)[4][4],int row1,int(& grid2)[4][4],int row2){
	vector<bool> exist (MAX, false);
	for(int i = 0; i < 4; i++){
		exist[grid1[row1][i]] = true;
	}
	int result = 0;
	for(int i = 0; i < 4; i++){
		if(exist[grid2[row2][i]] && !result){
			result = grid2[row2][i];
		}
		else if(exist[grid2[row2][i]] && result){
			result = BAD;
			break;
		}
	}

	return result;
}

int main()
{
	#ifdef SMALL
		freopen("A-small-attempt0.in","rt",stdin);
		freopen("A-small-attempt0.out","wt",stdout);
	#endif
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		int grid1[4][4];
		int grid2[4][4];
		int row1,row2;
		scanf("%d", &row1);
		for(int i=0; i<4; i++)
			for(int j =0; j < 4; j++)
			{
				scanf("%d", &grid1[i][j]);
			}
		scanf("%d", &row2);
		for(int i=0; i<4; i++)
			for(int j =0; j < 4; j++)
			{
				scanf("%d", &grid2[i][j]);
			}

		printf("Case #%d: ", t);
		
		int result = solve(grid1,row1-1,grid2,row2-1);
		if(result && result <= 16)
			cout<<result<<endl;
		else if(result == BAD)
			cout<<"Bad magician!"<<endl;
		else if(result == CHEAT)
			cout<<"Volunteer cheated!" <<endl;
	}
}