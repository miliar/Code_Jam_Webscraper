#include <iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int i=0; i<t; i++)
	{
		
		int n;
		cin>>n;

		cout<<"Case #"<<i+1<<": ";

		if(n==0)
			cout<<"INSOMNIA"<<endl;
		else
		{
			bool a[10];
			for(int j=0;j<=9; j++)
			{
				a[j] = false;
			}
			

			long long int count = 1; 
			while(true)
			{
				long long int tempans = n*count;
				long long int ans = tempans;
				while(tempans!=0)
				{
					int temp = tempans%10;
					a[temp] = true;
					tempans = tempans/10;
				}

				bool flag = true;
				for (int k=0; k<=9; k++)
				{
					if(a[k]==false)
					{
						flag = false;
						break;
					}
				}
				if(flag==true)
				{
					cout<<ans<<endl;
					break;
				}
				count++;
			}
		}		
	}

	return 0;
}
