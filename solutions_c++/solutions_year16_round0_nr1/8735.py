#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int arr[10];
int main() 
{	
	//cout<<arr[4]<<" ";
	int t, a, fg = 10, c=1;
	long long p, n, i, k;
//	unsigned long long temp;
	cin>>t;
	while(t--)
	{
		memset(arr,0,sizeof(arr));
		cin>>n;
		k = n;
		fg = 10;
		if (n == 0)
		{
			cout<<"Case #"<<c<<": INSOMNIA\n";
			c++;
			continue;
		}
		i = 1;
		while (fg)
		{
			n = k*i;
			p = n;
			while (p)
			{
				a = p % 10;
				if(arr[a] == 0)
				{
					arr[a] = 1;
					fg--;
				}
				if (fg == 0)
					break;
				p /= 10;
			}
			i++;
		}
		cout<<"Case #"<<c<<": "<<n<<"\n";
		c++;
	}
	return 0;
}