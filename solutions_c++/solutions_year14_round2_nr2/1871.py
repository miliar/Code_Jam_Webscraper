/* Gansito144 */
#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<memory.h>
#include<set>

using namespace std;

typedef long long int i64;

i64 ans;

int main()
{	
	i64 T , A , B , K, ANS , AyB;
	
	cin >> T;
	
	for( int ca  = 1 ; ca <= T; ca++ )
	{
		cin >> A >> B >> K;
		ANS = 0;
		
		for( i64 i = 0; i < A ; i++ )
			for( i64 j = 0; j < B; j++ )
			{
				AyB =  i & j;
				if( AyB < K  ) ANS++;
			}
		
		cout << "Case #" << ca << ": " << ANS << endl;
	}
	return 0;
}
