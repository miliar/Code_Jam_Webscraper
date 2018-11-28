#include<iostream>
#include<fstream>
 
using namespace std;

void f(ifstream &in, ofstream &out, int c)
{
	int row1 = 0;
	in>>row1;
	row1--;

	int **a1 = new int*[4];
	for(int i = 0 ; i < 4; i++)
	{
		a1[i] = new int [4];
	}
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
		{
			in >> a1[i][j];
		}

	int row2 = 0;
	in>>row2;
	row2--;

	int **a2 = new int*[4];
	for(int i = 0 ; i < 4; i++)
	{
		a2[i] = new int [4];
	}
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
		{
			in >> a2[i][j];
		}

	int count = 0;
	int k = 0;
	int temp = 0;
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(a1[row1][i] == a2[row2][j]) 
			{
				count++;
				temp = a1[row1][i];
			}
		
			if(a1[row1][i] != a2[row2][j]) 
			{
				++k;
			}
		}
	}
	if(count == 1)
	{
		out << "Case #" << c << ": ";
		out << temp <<endl;
	}
	else
	{
		if(k == 16)
		{
			out << "Case #" << c << ": ";
			out << "Volunteer cheated!" <<endl;
		}
		else
		{
			out << "Case #" << c << ": ";
			out <<"Bad magician!"<<endl;
		}
	}

}

int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("out.txt");
	int count = 0;
	in>>count;
	for(int i = 0; i < count; i++)
	{
		int k = i + 1;
		f(in,out,k);
	}
	return 0;
}