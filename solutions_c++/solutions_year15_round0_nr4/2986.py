//Solved manually

#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

string table[4][4][4];

void fillTable()
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				table[i][j][k] = "0";
			}
		}
	}
	
	
	table[0][0][0] = "GABRIEL";
	table[0][0][1] = "RICHARD";
	table[0][0][2] = "RICHARD";
	table[0][0][3] = "RICHARD";
	
	table[0][1][0] = "GABRIEL";
	table[0][1][1] = "GABRIEL";
	table[0][1][2] = "RICHARD";
	table[0][1][3] = "RICHARD";
	
	table[0][2][0] = "GABRIEL";
	table[0][2][1] = "RICHARD";
	table[0][2][2] = "RICHARD";
	table[0][2][3] = "RICHARD";
	
	table[0][3][0] = "GABRIEL";
	table[0][3][1] = "GABRIEL";
	table[0][3][2] = "RICHARD";
	table[0][3][3] = "RICHARD";
	
	table[1][1][0] = "GABRIEL";
	table[1][1][1] = "GABRIEL";
	table[1][1][2] = "RICHARD";
	table[1][1][3] = "RICHARD";
	
	table[1][2][0] = "GABRIEL";
	table[1][2][1] = "GABRIEL";
	table[1][2][2] = "GABRIEL";
	table[1][2][3] = "RICHARD";
	
	table[1][3][0] = "GABRIEL";
	table[1][3][1] = "GABRIEL";
	table[1][3][2] = "RICHARD";
	table[1][3][3] = "RICHARD";
	
	table[2][2][0] = "GABRIEL";
	table[2][2][1] = "RICHARD";
	table[2][2][2] = "GABRIEL";
	table[2][2][3] = "RICHARD";
	
	table[2][3][0] = "GABRIEL";
	table[2][3][1] = "GABRIEL";
	table[2][3][2] = "GABRIEL";
	table[2][3][3] = "GABRIEL";
	
	table[3][3][0] = "GABRIEL";
	table[3][3][1] = "GABRIEL";
	table[3][3][2] = "RICHARD";
	table[3][3][3] = "GABRIEL";
}

int main()
{
    int T;
	cin>>T;
	fillTable();
	string result[T];
    for(int i=0; i<T; i++)
    {
		int X, R, C;
		cin >> X >> R >> C;
		if(table[R-1][C-1][X-1] == "0") result[i] = table[C-1][R-1][X-1];
		else result[i] = table[R-1][C-1][X-1];
    }
    
    for(int i=0; i<T; i++)
    {
    	cout<<"Case #" << i+1<< ": "<<result[i]<<endl;
    }
}
