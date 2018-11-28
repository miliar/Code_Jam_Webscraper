#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;


string trick ( int n1 , string*  arrange1[4] , int n2 , string* arrange2[4] )
{
  string s2 = "Volunteer cheated!";
	string s3 = "Bad magician!";
  string s1;

  int result,flag=0;
	for ( int i=0 ; i<4 ; i++ )
	{
		for ( int j=0 ; j<4 ; j++ )
		{
			if ( arrange1[n1-1][i] == arrange2[n2-1][j] )
			{
				s1 = arrange1[n1-1][i];
				flag++;
			}
		}
	}

 
	if ( flag == 1)
		return s1;
	else if ( flag > 1 )
		return s3;
	else
		return s2;

}

int main()
{
	ifstream input ("A-small-attempt1.in");
	ofstream output ("A-small-attempt1.out");
	int caseX;
	input>>caseX;

	int* n1 = new int[caseX];
	int* n2 = new int[caseX];


	string*** arrangements1 = new string** [caseX];
	for ( int i=0 ; i<caseX ; i++ )
		arrangements1[i] = new string* [4];
	for ( int i=0 ; i<caseX ; i++ )
		for ( int j=0 ; j<4 ; j++ )
			arrangements1[i][j] = new string [4];
	
	string*** arrangements2 = new string** [caseX];
	for ( int i=0 ; i<caseX ; i++ )
		arrangements2[i] = new string* [4];
	for ( int i=0 ; i<caseX ; i++ )
		for ( int j=0 ; j<4 ; j++ )
			arrangements2[i][j] = new string [4];

	for ( int i=0 ; i<caseX ; i++ )
	{
		input>>n1[i];
		
		for ( int j=0 ; j<4 ; j++ )
			for ( int k=0 ; k<4 ; k++ )
				input>>arrangements1[i][j][k];

		
		input>>n2[i];
		
		for ( int j=0 ; j<4 ; j++ )
			for ( int k=0 ; k<4 ; k++ )
				input>>arrangements2[i][j][k];
	}

	for ( int i=0 ; i<caseX ; i++ )
		{
	  output <<"Case #"<<i+1<<": ";
		string s = trick ( n1[i] , arrangements1[i] , n2[i] , arrangements2[i] );
		output<<s<<endl;
   }
		
	
	return 0;
}
