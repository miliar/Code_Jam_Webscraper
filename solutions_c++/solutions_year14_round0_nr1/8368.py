#include<iostream.h>

void main()
{
int arr[4][4],arr1[4][4],i,j,k,count,r1,r,p;
int t,n;
n=1;
cin>>t;

count=0;

while(t>0)
	{
	count=0;
	cin>>r;

	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			{
			cin>>arr[i][j];
			}
	}

	cin>>r1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			{
			cin>>arr1[i][j];
			}
	}
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
			{
			if(arr[r-1][i]==arr1[r1-1][j])
				{
				count++;
				p=arr[r-1][i];
				}
			}
	}
	if(count==0)
	cout<<"Case #"<<n<<": Volunteer cheated!"<<endl;
	if(count==1)
	{
	cout<<"Case #"<<n<<": "<<p<<endl;
	}
	if(count>1)
	{
	cout<<"Case #"<<n<<": Bad magician!"<<endl;
	}
	t--;
	n++;

}}