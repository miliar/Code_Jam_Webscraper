#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main()
{
	int T;cin>>T;
	for(int t=0;t<T;t++)
	{
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		int *arr;
		arr=new int[smax+1];

		for(int i=0;i<s.length();i++)
		{
			arr[i]=s[i]-48;
		}

		for(int i=1;i<s.length();i++)
			arr[i]=arr[i]+arr[i-1];
		int num=0;
		for(int i=1;i<s.length();i++)
		{
			if(arr[i-1]<i)
			{
				num=num+(i-arr[i-1]);
			}
			arr[i]=arr[i]+num;
		}
		cout<<"Case #"<<t+1<<": "<<num<<endl;
		delete[] arr;
	}
}
