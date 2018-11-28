#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;
bool checkPalindrome(int number);
int main()
{
	int test,a,b;
	int tc,i,count;
	float root;
	bool pal,sqpal;
	while (cin>>test)
	{
		for (tc=1; tc<=test; tc++)
		{
			cin>>a>>b;
            count = 0;
			for ( i = a; i <=b ; i++)
			{
				pal = checkPalindrome(i);
				if (pal==true)
				{
					root = sqrt(i);
					if (fmod(root*10,10)==0)
					{
						sqpal = checkPalindrome(root);
						if (sqpal==true)
						{
							count++;
						}
					}
				}
			}

			cout<<"Case #"<<tc<<": "<<count<<endl;
		}
	}
	return 0;
}

bool checkPalindrome(int number)
{
	int digits[100],k;
	int index,palindrome,n;
	index=0;
	palindrome=1;
	n=number;
	do
	{
		digits[index++] = n%10;
		n=n/10;
	} while (n>0);

	for (k=0;k<index/2+1;k++)
	{
		if (digits[k]!=digits[index-1-k])
		{
			palindrome=0;
			break;
		}
	}
	if (palindrome==1)
		return true;
	else
		return false;
}
