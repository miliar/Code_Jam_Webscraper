#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;


int main()
{
	int T;
	int row1, row2;
	ifstream f;
	ofstream f2;
	int i,j,k;
  	f.open ("A-small-attempt1.in");
	f2.open("A-small-attempt1.out");
	f>>T;
	int mat[4][4];
	int ans1[4];
	int ans2[4];
	int count;
	int output;
	//cout<<T<<endl;
	for( i= 0; i<T; i++ )
	{
		f>>row1;
		
		for( j=0; j< 4; j++ )
			for ( k=0; k<4; k++ )
				f>>mat[j][k];
		for( j=0; j<4; j++ )
			ans1[j] = mat[row1-1][j];
		
	
		f>>row2;
		for( j=0; j< 4; j++ )
			for ( k=0; k<4; k++ )
				f>>mat[j][k];
		for( j=0; j<4; j++ )
			ans2[j] = mat[row2-1][j];
		//now process the output
		count =0;
		for( j=0; j<4; j++ )
		{
			for( k=0; k<4; k++ )
			{
				if( ans1[j] == ans2[k] )
				{
					output = ans1[j];
					count++;
				}
			}
		}
		if( count ==1 )
			f2<<"Case #"<<(i+1)<<": "<<output<<endl;
		else if( count > 1 )
			f2<<"Case #"<<(i+1)<<": Bad magician!"<<endl;
		else
			f2<<"Case #"<<(i+1)<<": Volunteer cheated!"<<endl;

	}
		
	 	


  	f.close();
	f.close();
	//cin>>T;
	




	return 0;
}
