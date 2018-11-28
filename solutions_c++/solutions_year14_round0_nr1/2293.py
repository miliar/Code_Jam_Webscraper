#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int x[5][5]{};
	int y[5][5]{};
	//int **x=p;
	//int **y=q;
	int iter;
	cin >> iter;
	int iterr=0;
	while(++iterr <= iter){
		int row1,row2;
		cin >> row1;
		row1--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> x[i][j];
		cin >> row2;
		row2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> y[i][j];
		int c=0;
		int num;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				 if(x[row1][i]==y[row2][j]){
					num = x[row1][i];
					c++;
				 }
		cout << "Case #" << iterr <<": ";
		switch(c){
		case 1:
			cout << num << endl;
			break;
		case 0:
			cout << "Volunteer cheated!" << endl;
			break;
		default:
			cout << "Bad magician!" << endl;
		}
	}
	getchar();

    return 0;
}
