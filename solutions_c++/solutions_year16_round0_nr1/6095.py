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

void main() {
	int t, n;	
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.	
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		bool b[10];
		for( int k = 0; k < 10; k++ )
		{
			b[k]	= false;
		}
		bool bIsDONE	= false;
		for(int j = 1; j <= 200; j++ )
		{
			int v	= n * j;			
			while( v >= 10 )
			{
				int t	= v % 10;
				b[t]	= true;
				v		/= 10;				
			}
			b[v]	= true;

			bool bIsOK	= true;
			for( int m = 0; m < 10; m++ )
			{
				if( !b[m] )	bIsOK = false;
			}
			if( bIsOK )
			{
				cout << "Case #" << i << ": " << n*j << endl;
				bIsDONE		= true;
				break;
			}
		}	
		if( !bIsDONE )	cout << "Case #" << i << ": INSOMNIA" << endl;
    }

}