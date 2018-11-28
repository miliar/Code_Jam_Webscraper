#include<iostream>
using namespace std;

int main()
{
	int t,i,j=1,dig,cnt=0;
	long long int n,x,y=1;
	cin >>t;
	i=1;
	while(i<=t)
	{
		cin >> n;
		j=1;
		cnt=0;
		int arr[10]={0};
		if(n==0)
			cout << "Case #" << i <<": "<< "INSOMNIA" << endl;
		else
		{
				while(1)
				{
					x=y=j*n;
					while(x>0)
					{
						dig=x%10;
						if(arr[dig]==0)
						{
							cnt++;
							arr[dig]++;
						}
						
						x=x/10;
						
					}
					if(cnt==10)
						{
							cout << "Case #" << i <<": " << y <<endl;
							break;
						}
						j++;
				}
		}
		i++;
	}
	return 0;
}
