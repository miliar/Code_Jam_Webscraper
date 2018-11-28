#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;
int number = 0;
void main()
{
	extern int number;
	int magic(int no1, int card1[4][4], int no2, int card2[4][4]);
	int num, i1, i2, i = 1, k;
	int a[4][4] , b[4][4] ;
	ifstream openfile("C:\\Users\\Gong\\Desktop\\A-small-attempt0.in", ios::in);
	ofstream writefile("C:\\Users\\Gong\\Desktop\\output.txt", ios::out);
	openfile >> num;
	while (i <= num)
	{
		openfile >> i1;
		for (int j = 0; j < 4;j++)
		for (int m = 0; m < 4; m++)
			openfile >> a[j][m];
		openfile >> i2;
		for (int j = 0; j < 4; j++)
		for (int m = 0; m < 4; m++)
			openfile >> b[j][m];
		k = magic(i1, a, i2, b);
		switch (k)
		{
		case 0: writefile << "Case #" << i << ": Volunteer cheated!" << endl; break;
		case 1: writefile << "Case #" << i << ": " << number << endl; break;
		default: writefile << "Case #" << i << ": Bad magician!" << endl; break;
		}
		i++;
	}
	system("pause");
}

int magic(int no1, int card1[4][4], int no2, int card2[4][4])
{
	extern int number;
	int i=0;
	int card[2][4];
	for (int j = 0; j < 4; j++)
	{
		card[0][j] = card1[no1-1][j];
		card[1][j] = card2[no2-1][j];
	}
	for (int j = 0; j < 4; j++)
	for (int k = 0; k < 4; k++)
	if (card[0][j] == card[1][k]) 
	{   
		i++;
		number = card[0][j];
	}
	return i;
}