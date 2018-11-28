/* Fair and Square Solver*/

#include<iostream>
#include<cmath>

using namespace std;
bool ispalindrome(int i);


int main()
{
	int testcases;
	int sqarray[33];
	cin >> testcases;

	for(int p = 1; p*p < 1000; ++p)
		sqarray[p] = p*p;
	sqarray[32] = 1001;

	for(int t = 1; t<= testcases ; ++t)
	{
		long long int A, B;

		cin>>A>>B;

		int k = ceil(sqrt(A));
		int i = sqarray[k];
		int ctr = 0;
		bool f = false, f2 = false;

		for( ; sqarray[k]<=B; k++)
		{
			
			f = ispalindrome(sqarray[k]);
			if (f == true)
				f2  = ispalindrome(k);
				if(f2 == true)
					ctr++;

			f = false;
			f2 = false;

		}

		cout<<"Case #"<<t<<": "<<ctr<<endl;

	}

	return 0;
}

bool ispalindrome(int i)
{
	int rev=0, digit;
	int num = i;
//	cout<<i<<' ';

	do
	{
		digit = i%10;
		rev = (rev*10) + digit;
		i = i/10;
	}while (i!=0);

//	cout<<num<<' '<<rev<<endl;

	if (num == rev)
		return true;
	else
		return false;
}



