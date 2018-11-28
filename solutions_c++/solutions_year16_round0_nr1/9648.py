#include <cstdio>
#include <iostream>

using namespace std;

const long long MAX_VAL = 1000000000000000000LL;

bool hasDigit[10];

bool applyDigits(long long x)
{
	if(x == 0) hasDigit[0] = true;
	while(x > 0)
	{
		hasDigit[x%10] = true;
		x /= 10;
	}
	for(int i=0; i<=9; i++) if(!hasDigit[i]) return false;
	return true;
}

void doTest(int caseNumber)
{
	for(int i=0; i<=9; i++) hasDigit[i]=false;
	
	long long N;
	
	cin >> N;
	long long X = N;
	
	if(X != 0)
		while(X <= MAX_VAL)
		{
			if(applyDigits(X)) break;
			X += N;
		}
	
	cout << "Case #" << caseNumber << ": ";
	if(X <= MAX_VAL and X != 0) cout << X << "\n";
	else cout << "INSOMNIA\n";
}

int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T; i++) doTest(i);
	
	return 0;
}
