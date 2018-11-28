#include<bits/stdc++.h>

using namespace std;

void read(int *arr)
{
	int n,temp;
	string temp_str;
	cin>>n;
	for(int i=1;i<=4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>temp;
			if(i==n)
				arr[temp]++;
		}
		
	}
}
int main()
{
	int t;
	cin>>t;
	int case_no=1;
	while(t--)
	{
		int arr[20];
		memset(arr,0,sizeof arr);
		read(arr);
		read(arr);
		int two=-1,cnt_two=0;
		for(int i=1;i<=16;i++)
		{
			if(arr[i]==2)
				two=i,cnt_two++;
		}
		cout<<"Case #"<<case_no++<<": ";
		if(cnt_two==0)
		{
			cout<<"Volunteer cheated!";
		}
		else if(cnt_two==1)
		{
			cout<<two;
		}
		else
		{
			cout<<"Bad magician!";
		}
		cout<<"\n";
		
		
	}
	return 0;
}
