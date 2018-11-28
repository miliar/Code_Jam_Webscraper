#include <iostream.h>
using namespace std;

int main() {
int t, n, frn, i, j=1, sum, arr[10];
char ch;
//	f1 >> t;
	t=100;
	while (t--)
	{
		frn=sum=0;
		cin >> n;
		for (i=0; i<n+1; i++)
		{
			cin >> ch;
			arr[i]=ch;
			arr[i]-=48;
		}
		for (i=0; i<n+1; i++)
		{
			sum+=arr[i];
			if (sum<i+1)
			{
				while (sum<i+1)
				{
					frn++;
					sum++;
				}
			}
		}
		cout <<"Case #"<<j<<": "<<frn<<endl;
		j++;
	}

	return 0;
}