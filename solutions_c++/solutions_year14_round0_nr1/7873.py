#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int rows = 4;
const int columns = 4;
int main()
{
	int cases;
	cin>> cases;
	int t = 1;
	int firstAns,secAns;
	int ** matrix = (int**)new int*[rows];
	int i,j;
	for( i = 0; i<rows; i ++ )
		matrix[i]= new int[columns];
	int res;
	int resCnt;
	vector<int>v(columns);
	while( t<= cases)
	{
		v.clear ();
		res = -1;
		resCnt = 0;
		cin>> firstAns;
		for(  i = 0; i< rows; i ++)
			for(  j = 0; j < columns; j ++)
			{
				cin>> matrix[i][j];
				if(i == firstAns -1)
					v.push_back (matrix[i][j]);
			}
		cin>> secAns;
		for(  i = 0; i< rows; i ++)
			for(  j = 0; j < columns; j ++)
			{
				cin>> matrix[i][j];
			}
		for( i = 0; i < columns; i++)
			for( j = 0; j < columns;j++)
			{
				if(v[i] == matrix[secAns-1][j])
				{
					res = v[i];
					resCnt++;
				}
				
			}
		if(resCnt==1)
			cout<< "Case #"<<t<<": "<< res<<endl;
		else if(resCnt > 1)
			cout<< "Case #"<<t<<": "<<"Bad magician!"<<endl;
		else
			cout<< "Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
		t++;
	}

	for( i = 0; i < columns; i++)
		delete []matrix[i];
	delete []matrix;

	return 0;

}