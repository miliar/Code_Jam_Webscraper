#include <string>
#include <iostream>
#include <cmath>

using namespace std;

bool isPal(long long x){
	long long tmp = x, revx = 0;
	while(tmp != 0){
		revx = revx * 10 + (tmp % 10);
		tmp = tmp / 10;
	}
	return (revx == x);
}

long long solve(long long a, long long b)
{
	int ret = 0;
	for(long long i = (long long)sqrt(a); i <= sqrt(b); ++i)
		if((i*i) >= a && (i*i) <= b && isPal(i) && isPal(i*i))
			++ret;
			
	return ret;
}

int main()
{
	int t;
	cin >> t;
	
	for(int testNo = 0; testNo < t; ++testNo){
		long long a, b;
		cin >> a >> b;
		cout << "Case #" << (testNo+1) << ": " << solve(a, b) << endl;
	}
	return 0;
}
