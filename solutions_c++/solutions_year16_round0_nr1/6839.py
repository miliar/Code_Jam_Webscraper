#include<iostream>
#include<conio.h>
using namespace std;
void arr_start(int *arr)
{
		for(int i=0;i<10;i++)
		{
			arr[i]=-1;
		}
}

bool check_array(int *arr)
{
	for(int i=0;i<10;i++)
	{
		//cout<<arr[i]<<endl;
	if(arr[i]==-1)
		return false;
	}
	return true;
}

int main()
{
	int t,chk,count=1;
	long long int num;
	int arr[10];
	cin>>t;
	while(t--)
	{
		int i=1;
		long long int temp;
		arr_start(arr);
	    cin>>num;
		temp=num;
		while(i<200)
		{
			
			//cout<<"Num:"<<num<<endl;
					while(num!=0)
					{
					chk=num%10;
					//cout<<"Chk:"<<chk<<endl;
					num=num/10;
					arr[chk]=chk;
					}
				if(check_array(arr))
				{
				cout<<"Case #"<<count<<": "<<i*temp<<endl;
				break;
				}
		num=temp;
		i++;
		num=i*num;
		}
		if(i>=200)
			cout<<"Case #"<<count<<": INSOMNIA"<<endl;
		count++;
	}
	getch();
return 0;
}