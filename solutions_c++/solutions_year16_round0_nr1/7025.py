#include <iostream>
#include <vector>

using namespace std;

vector<int> map(10,0);

void resetMap() {
	for (int i = 0; i < 10; ++i)
		map[i] = 0;
}

int solved() {
	for (int i = 0; i < 10; ++i)
		if(map[i] == 0)
			return 0;
	return 1;
}

void mark(long long N) {
	int k;

	while(N >= 10) {
		k = N%10;
		map[k] = 1;
		N /= 10;
	}
	map[N] = 1;
}

long long solve( int N ) {
	long long temp = N;
	while( 1 ) {
		mark(temp);
		if( solved() )break;
		temp += N;	
	}
		return temp;
}

int main(int argc, char const *argv[])
{
	long long t, N;

	cin >> t;

	for (int i = 1; i < t+1; ++i)
	{
		resetMap();
		cin >> N;
		cout << "Case #" << i << ": "; 
		if( N == 0 ) 
			cout<< "INSOMNIA" << endl;
		else
			cout << solve(N) << endl;
	}
	return 0;
}
