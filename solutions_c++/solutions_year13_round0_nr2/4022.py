#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;


int main()
{

	int T;


    ifstream fin("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\B-large.in");

    //ifstream fin("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\test.txt");

     ofstream fout("C:\\weilin\\Competition\\codeForces\\CodeJam2013\\CodeJam2013\\output.txt");

	fin >> T;
	long long total = 0;
	
    int a[100][100];
	for (int i=0; i <T; i++)
	{
        int N, M;
        fin >> N >> M;
		for (int j=0; j < N; j++)
		{
			for (int m=0; m < M; m++)
			{
                int c;
                fin >> c;
                a[j][m] = c;
                
			}
		}
        int row[100]; int col[100];
        memset(row, 0, sizeof(row)); memset(col, 0, sizeof(col));

        for (int n=0; n < N; n++)
		{
           int max = 0;
           for (int m=0; m < M; m++)
		   {
              if (a[n][m] >  max)
                  max = a[n][m];
		   }
           for (int m=0; m < M; m++)
		   {
               if (a[n][m] < max)
			   {
                  if (col[m] == 0) {
                      col[m] = a[n][m];
                      for (int k=0; k < N; k++)
					  {
                          if (a[k][m]  > col[m])
                             {    
								 fout << "Case #" << i+1 <<  ": "<< "NO" << endl; 
								 goto nextcase;}
					  }
				  }
				  else if (col[m] != a[n][m])
				  {
                      {    
						  fout << "Case #" << i+1 <<  ": "<< "NO" << endl; goto nextcase;}
				  }
			   }
		   }
		}

        
        for (int m=0; m < M; m++)
		{
           int max = 0;
           for (int n=0; n < N; n++)
		   {
              if (a[n][m] > max)
                  max = a[n][m];
		   }
          

           for (int n=0; n < N; n++)
		   {
              if (a[n][m] < max)
			  {
                  if (row[n] == 0) {
                      row[n] = a[n][m];

                      for (int k=0; k < M; k++)
					  {
                          if (a[n][k]  > row[n])
                             {    
								 fout << "Case #" << i+1 <<  ": "<< "NO" << endl; 
								 goto nextcase;}
					  }
				  }
				  else if (row[n] != a[n][m])
				  {
                      {    
						  fout << "Case #" << i+1 <<  ": "<< "NO" << endl; goto nextcase;
					  }
				  }
			  }
		   }
		} 

        fout << "Case #" << i+1 <<  ": "<< "YES" << endl; 
nextcase:
        continue;
	}
	return 0;
} 