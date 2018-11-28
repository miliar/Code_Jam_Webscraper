#include<bits/stdc++.h>
using namespace std;

int main() {
	int t,max,i;
	cin>>t;
	for(i=1;i<=t;i++)

	{
		int s=0,c=0,j;
		cin>>max;
		char arr[max+1];
		cin>>arr;

		for(j=0;j<max+1;j++)
		{
			if(i==0)
			{
             s=s+(arr[j]-'0');
			}
			else if(j<=s)
			{
				s=s+(arr[j]-'0');
			}
			else
			{
				c=c+1;
				s=s+(arr[j]-'0')+1;

			}

		}

	cout<<"Case #"<<i<<": "<<c<<endl;

	}

	return 0;
}
