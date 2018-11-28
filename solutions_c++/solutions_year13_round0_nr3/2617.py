#include <iostream>
#include <cmath>

using namespace std;

bool IsPalindrome(unsigned long long i);

int main()
{
    int numCases;
    cin >> numCases;
    for (int caseNum = 1; caseNum <= numCases; caseNum++)
    {
	unsigned long long a;
	cin >> a;
	unsigned long long b;
	cin >> b;
	unsigned long long start = ceil(sqrt(a));
	unsigned long long end = floor(sqrt(b));
	unsigned long long counter = 0;
	for (unsigned long long i = start; i <= end; i++)
	{
	    if (IsPalindrome(i) && IsPalindrome(i*i))
	    {
		counter++;
		//cout << (i*i) << " ";
	    }
	}
	//cout << endl;
	cout << "Case #" << caseNum << ": " << counter << endl;
    }
}

bool IsPalindrome(unsigned long long i)
{
    unsigned long long temp = i;
    unsigned long long reverse = 0;
    while (temp > 0)
    {
	reverse = reverse * 10 + temp % 10;
	temp = temp / 10;
    }
    return reverse == i;
}
