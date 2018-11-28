#include <iostream>
#include <vector>
using namespace std;
int main()
{
	int A[10];
	int t;
	for (int i = 0; i < 10; i++)
	{
		A[i] = 0;
	}
	long int n;
	cin >> t;
	int q;
	int result;
	for (int i = 0; i < t; i++)
	{
		cin >> n;
		if(n == 0)
		{
			cout << "Case #"<<i+1<<": INSOMNIA"<<endl;
			continue;
		}
		int k = 1;
		while(A[0]*A[1]*A[2]*A[3]*A[4]*A[5]*A[6]*A[7]*A[8]*A[9] == 0)
		{
			q = n*k;
			result = q;
			while(q)
			{
				A[q%10] = 1;
				q = (q - (q%10))/10;
			}
			k++;
		}
			for (int  x= 0; x < 10; x++)
	{
		A[x] = 0;
	}

		cout << "Case #"<<i+1<<": "<<result<< endl;
	}
}