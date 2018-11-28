#include<fstream>
#include<iostream>
using namespace std;

int main ( ) 
{
	ifstream fin ("A-large.in");
	//ifstream fin ("fileQ1.txt");
	ofstream fout ("output.out");
	unsigned long long test;
	fin >> test;
	
	for ( unsigned long long t=1; t<=test; ++t ) 
	{
		unsigned long long Smax;
		fin >> Smax;
		
		string audience;
		fin >> audience;
		
		unsigned long long array[audience.size()][2];
		
		// cout << Smax << " " << audience << endl;
		
		unsigned long long level = 0;
		for ( unsigned long long i=0; i<audience.size(); ++i ) 
		{
			char ch = audience[i];
			unsigned long long no = ch-48;
			
			array[i][0] = no;
			array[i][1] = level;
			++level;
		}
		
		/* for ( int i=0; i<audience.size(); ++i ) {
			for ( int j=0; j<2; ++j ) cout << array[i][j] << " ";
			cout << endl;
		} */
		
		unsigned long long clapping = 0;
		unsigned long long introduced = 0;
		for ( unsigned long long i=0; i<audience.size(); ++i ) {
			while ( array[i][0] > 0 ) {
				while ( array[i][1] > clapping ) {
					++introduced;
					++clapping;
				}
				if ( array[i][1] <= clapping ) ++clapping;
				
				array[i][0] -= 1;
			}
		}
		
		cout << "Case #" << t << ": " << introduced << endl;
		fout << "Case #" << t << ": " << introduced << endl;
		//system("pause");
		
	} 
} // #EndOfMain!
