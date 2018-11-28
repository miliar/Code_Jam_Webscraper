#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
	int T,A,B,K;
	while ( cin >> T ) 
	for ( int t = 1 ; t <= T ; ++ t ) {
		cin >> A >> B >> K;
		int count = 0;
		for ( int i = 0 ; i < A ; ++ i )
		for ( int j = 0 ; j < B ; ++ j )
			if ( (i&j) < K ) count ++;
			
		printf("Case #%d: %d\n",t,count);
	}
	
	return 0;
}
