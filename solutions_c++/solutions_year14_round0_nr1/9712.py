#include <iostream>
#include <fstream>
using namespace std ;
main ()
{
	int m,n,c,d,a1[4][4],a2[4][4],ctr=0;
	ifstream fin ("A-small-attempt0.in");
	ofstream fout("out.txt");
	fin >> n;
	for (int i=0 ; i < n ; i++ )
	{
		fin >> c;
		for (int j =0; j< 4 ; j++)
		{
			for (int k =0; k< 4 ; k++)
				fin >> a1[j][k];
		}
		fin >> d;
		for (int j =0; j< 4 ; j++)
		{
			for (int k =0; k< 4 ; k++)
				fin >> a2[j][k];
		}
		
		for (int j=0 ; j < 4 ; j++ )
		{
				for (int k =0; k< 4 ; k++)
				{
					
						if (a1[c-1][j]==a2[d-1][k])
						{
							ctr++;
							m= a1[c-1][j];	
						}
				}
		}
		
		fout <<"Case #"<<i+1<<": ";
		
		if (ctr ==1)
		{
			fout <<m<<endl;
		}
		else if (ctr ==0)
		{
			fout <<"Volunteer cheated!"<<endl;
		}
		else if (ctr >1)
		{
			fout <<"Bad magician!"<<endl;
		}
		
		ctr=0;
		
	}
	
	
	
}
