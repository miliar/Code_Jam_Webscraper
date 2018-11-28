#include <iostream>
#include <algorithm>
using namespace std;

float N[10], K[10];

int main() {
	int T, n, i, j, countwar=0, t;
	cin>>T;
	for(t=1; t<=T; t++)
	{
		countwar = 0;
		for(i=0; i<10; i++)
		N[i] = K[i] = 0;

		cin>>n;
		for(i=0; i<n; i++)
		{
			cin>>N[i];
		}

		for(i=0; i<n; i++)
		{
			cin>>K[i];
		}

		sort(&N[0], &N[n-1]+1);
		sort(&K[0], &K[n-1]+1);
		/*
		for(i=0; i<n; i++)
		{
			cout<<N[i]<<" ";
		}
		cout<<endl;
		for(i=0; i<n; i++)
		{
			cout<<K[i]<<" ";
		}
		cout<<endl;
		*/
		i = j =0;
		while(i<n && j<n)
		{
			if(N[i]>K[j])
			j++;
			if(N[i]<K[j])
			{
				i++;
				j++;
				countwar++;
			}

		}
		//cout<<"Real war ans = "<<(n-countwar)<<endl;
		int count =0;
		float m;
		for(i=0; i<n; i++)
		{
			if(N[i]<K[i])
			{
				for(j=i+1;j<n; j++)
				{
					if(N[j]>K[i])
					{
						m = N[i];
						N[i] = N[j];
						N[j] = m;
						break;
					}
				}
			}
		}
		/*
		for(i=0; i<n; i++)
		{
			cout<<N[i]<<" ";
		}
		cout<<endl;
		for(i=0; i<n; i++)
		{
			cout<<K[i]<<" ";
		}
		cout<<endl;
		*/

		for(i=0; i<n; i++)
		if(N[i]>K[i])
		count++;

		cout<<"Case #"<<t<<": "<<count<<" "<<(n-countwar)<<endl;

	}

	return 0;
}
