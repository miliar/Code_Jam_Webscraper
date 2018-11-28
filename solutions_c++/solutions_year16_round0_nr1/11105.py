
#include<bits/stdc++.h>
using namespace std;
int debug=1;
int main()
{
	int N;
	cin >> N;
	int i=1,n=0,j=0,r=0,count=0;
	long long n1=1LL;
	vector<int> arr(10,0);
	while(N--)
	{
		scanf("%d",&n);
		if(n==0)
		{
			cout << "Case #" << i++ << ": INSOMNIA"  << endl;
			continue;
		}

		for(int z=0;z<10;z++)
			arr[z]=0;
		count=0;
		j=1;
		while(1)
		{
			n1=j*n*1LL;
			while(n1>0)
			{
				r=n1%10;
				if(arr[r]==0)
				{
					arr[r]=1;
					count++;
				}
				n1=n1/10;
			}
			if(count==10)
			{
				cout << "Case #" << i++ << ": " << j*n << endl;
				break;
			}
			j++;
		}
	}
	return 0;
}
