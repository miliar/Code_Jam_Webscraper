#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stack>

using namespace std;

int countFairAndSquare( double aStr , double bStr );
bool isPalindrome( double P );

int main () {

  string line;
  int num_of_cases = 0;
  int caseCount = 0;

  double A = 0, B = 0;

  int res = 0;

  ifstream input( "C-small-attempt0.in" );

  ofstream output( "C-small1.out" , ios_base::app );

  if ( input.is_open() && input.good() )
  {
	  getline( input , line );
	  istringstream iss(line);

	  iss >> num_of_cases;

	  cout << "Case count: " << num_of_cases << endl;

	if( num_of_cases > 0 )
	{
		while( input.good() && caseCount < num_of_cases )
		{

			// read N and M
			getline( input , line );
			istringstream iss(line);

			iss >> A >> B;
			/*cout << "A: " << A << " B: " << B << endl;*/

			/*if( isPalindrome( A ) )
			{
				cout << "A YES" << endl;
			}
			else
			{
				cout << "A NO" << endl;
			}
			if( isPalindrome( B ) )
			{
				cout << "B YES" << endl;
			}
			else
			{
				cout << "B NO" << endl;
			}*/

			caseCount++;

			// analyse case
			res = countFairAndSquare( A , B );

			if( output.is_open() && output.good() )
			{
				output << "Case #" << caseCount << ": " << res << endl;
			}

		}
	}
    
    input.close();
	output.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}

int countFairAndSquare( double A , double B )
{
	int fairAndSquareCount = 0;
	double squareTemp = 0;

	for( double i = A; i <= B; i++ )
	{
		if( isPalindrome( i ) )
		{
			squareTemp = sqrt( i );

			if( ( static_cast<int>(i) % static_cast<int>(squareTemp) == 0 ) && isPalindrome( squareTemp ) )
			{
				fairAndSquareCount++;
			}
		}
	}

	return fairAndSquareCount;
}

bool isPalindrome( double P )
{
	// get digits first
	ostringstream str;
	str << P;
	string dStr = str.str();

	double length = dStr.length();

	if( length == 1 )
		return true;

	/*cout << "double from stream: " << dStr << " length: " << length << endl;*/

	for( double i = 0; i < length / 2; i++ )
	{
		if( dStr.at( i ) != dStr.at( length - 1 - i ) )
		{
			return false;
		}
	}

	return true;
}