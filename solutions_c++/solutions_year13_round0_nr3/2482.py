#include <iostream>
#include <cstdio>
#include <limits>
#include <math.h>

using namespace std;

long long fairSquare[39];

int isPalindrome(unsigned long long number)
{
    long long reversed = 0;
    long long copy = number;
    
    while(number != 0)
    {
	reversed = reversed * 10 + number % 10;
	number /= 10;
    }
    return (reversed == copy) ? 1 : 0;
}

void printFairSquare()
{
    for(int i=0; i<39; i++)
    {
	cout << i+1 << ": " << fairSquare[i] << endl;
    }
}

void generateFairSquare()
{
    int j=0;

    long long limit = 100000000000000LL; 

    long long sqrtLimit = floor(sqrt(limit));
    
    for(long long i=1; i <= sqrtLimit; i++)
    {
	if (isPalindrome(i) && isPalindrome(i*i))
	{
	    fairSquare[j++] = i*i;
	}
    }
}

int fairSquareCount(long long A, long long B)
{
    int count = 0;

    for(int i = 0; i < 39; i++)
    {
	if((fairSquare[i] >= A) && (fairSquare[i] <= B))
	{
	    count++;
	}
    }
    return count;
}

int main()
{
    int T;
    long long A, B;

    generateFairSquare();

    cin >> T;
    
    for (int i=0; i<T; i++)
    {
	cin >> A >> B;
	
	if (A > B)
	{
	    cout << "Case #" << i+1 << ": 0" << endl;
	}
	else
	{
	    cout << "Case #" << i+1 << ": " << fairSquareCount(A, B) << endl;
	}
    }
    return 0;
}
