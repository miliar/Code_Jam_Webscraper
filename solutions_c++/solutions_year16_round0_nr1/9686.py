#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		long long n,m;
		int count = 0,j;
		bool arr[10];
		for(int j=0;j<10;j++)
		{
			arr[j] = false;
		}
		cin >> n;
		if(n==0)
		{
			cout << "Case #" << i <<": INSOMNIA" <<endl;
			continue;
		}
		for(j=1;;j++)
		{
			m=n*j;
			while(m!=0)
			{
				if(arr[m%10]==false)
				{
					arr[m%10]=true;
					count+=1;
					if(count==10)
					{
						break;
					}	
				}
				m = m/10;
			}
			if(count==10 || n*j<0)
			{
				break;
			}
		}
		if(count==10)
		{
			cout << "Case #" << i <<": " << n*j <<endl;
		}
		else
		{
			cout << "Case #" << i <<": INSOMNIA" <<endl;
		}
	}
	return 0;
}