#include<iostream>
using namespace std;
int main()
{
	int t;
	long int num,rem,count=0;
	int arr[10],arr1[100];
	//cout<<"ENTER CASES";
	cin>>t;
	int main=t;
	while(t--)
	{
	//cout<<"ENTER NUMBER";
	cin>>num;
	if(num==0)
	{
		long int temp;
		temp=0;
	}
	else
	{
		for(int i=0;i<10;i++)
		{
			arr[i]=0;
		}
		//cout<<num<<endl;
		int flag=1;
		long int temp,numtemp;
		numtemp=num;
		while(1)
		{ 
			flag=1;
			temp=num;
			//cout<<"TEMP : "<<temp<<"  "<<num<<endl;
			while(num!=0)
			{
				rem=num%10;
				if(arr[rem]==0)
				{
					arr[rem]=1;
				}
				else
				{
					count=arr[rem];
					arr[rem]=count+1;
				}
				num=num/10;
			}
			for(int i=0;i<10;i++)	
			{
				if(arr[i]==0)
				{
						flag=2;
					break;
				}
			}
			if(flag!=2)
			{
				break;
			}	
			num=temp;
			num=num+numtemp;
		}
		
		/*for(int i=0;i<10;i++)
		{
			cout<<arr[i]<<endl;
		}*/
		arr1[main-t]=temp;
		//cout<<temp;
	}
	}
	for(int i=1;i<101;i++)
	{
		if(arr1[i]==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<arr1[i]<<endl;
		}
	}
	return 0;
}	
