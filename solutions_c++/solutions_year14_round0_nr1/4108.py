#include<vector>
#include<fstream>
#include<string>
#include<algorithm>
#include<ctime>
using namespace std;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t , n ;
	cin >> t;
	for ( int i = 0 ; i < t ; i++ )
	{
		int n1;
		vector < int > first(4);
		int n2;
		vector < int > second(4);
		int temp;
		cin >> n1;
		for ( int i = 0 ; i < 4 ; i++ )
			for ( int j = 0 ; j < 4 ; j++)
				if ( i == n1-1 )
					cin >> first [ j ] ;
				else
					cin >> temp;
		cin >> n2;
		for ( int i = 0 ; i < 4 ; i++ )
			for ( int j = 0 ; j < 4 ; j++)
				if ( i == n2-1 )
					cin >> second [ j ] ;
				else
					cin >> temp;
		
		int count = 0;
		int number;
		
		for ( int i = 0 ; i < 4 ; i++ )
			for ( int j = 0 ; j < 4 ; j++)
				if( first [ i ] == second [ j ] )
				{
					count++;
					number = first [ i ];
				}
		

		if ( count == 1 )
			cout << "Case #" << i+1 << ": " << number << endl;
		else if ( count == 0 )
			cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		else 
			cout << "Case #" << i+1 << ": Bad magician!" << endl;

	}
}