#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for(int l=1;l<=t;l++)
	{
		int n;
		cin >> n;
		int a[(2*n-1)*n];
		for(int i=0;i<(2*(n)-1)*n;i++)
			cin >> a[i];
		int b[n];
		for(int i=0;i<(2*n-1)*n;i++)
		{
			if(a[i]>0)
			{
				for(int j=i+1;j<(2*n-1)*n;j++)
				{
					if(a[i]==a[j])
					{
						a[i]=(-1)*2*(i);
						a[j]=(-1)*2*(i);
						break;
					}
				}
			}
		}	
		int j=0;
		for(int i=0;i<(2*n-1)*n;i++)
		{
			if(a[i]>0)
			{
				b[j]=a[i];
				j++;
			}
		}
		sort(b,b+n);
		cout << "Case #" << l <<": ";
		for(int i=0;i<n;i++)
			cout << b[i] << " ";
		cout << endl;
	}
}
