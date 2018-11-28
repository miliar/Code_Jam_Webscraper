/************************************************************************
* Problem ID: 
*************************************************************************
*  Rahul Kushwaha
*************************************************************************
* Additional Information [Bookname , Links, etc.]
*
*************************************************************************/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <ctime>
#include <string.h>

#define FOR(X) for(int i=0; i<(X);i++)
#define FOR_R(X) for( int i= (X);i>0;i--)
#define MAX(X,Y) (X) > (Y) ? (X) : (Y)
#define MIN(X,Y) (X) < (Y) ? (X) : (Y)
#define SWAP_XOR(X,Y) (X)=(X)^(Y);(Y)=(X)^(Y);X=(X)^(Y);
#define SWAP(X,Y) { int temp = (X); (X)= (Y); (Y) = temp;}

typedef long long LL;
typedef long double LD;

const int oSum4 = 4 * 'O' ;
const int oSum3 = 3 * 'O' +  'T';
const int xSum4 = 4 * 'X' ;
const int xSum3 = 3 * 'X' + 'T';

using namespace std;
int matrix[4][4];

void CheckWinner(int testCase, bool incomplete)
{
	int row0 = 	    matrix[0][0] + matrix[0][1] + matrix[0][2] + matrix[0][3];
	int row1 = 	    matrix[1][0] + matrix[1][1] + matrix[1][2] + matrix[1][3];
	int row2 = 	    matrix[2][0] + matrix[2][1] + matrix[2][2] + matrix[2][3];
	int row3 = 	    matrix[3][0] + matrix[3][1] + matrix[3][2] + matrix[3][3];

	int col0 = 	    matrix[0][0] + matrix[1][0] + matrix[2][0] + matrix[3][0];
	int col1 = 	    matrix[0][1] + matrix[1][1] + matrix[2][1] + matrix[3][1];
	int col2 = 	    matrix[0][2] + matrix[1][2] + matrix[2][2] + matrix[3][2];
	int col3 = 	    matrix[0][3] + matrix[1][3] + matrix[2][3] + matrix[3][3];

	int leftDiagonalSum = 	   matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3];
	int rightDiagonalSum = 	   matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0];

	if( row0 == oSum3 || row0 == oSum4 || col0 == oSum3 || col0 == oSum4 ||
		row1 == oSum3 || row1 == oSum4 || col1 == oSum3 || col1 == oSum4 ||
		row2 == oSum3 || row2 == oSum4 || col2 == oSum3 || col2 == oSum4 ||
		row3 == oSum3 || row3 == oSum4 || col3 == oSum3 || col3 == oSum4 ||
		leftDiagonalSum == oSum3 || leftDiagonalSum == oSum4 ||
		rightDiagonalSum == oSum3 || rightDiagonalSum == oSum4 )
		cout<<"Case #"<<testCase <<": "<<"O won";
	else if( col0 == xSum3 || col0 == xSum4 || row0 == xSum3 || row0 == xSum4 || 
			 col1 == xSum3 || col1 == xSum4 || row1 == xSum3 || row1 == xSum4 || 
			 col2 == xSum3 || col2 == xSum4 || row2 == xSum3 || row2 == xSum4 || 
			 col3 == xSum3 || col3 == xSum4 || row3 == xSum3 || row3 == xSum4 || 
		leftDiagonalSum == xSum3 || leftDiagonalSum == xSum4 ||
		rightDiagonalSum == xSum3 || rightDiagonalSum == xSum4 )
		cout<<"Case #"<<testCase <<": "<<"X won";
	else if(incomplete)
		cout<<"Case #"<<testCase <<": Game has not completed";
	else 	cout<<"Case #"<<testCase <<": Draw";
	cout<<endl;
}
int main()
{
	freopen("Input.txt", "r", stdin);
	freopen	("Output.txt", "w", stdout);
	int testCases;
	scanf("%d\n",&testCases);
	char temp;
	FOR(testCases)
	{
		bool flag = true;
		for(int j = 0; j< 4; j++)
		{
			for(int k = 0; k< 4; k++)
			{
				scanf("%c", &matrix[j][k]);
				if(flag)
				{
					if(matrix[j][k] == '.')
						flag = false;
				}
			}
			scanf("%c", &temp);
		}
		CheckWinner(i+1, !flag);
		scanf("%c", &temp);
	}
	fclose(stdin);
	fclose(stdout);
	return 0; 
}