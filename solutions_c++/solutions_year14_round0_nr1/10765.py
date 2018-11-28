#include<iostream>
#include<fstream>
using namespace std;
main()
{
	ifstream fin("A-small-attempt.in");
	ofstream fout("output3.txt");
	int testcases;
	fin >> testcases;
	for(int c=1; c<=testcases; c++)
	{
		int row;
		fin >> row;
		int array[4][4];
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
			fin >> array[i][j];
		int row2;
		fin >> row2;
		int array2[4][4];
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
			fin >> array2[i][j];
	   
	   
	   int card , count = 0;
	  for(int i=0; i<4; i++)
	  {
		 for(int j=0; j<4; j++)
		 {
		    if(array[row-1][i] == array2[row2-1][j])
		    { 
		      card = array[row-1][i];
			  count++;
		    }	
		 }
	  }
	  if(count == 0)
	   fout << "Case #" << c << ": Volunteer cheated!" << endl;
	  
	  else if(count > 1)
	   fout << "Case #" << c << ": Bad magician!" << endl;
	  
	  else if(count == 1)
	   fout << "Case #" << c << ": " << card << endl;  
	}
	
	fin.close();
	fout.close();
}
