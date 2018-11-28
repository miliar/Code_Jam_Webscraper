#include <iostream>

using namespace std;

int main()
{
	freopen( "C-small-attempt0.in", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int T = 0;
	scanf( "%d", &T );

	for( int i = 0; i < T; i++ )
	{
		int A = 0;
		scanf( "%d", &A );

		int B = 0;
		scanf( "%d", &B );

		int count = 0;
		int arr[5] = {1,4,9,121,484};

		for( int j = 0; j < 5; j++ )
		{
			if( (A <= arr[j])&&(arr[j] <= B ) ) count++;
		}

		printf( "Case #%d: %d\n", i+1, count );
	}

	return 0;
}