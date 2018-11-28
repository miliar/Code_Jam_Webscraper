
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;
int ProcessInput();

int main()
{

int testcases, i;

cin >> testcases;

for(i=0; i < testcases; i++) {
	cout<<"Case #"<<i + 1<<": ";
	ProcessInput();
}

return 0;
}

long long A, B, K, possible_wins, i, j;
int ProcessInput()
{

cin >> A;
cin >> B;
cin >> K;
possible_wins = 0;
//int size = sizeof(long long);
for(i = 0; i < A; i ++)
	for(j=0; j < B; j++)
		if( (i & j) < K )
			possible_wins ++;


//cout << cur_time_taken << endl;
printf("%lld\n", possible_wins);

return 0;

}

