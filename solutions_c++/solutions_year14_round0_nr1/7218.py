#include <fstream>
using namespace std;

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("output.txt");
	int number, array1[4][4], array2[4][4];
	int i, j, k;
	int string1, string2;
	int variant, numOfVariants;
	cin >> number;
	for( k=1; k<=number; k++ )
	{
		cin >> string1;
		string1--;
		for( i=0; i<4; i++ )
		{
			for( j=0; j<4; j++ )
				cin >> array1[i][j];
		}
		cin >> string2;
		string2--;
		for( i=0; i<4; i++ )
		{
			for( j=0; j<4; j++ )
				cin >> array2[i][j];
		}
		numOfVariants = 0;
		for( i=0; i<4; i++ )
		{
			for( j=0; j<4; j++ )
			{
				if( array1[string1][i] == array2[string2][j] )
				{
					numOfVariants++;
					variant = array1[string1][i];
					break;
				}
			}
		}
		if(numOfVariants == 0)
			cout << "Case #" << k << ": Volunteer cheated!" << endl;
		else if(numOfVariants == 1)
			cout << "Case #" << k << ": " << variant << endl;
		else
			cout << "Case #" << k << ": Bad magician!" << endl;
	}
	return 0;
}