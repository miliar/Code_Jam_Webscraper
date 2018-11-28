#include <iostream>
#include <sstream>
#include <fstream>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in;
	in.open ("A-small-attempt0.in");
	
	ofstream out;
	out.open ("output.txt");
	
	int t;
	in >> t;
	
	int row1 = 0;
	int row2 = 0;
	int mat1[4];
	int mat2[4];
	int arr[4];
	
	int count = 0;
	int num = 0;
	
	for (int i=0; i<t; i++)
	{
		count = 0;
		
		/*-----------------------INPUT-------------------------*/
		in >> row1;
		
		for (int j=0; j<4; j++)
		{
			if (j == row1-1)
			{
				in >> mat1[0]; in >> mat1[1]; in >> mat1[2]; in >> mat1[3]; 
			}
			else
			{
				in >> arr[0]; in >> arr[1]; in >> arr[2]; in >> arr[3];
			}
		}
		
		in >> row2;
		
		for (int j=0; j<4; j++)
		{
			if (j == row2-1)
			{
				in >> mat2[0]; in >> mat2[1]; in >> mat2[2]; in >> mat2[3]; 
			}
			else
			{
				in >> arr[0]; in >> arr[1]; in >> arr[2]; in >> arr[3];
			}
		}
		/*----------------------------------------------------------------------*/
		
		out << "Case #" << i+1 << ": ";
		
		/*--------------------ALGO----------------------*/
		for (int j=0; j<4; j++)
		{
			for (int k=0; k<4; k++)
			{
				if (mat1[j] == mat2[k])
				{
					count++;
					num = mat1[j];
					break;
				}
			}
		}
		//cout << "count = " << count << " - ";
		if (count == 1)
			out << num << endl;
		if (count == 0)
			out << "Volunteer cheated!" << endl;
		if (count > 1)
			out << "Bad magician!" << endl;
			
		/*************************************************/
	}
	
	in.close();
	out.close();
	
	return 0;
}
