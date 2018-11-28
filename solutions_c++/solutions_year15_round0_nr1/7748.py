#include<iostream>
using namespace std;

int main()
{
	int t,i=1;
	cin>>t;
	while(t--)
	{
		int smax,total=0,fri=0;
		cin>>smax;
		char arr[smax+2];
		cin>>arr;
		
		for(int j=0;arr[j]!='\0';j++)
		{
			if(total>=j)
			{
				total=total+(arr[j]-'0');
			}
			else
			{
				fri+=(j-total);
				total+=(j-total);
				total=total+(arr[j]-'0');
			}
		}
		cout<<"Case #"<<i<<": "<<fri<<"\n";
		i++;
	}
	return 0;
}