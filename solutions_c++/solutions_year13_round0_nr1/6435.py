
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <stdio.h>
//#include <conio.h>

using namespace std;
/*
int isp(string s) {
    int i = -1, j = s.length();
    while (i < j && s[++i] == s[--j]);
    return i >= j;
}


string convert (int val, int base)
{
	string x;
	do
	{
		x += "0123456789ABCDEFGHIJKLMNOPQRSTVWXYXZ"[val % base];
		val /=base;
	}
	while(val);
	return string(x.rbegin(),x.rend());
}*/

int main() 
{
	ifstream fin("A-large.in");
	ofstream fout ("output.out");
	int n,a,b;
	fin >> n;
	
	
	char c;
	
	for (int k  = 1; k  <= n; k ++)
	{
		int m [4][4];
		int blanco = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> c; 
				if(c == 'X')
					m[i][j] = 1;
				if(c == 'T')
					m[i][j] = 1000;
				if(c == 'O')
					m[i][j] = 10;
				if(c == '.')
				{
					m[i][j] = 0;
						blanco++;
				}
					
			}
		}
		string cad;
		getline(fin,cad);
		bool sw = false;
		if(  m[0][0]+m[0][1]+m[0][2]+m[0][3]==4 || m[0][0]+m[0][1]+m[0][2]+m[0][3]==1003 || m[1][0]+m[1][1]+m[1][2]+m[1][3]==4 || m[1][0]+m[1][1]+m[1][2]+m[1][3]==1003|| m[2][0]+m[2][1]+m[2][2]+m[2][3]==4 || m[2][0]+m[2][1]+m[2][2]+m[2][3]==1003 || m[3][0]+m[3][1]+m[3][2]+m[3][3]==4 || m[3][0]+m[3][1]+m[3][2]+m[3][3]==1003 
			|| m[0][0]+m[1][0]+m[2][0]+m[3][0]==4 || m[0][0]+m[1][0]+m[2][0]+m[3][0]==1003|| m[0][1]+m[1][1]+m[2][1]+m[3][1]==4  || m[0][1]+m[1][1]+m[2][1]+m[3][1]==1003  || m[0][2]+m[1][2]+m[2][2]+m[3][2]==4 || m[0][2]+m[1][2]+m[2][2]+m[3][2]==1003 || m[0][3]+m[1][3]+m[2][3]+m[3][3]==4 || m[0][3]+m[1][3]+m[2][3]+m[3][3]==1003
			|| m[0][0]+m[1][1]+m[2][2]+m[3][3]==4 || m[0][0]+m[1][1]+m[2][2]+m[3][3]==1003|| m[0][3]+m[1][2]+m[2][1]+m[3][0]==4 || m[0][3]+m[1][2]+m[2][1]+m[3][0]==1003)
		{
			fout<<"Case #" <<k<<": "<<"X won" <<endl;
			sw = true;

		}
	
		if(  m[0][0]+m[0][1]+m[0][2]+m[0][3]==40 || m[0][0]+m[0][1]+m[0][2]+m[0][3]==1030 || m[1][0]+m[1][1]+m[1][2]+m[1][3]==40 || m[1][0]+m[1][1]+m[1][2]+m[1][3]==1030|| m[2][0]+m[2][1]+m[2][2]+m[2][3]==40 || m[2][0]+m[2][1]+m[2][2]+m[2][3]==1030 || m[3][0]+m[3][1]+m[3][2]+m[3][3]==40 || m[3][0]+m[3][1]+m[3][2]+m[3][3]==1030 
			|| m[0][0]+m[1][0]+m[2][0]+m[3][0]==40 || m[0][0]+m[1][0]+m[2][0]+m[3][0]==1030|| m[0][1]+m[1][1]+m[2][1]+m[3][1]==40  || m[0][1]+m[1][1]+m[2][1]+m[3][1]==1030  || m[0][2]+m[1][2]+m[2][2]+m[3][2]==40 || m[0][2]+m[1][2]+m[2][2]+m[3][2]==1030 || m[0][3]+m[1][3]+m[2][3]+m[3][3]==40 || m[0][3]+m[1][3]+m[2][3]+m[3][3]==1030
			|| m[0][0]+m[1][1]+m[2][2]+m[3][3]==40 || m[0][0]+m[1][1]+m[2][2]+m[3][3]==1030|| m[0][3]+m[1][2]+m[2][1]+m[3][0]==40 || m[0][3]+m[1][2]+m[2][1]+m[3][0]==1030)
		{
			fout<<"Case #" <<k<<": "<<"O won" <<endl;
			sw = true;

		}
		
		if(!sw && blanco == 0)
			fout<<"Case #" <<k<<": "<<"Draw" <<endl;
		if(!sw && blanco != 0)
			fout<<"Case #" <<k<<": "<<"Game has not completed" <<endl;



		/*fin >> a >> b;
		int c = 0;
		for (int i = a; i <= b; i++)
		{
			if(isp(convert(i,10)))
			{
				
				double raiz = sqrt(i);
				if(raiz - (int )raiz == 0.0)
				{
					
					if(isp(convert(raiz,10)))
					{
						c++;
					}
				}

			}
		}
		fout<<"Case #" <<j<<": "<<c <<endl;
		//printf("Case #%d: %d\n",j,c);*/


	}
	//getch();
	
   
    
    return 0;
}