#include <iostream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

long long int getUpperRoot(long long int a)
{
	long long int b = (long long int) sqrt(a);
	if (b*b<a)
		b++;
	return b;
}

long long int getLowerRoot(long long int a)
{
	long long int b = (long long int) sqrt(a);
	return b;
}

bool isPalindrome(long long int a)
{
	vector <int> list;
	while (a>0)
	{
		list.push_back(a%10);
		a/=10;
	}
	
	int ct = list.size();
	for (int i=0; i<ct/2; i++)
	{
		if (list[i]!= list[ct-1-i])
			return false;
	}
	
	return true;
}

int main()
{
	int T;
	cin >> T;
	//T = 10000;
	for (int i=0; i<T; i++)
	{
		long long int A, B;
		cin >> A >> B;
		//A = 1;
		//B = 100000000000000;
		int upperRootA = getUpperRoot(A);
		int lowerRootB = getLowerRoot(B);
		
		int ct = 0;
		for (int j=upperRootA; j<=lowerRootB; j++)
		{
			if (isPalindrome(j) && isPalindrome(j*j))
				ct++;
		}
		
		cout << "Case #" << i+1 << ": " << ct << endl;
	}
}