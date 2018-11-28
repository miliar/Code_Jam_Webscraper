#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int n,m;
	cin>>m;
for(n=0;n<m;n++)
{

	int i,j,k,check,count=0;;
	char arr[100];
	cin>>arr;
//	cout<<arr<<'\n';
	int l=strlen(arr);
//	cout<<l;
	for(i=1;i<l;i++)
	{
		if(arr[i-1]==arr[i])
		{

			check=1;
		}
		else
		{
			count++;
			
			check=0;
			
		}
	}

	if(arr[l-1]!='+')
		count++;

	cout<<"Case #"<<n+1<<": "<<count<<'\n';
}
	

}