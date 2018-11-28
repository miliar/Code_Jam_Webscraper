#include<iostream>
#include<fstream>
using namespace std;
int num, result;
char s[4];
int wonx[4][4];
int wono[4][4];
int judge()  //1 ---X   2  ----0  3 ---draw   4---game
{
	int n1 =0,n2=0, n3=0,n4=0;
	for(int i = 0; i<4; i++ )
	{
		n1=0, n2=0, n3=0, n4=0;
		for( int j = 0; j <4; j++ )
		{
			n1+=wonx[i][j];
			n3+=wono[i][j];
			n2+=wonx[j][i];
			n4+=wono[j][i];
		}
		if( n1 == 4 || n2 == 4 )
			return 1;
		if(n3 ==0 || n4== 0 )
			return 2;
	}
	n1=0, n2=0, n3=0, n4=0;
	for( int y= 0; y<4; y++ )
	{
		n1+=wonx[y][y];
		n2+=wonx[3-y][y];
		n3+=wono[y][y];
		n4+=wono[3-y][y];
		
	}
	if( n1 == 4 || n2 ==4  )
			return 1;
	if(n3 ==0  || n4 == 0)
			return 2;
	for( int i=0; i<4; i++ )
	{
		for( int j =0; j<4; j++)
		{
			if( wonx[i][j] == 5 )
				return 4;
		}
	}
	return 3;
}
int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> num;
	for( int p = 0 ; p < num; p++ )
	{
		for( int j =0 ; j<4; j++)
		{
			fin >> s;
			for ( int k=0; k <4; k++ )
			{
				if(s[k] == 'X')
				{
					wonx[j][k] = 1;
					wono[j][k] = 1;
				}
				if(s[k] == 'O')
				{
					wonx[j][k] =0 ;
					wono[j][k] =0;
				}
				if(s[k] == '.')
				{
					wonx[j][k] = 5;
					wono[j][k] = 5;
				}
				if( s[k] == 'T')
				{
					wonx[j][k] = 1;
					wono[j][k] = 0;
				}
			}
		}
		result = judge();
		if( result == 1)
			fout << "Case #" << p+1 << ": X won" << endl; 
		if( result == 2)
			fout << "Case #" << p+1 << ": O won" << endl; 
		if( result == 3)
			fout << "Case #" << p+1 << ": Draw" << endl; 
		if( result == 4)
			fout << "Case #" << p+1 << ": Game has not completed" << endl; 
		
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}
