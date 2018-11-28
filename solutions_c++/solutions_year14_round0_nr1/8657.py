#include<iostream>
#include<fstream>
using namespace std;
void main()
{
	ifstream in("A-small-attempt3.in");
	ofstream out("output.txt");
	int arr1[4][4];
	int arr2[4][4];
	int cases;
	in >> cases;
	in.ignore();
	for (int i = 0; i < cases; i++)
	{
		int rowA, rowB;
		in >> rowA;
		in.ignore();
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				in >> arr1[j][k];
				in.ignore();
			}
		}
		in >> rowB;
		in.ignore();
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				in >> arr2[j][k];
				in.ignore();
			}
		}
		int count = 0;
		int num1, num2;
		for (int n = 0; n < 4; n++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (arr1[rowA-1][n] == arr2[rowB-1][j])
				{
					count++;
					num1 = arr1[rowA-1][n];
				}
			}
		}
		if (count == 1)
		{
			num2 = num1;
		}
		out << "Case #" << i + 1 << ": ";
		if (count == 1)
		{
			out << num2 << "\n";
		}
		else if (count > 1)
		{
			out << "Bad magician!" << endl;
		}
		else if (count == 0){
			out << "Volunteer cheated!" << endl;
		}
	}
	in.close();
	out.close();
}