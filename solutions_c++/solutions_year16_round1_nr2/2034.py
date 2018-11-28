#include<iostream>

using namespace std;
int main()
{
	int b[2510];

	
int t;
cin>>t;
int d=1;
do{
		for(int i=0;i<2510;i++)
	{
		
		b[i]=0;
		
	}
	

int n;
cin>>n;
int arr[n];
int l=2*n-1;
int i=0;
for(i=0;i<l;i++)
{
	
	for(int j=0;j<n;j++)
	{
		cin>>arr[j];
		int h=arr[j];
		b[h]=b[h]+1;
		
	}



	
}
cout<<"Case #"<<d<<": ";

for(int j=0;j<2510;j++)
	{
	
	if(b[j]!=0)
	{int p=b[j]%2;
		if(p==1)
		{cout<<j<<" ";
		}
		
		
	}
	
	
	}
	cout<<endl;

	
	
	
d++;}while(d<=t);
	
	return 0;
}
