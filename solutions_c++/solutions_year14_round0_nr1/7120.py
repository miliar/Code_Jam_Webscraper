#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int casenum=1,row1,row2,n,t;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		int times=0;
		cin >> row1;
		row1--;
		int board1 [4][4];
		int board2 [4][4];
		for (int i = 0; i < 4; ++i)
		{
			int q,w,e,r;
			cin >> q >> w >> e >> r;
			board1[i][0]=q;
			board1[i][1]=w;
			board1[i][2]=e;
			board1[i][3]=r;
		}
		cin >> row2;
		row2--;
		for (int i = 0; i < 4; ++i)
		{
			int q,w,e,r;
			cin >> q >> w >> e >> r;
			board2[i][0]=q;
			board2[i][1]=w;
			board2[i][2]=e;
			board2[i][3]=r;
		}
		int rowq[4];
		int roww[4];
		for (int i = 0; i < 4; ++i)
		{
			rowq[i]=board1[row1][i];
			roww[i]=board2[row2][i];
		}
		for (int m = 0; m < 4; ++m)
		{
			for (int i = 0; i < 4; ++i)
			{
				if(roww[m]==rowq[i]){
					times++;
					t = roww[m];
				}
			}
		}
		if(times==1){
			cout <<"Case #" << casenum << ": " << t << endl;
		}
		else if(times>1){
			cout <<"Case #" << casenum << ": Bad magician!" << endl;
		}
		else{
			cout <<"Case #" << casenum << ": Volunteer cheated!" << endl;
		}
		casenum++;

	}
}