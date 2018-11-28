#include<iostream>
#include<fstream>

using namespace std;

void main(int arg, char* argv[])
{
	
	ifstream fin;

	fin.open("A-small-attempt2.in", ios::in);

	ofstream fout("A-small-output.out", ios::out);

	if(fin && fout)
	{
		int T = 0 ;
		fin>>T;

		int total = 136, x1, x2;

		int cor_1, cor_2, j, k;

		int matrix_1[4][4], matrix_2[4][4];
	
		int count = 0 , col, row;

		for(int i = 0 ; i<T && (T>=1&&T<=1000) ; ++i)
		{
			fin>>cor_1;
			x1 = 0 ;
			for(j = 0 ; j<4 ; ++j)
			{
				for(k = 0 ; k<4 ; ++k)
				{
					fin>>matrix_1[j][k];
					x1 = x1 + matrix_1[j][k];
				}
			}

			x2 = 0;
			fin>>cor_2;
			for(j = 0 ; j<4 ; ++j)
			{
				for(k = 0 ; k<4 ; ++k)
				{
					fin>>matrix_2[j][k];
					x2 = x2 + matrix_2[j][k];
				}
			}

			count = 0 ;

			if(x1==136 && x2==136)
			{
				for(j = 0 ; j<4 ; ++j)
				{
					for(k = 0 ; k<4 ; ++k)
					{
						if(matrix_1[cor_1-1][j]==matrix_2[cor_2-1][k])
						{
							count++;
							row = cor_1-1;
							col = j;
						}
					}
				}
				fout<<"Case #"<<i+1<<": ";
				if(count==0)
				{
					fout<<"Volunteer cheated!";
				}
				else if(count>1){
					fout<<"Bad magician!";
				}
				else{
					fout<<matrix_1[row][col];
				}
				fout<<endl;
			}
		}
	}
	fout.close();
	fin.close();
}
