#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;


long long int ans[1000001];

int main()
{
	ans[0] = -1;

	for(int i=1;i<1000001;i++)
	{
		long long int n = i;

		int C[10];

		for(int j =0;j<10;j++)
			C[j] = 0;

		long long int k = 1;
		while(1)
		{
			long long int x = n*k;

			while(x)
			{
				C[x%10]++;
				x/=10;
			}

			bool flag = true;

			for(int j=0;j<10;j++)
				if(C[j]==0)
					flag = false;

			if(flag)
			{
				ans[i] = n*k;
				break;
			}

			k++;
		}
	}



	int T;
	long long int N;

	cin >> T;
	int I = T;

	while(T--)
	{
		cin >> N;

		cout << "Case #" << I-T << ": "; 

		if(ans[N]==-1)
			cout << "INSOMNIA" << endl;
		else
			cout << ans[N] << endl;

	}

	return 0;
}