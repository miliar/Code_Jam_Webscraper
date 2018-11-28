#include<iostream>
#include<stdlib.h>
using namespace std;

int check(int cnt[])
{
	for(int i=0;i<=9;i++)
	{
		if(cnt[i]<=0)
		return 0;
	}
	return 1;
}

void flsh(int cnt[])
{
	for(int i=0;i<=9;i++)
	{
		cnt[i]=0;
	}
}


int main()
{
	long long no,temp,temp1,temp2;
	int t,rem=0,cnt[10]={0},count=1,t1=1;
	cin>>t;
	while(t>0)
	{
		cin>>no;
		temp1=no;
		count=1;
		flsh(cnt);
		if(no!=0)
		{
			do
			{
				temp=temp1;
				while(temp>0)
				{
					rem=temp%10;
					cnt[rem]++;
					temp=temp/10;
				}
			count++;
			temp2=temp1;
			temp1=no*count;
			}while(!check(cnt));
			count--;
			cout<<"Case #"<<t1<<": "<<temp2<<endl;	
		}
		else
		{
			cout<<"Case #"<<t1<<": INSOMNIA"<<endl;
		}
		t1++;
		t--;
	}

}
