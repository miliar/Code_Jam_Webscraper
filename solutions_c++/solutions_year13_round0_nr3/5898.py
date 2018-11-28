#include <iostream>
#include <vector>
using namespace std;

bool isPalindrome(int x) {
	if (x < 0)  return false;
	if (x == 0) return true;

	int div = 1;
	while (x/div >= 10) {
		div *= 10;
	}

	while (x > 0)
	{
		int l = x/div;
		int r = x%10;
		if (l != r) 
			return false;
		x = (x % div)/10;
		div /= 100;
	}
	return true;
}

bool getRoot(int x, int& root)
{
	if (x == 1)
	{
		root = 1;
		return true;
	}
	int l = 1;
	int r = x;
	while(l < r){
		int m = l+(r-l)/2;
		if (m*m == x)
		{
			root = m;
			return true;
		}else if (m*m > x)
		{
			r = m - 1;
		}else{
			l = m + 1;
		}
	}
	root = -1;
	return false;
}

int main(int argc, char** argv)
{
	int T;
	cin >> T;

	int A;
	int B;
	for (int i = 0; i < T; i++)
	{
		cin >> A >> B;
		int sum = 0;
		for (int k = A; k <= B; k++)
		{
			if (!isPalindrome(k))
				continue;
			int root;
			if (getRoot(k, root) && isPalindrome(root))
				sum++;
		}
		cout << "Case #" << i+1 << ": " << sum << endl;
	}

	return 0;
}

