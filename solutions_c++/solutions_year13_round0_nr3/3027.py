#include <iostream>
#include <cmath>

using namespace std;

bool isPalindrome(int curr)
{
	int size = ceil(log10(curr))+1;
	int upper = pow(10, size-2);
	while(upper)
	{
		if(curr/upper != curr%10)
			return false;
		curr = (curr%upper)/10;
		upper /= 100;
	}
	return true;
}

int main()
{
	int T;
	cin >> T;
	for(int n=1; n<=T; n++)
	{
		int A, B;
		cin >> A >> B;
		int count = 0;
		for(int i=A; i<=B; i++)
		{
			if(isPalindrome(i) && sqrt(i)==floor(sqrt(i)) && isPalindrome(sqrt(i)))
				count++;
		}
		cout << "Case #" << n << ": " << count << endl;
	}
	return 0;
}
