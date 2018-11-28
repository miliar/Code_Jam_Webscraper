#include <iostream>
using namespace std;

int main()
{
	long int T,n,A[10],r,z,p,j;
	cin>>T;
	for (int i = 0; i < T; i++)
	{
		r=1;
		int flag=0;
		for (j = 0; j < 10; j++)
		{
			A[j]=0;
		}

		cin>>n;

		if (n == 0)
		{
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		}

		else
		{
			while(flag != 10)
			{
				z = r*n;
				while(z != 0)
				{
					p = z%10;
					A[p] = 1;
					z = z/10;
				}
				for (j = 0; j < 10; j++)
				{
					if (A[j] == 1)
					{
						flag++;
					}
				}
				if (flag == 10)
				{
					cout<<"Case #"<<i+1<<": "<<r*n<<endl;
				}
				else
				{
					flag = 0;
					r++;
				}
			}
		}
	}
	return 0;
}