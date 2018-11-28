#include <iostream>
#include <string>

using namespace std;

void quickSort(int arr[], int left, int right) {
	int i = left, j = right;
	int tmp;
	int pivot = arr[(left + right) / 2];
	
	/* partition */
	while (i <= j) {
		while (arr[i] < pivot)
			i++;
		while (arr[j] > pivot)
			j--;
		if (i <= j) {
			tmp = arr[i];
			arr[i] = arr[j];
			arr[j] = tmp;
			i++;
			j--;
		}
	};
	
	/* recursion */
	if (left < j)
		quickSort(arr, left, j);
	if (i < right)
		quickSort(arr, i, right);
}

int flip( bool* bData, int iFlipMax, bool bToDest )
{
	for( int i = iFlipMax; i >= 0; i-- )
	{
		if( bData[i] == bToDest )
		{
			int iCnt	= flip( bData, i, !bToDest );
			return iCnt + 1;
		}
	}

	return 1;
}

void main() {
	int t;	
	string str;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.	
	for (int i = 1; i <= t; ++i) {
		cin >> str;  // read n and then m.
		int iLen	= str.length();
		bool* b		= new bool[iLen];
		for( int i = 0; i < iLen; i++ )
		{
			if( str.at(i) == '-' )	b[i] = false;
			else b[i]	= true;
		}

		int iCnt	= 0;
		for( int i = iLen - 1; i >= 0; i-- )
		{
			if( !b[i] )
			{
				iCnt	= flip( b, i, true );
				break;
			}
		}
		cout << "Case #" << i << ": " << iCnt << endl;
	
    }

}