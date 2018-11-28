// My solution for Google jam problem Problem A. Prima donna
// https://code.google.com/codejam/contest/2442487/dashboard#s=p1
// Jerome

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>
#include <cmath>
using namespace std;

const char* inFileName = "C-small-attempt4.in";
const char* outFileName = "out.txt";


char mul( char a, char b, bool& neg)
{
	int i,j;
	if( a == '1' ) i = 0;
	if( a == 'i' ) i = 1;
	if( a == 'j' ) i = 2;
	if( a == 'k' ) i = 3;

	if( b == '1' ) j = 0;
	if( b == 'i' ) j = 1;
	if( b == 'j' ) j = 2;
	if( b == 'k' ) j = 3;

	const char table[4][4] = 
	{ 
		{'1','i','j','k'},
		{'i','1','k','j'},
		{'j','k','1','i'},
		{'k','j','i','1'},
	};
	const bool sign[4][4] = 
	{ 
		{true,true,true,true},
		{true,false,true,false},
		{true,false,false,true},
		{true,true,false,false},
	};

	neg = sign[i][j];
	char ret = table[i][j];
	return ret;
}

map<string,char> mymap;

char mulstring( const string& str )
{


	if( str.size() == 1 )
		return str[0];
	
	char c = '1';
	for( int i=0; i< str.size(); i++ )
	{
		bool b = false;
		c = mul(c, str[i], b);
	}
	return c;
}

int main()
{
	std::ifstream infile(inFileName);
	std::ofstream outfile(outFileName);
	if( infile.fail() || outfile.fail() )
	{
		return 0;
	}
	
	string line;
	getline(infile,line);
	int T = stoi(line);
	
	for( int Case = 1; Case <= T; Case++ )
	{
		getline(infile,line);
		istringstream iss(line); 
		int L,X;
		iss >> L >> X;
		
		string ijk;
		getline(infile,line);

		for( int i=0; i< X; i++ )
		{
			ijk += line;
		}

		bool possible = false;
		// split the string in three:
		//cout<<ijk<<endl;
		
	
		if( ijk.size() >= 3 )
		{
			bool isI = find(ijk.begin(), ijk.end(), 'i' ) != ijk.end();
			bool isJ = find(ijk.begin(), ijk.end(), 'j' ) != ijk.end();
			bool isK = find(ijk.begin(), ijk.end(), 'k' ) != ijk.end();
			int sum = isI ? 1 : 0;
			sum += isJ ? 1 : 0;
			sum += isK ? 1 : 0;

			int index = 0;
			if( sum < 2 )
				index = ijk.size();

			vector<int> mulArray(ijk.size());
			vector<bool> boolArray(ijk.size());
			boolArray[ijk.size()-1] = true;
			mulArray[ ijk.size()-1] = ijk[ijk.size()-1];
			for( int i=ijk.size()-2; i>=0; i-- )
			{
				bool b = false;
				mulArray[i] = mul( ijk[i] ,mulArray[i+1],b );
				boolArray[i] = b == boolArray[i+1];
			}

			char c = '1';
			bool b = true;
			bool bb = true;
			while( !possible )
			{
				if( index >= ijk.size() ) 
					break;
			
				bool test;
				c = mul( c, ijk[index], test); 
				index++;
				b = b == test;

				if( c == 'i' && b )
				{
					bb = true;
					int index2 = index;
					char d = '1';
					while( !possible )
					{
						bool b2;
						d = mul( d, ijk[index2], b2 );
						index2++;
						bb = bb == b2;

						if( d == 'j' && bb )
						{
							// the last part must be equal to k:
							//string remain = ijk.substr(index2);
							//char k = mulstring( remain );
							char k = mulArray[index2];
							if( k == 'k' && boolArray[index2] )
							{
								possible = true;
							}
						}
						
						if( index2 >= ijk.length()-1 )
							break;
					}
				}
				
				if( index >= ijk.length() -2 )
				{
					std::cout<<"breaking index = "<<index<<endl;
					break;
				}
				
			}
		}
		

		string pos = possible ? "YES" : "NO";
		cout<<"Case #"<<Case<<": "<<pos<<endl;
		outfile <<"Case #"<<Case<<": "<<pos<<endl;
	
		
	}	
	

    infile.close();
	outfile.close();
	system("pause");
	return 0;
}