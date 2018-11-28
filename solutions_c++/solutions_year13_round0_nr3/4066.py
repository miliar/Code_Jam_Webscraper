#include<iostream>
#include<vector>

bool isPalindrome(unsigned long long n)
{
	unsigned long long a = n;
	unsigned long long b = 0;

	while(n)
	{
		b *= 10;
		b += n % 10;
		
		n /= 10;
	}
	
	return a == b;
}

int main()
{
	std::vector<unsigned long long> fairAndSquares;
	
	for(unsigned long long n=1; n < 10000000; ++n)
	{
		unsigned long long nSquared = n*n;
	
		if(isPalindrome(n) && isPalindrome(nSquared))
		{
			fairAndSquares.push_back(nSquared);
		}
	}
	
	
	int numTests;
	std::cin >> numTests;
	
	for(int testCase = 1; testCase <= numTests; testCase++)
	{
		unsigned long long a, b;
		int ans = 0;
		
		cin >> a >> b;
		
		for(std::vector<unsigned long long>::iterator it = fairAndSquares.begin(); it != fairAndSquares.end(); it++)
		{
			if(*it >= a && *it <= b)
			{
				ans++;
			}
		}
		
		std::cout << "Case #" << testCase << ": " << ans << std::endl;
	}

	return 0;
}