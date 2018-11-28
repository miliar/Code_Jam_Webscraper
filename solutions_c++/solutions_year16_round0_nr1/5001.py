#include <iostream>

using namespace std;

bool seenTendigits ( int arr[10] )
{
	for ( int i = 0; i < 10; i++ )
	{
		if ( arr[i] == 0 )
			return false;
	}
	return true;
}

int main ()
{
	int T;
	cin >> T;

	for ( int i = 1; i <= T; i++ )
	{
		unsigned long name;
		cin >> name;

		int arr[10] = { 0 };

		if ( name == 0 )
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}

		// final name
		unsigned long finName = name;

		for ( int j = 1; ; j++ )
		{
			finName = name * j;

			//local name
			unsigned long lName = finName;
			while ( lName > 0 )
			{
				arr[lName % 10]++;
				lName /= 10;
			}

			//check if all digits are seen
			if ( seenTendigits ( arr ) )
				break;
		}
		//print the final name
		cout << "Case #" << i << ": " << finName << endl;
	}
}