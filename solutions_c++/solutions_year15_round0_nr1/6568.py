#include<iostream>
#include<string>
using namespace std;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t,k,n,sum;
	string s;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		n = 0,sum=0;
		cin >> k >> s;

		for(int j = 0; j <= k; j++)
		{
			
			if(sum < j)
			{
				
				n += (j - sum);
				sum = j;
			}
			sum += s[j]-48;
		}

		cout << "Case #" << i << ": " << n <<endl;
	}





	return 0;
}
