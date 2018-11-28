#include <iostream>
#include <math.h>
using namespace std;

bool isPalindrome(int num)
{
	char digit[11];
	int i;

	for (i = 0; num; i++) {
		digit[i] = '0' + num % 10;
		num /= 10;
	}

	for (int j = 0; j < i; j++)
		if (digit[--i] != digit[j])
			return false;

	return true;
}

int main()
{
	int numCase;

	cin >> numCase;
	
	for (int currentCase = 1; currentCase <= numCase; currentCase++)
	{
		int a, b;
		int sqrtlimit;
		int count = 0;
		
		cin >> a >> b;
		sqrtlimit = (int)sqrt(b);

		for (int i = (int)ceil(sqrt(a)); i <= sqrtlimit; i++) {
			if (isPalindrome(i) && isPalindrome(i * i)) {
				count++;
			}
		}

		cout << "Case #" << currentCase << ": " << count << endl;
	}

	return 0;
}
