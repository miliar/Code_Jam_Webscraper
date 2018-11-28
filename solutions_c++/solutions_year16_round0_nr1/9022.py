#include<iostream>

using namespace std;

int main()
{
	/* code */
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		int n,k,l,m;
		cin >> n;
		int a[10]={0};
		int cnt=0;
		for(int j=1;j<=1000;j++)
		{
			k = n*j;
			m=k;
			while(k)
			{
				l = k%10 ;
				k = k/10;
				if(a[l]==0)
				{
					a[l]=1;
					cnt++;
				}
			}
			if(cnt==10)
				break ;
		}
		cout << "Case #" << i <<": " ;
		if(cnt==10)
			cout << m <<endl;
		else 
			cout << "INSOMNIA" <<endl;
	}
	return 0;
}