#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int j,z;
	cin>>z;
for(j=0;j<z;j++)
{
	char arr[1000];
	int length;
	cin>>arr;
	length=strlen(arr);
	char arr2[2000]={'\n'};

	int a=1000,b=1000,c=1000; 
	arr2[1000]=arr[0];
//	cout<<length;
//	cout<<arr2[10]<<'\n';
	for(int i=1;i<length;i++)
	{
		if(arr2[c]>arr[i])
		{
//			cout<<"in if"<<'\n';
			a++;
			arr2[a]=arr[i];
		}

		else
		{
//			cout<<"in if"<<'\n';
			b--;
			c--;
			arr2[b]=arr[i];
		}
	}

	cout<<"Case #"<<j+1<<": ";
	for(int i=b;i<=a;i++)
		cout<<arr2[i];
	cout<<'\n';
}
	
		
}