#include <bits/stdc++.h>
using namespace std;
int arr[26];
int brr[9];
bool test()
{
	for(int i=0;i<26;i++)
	{
		if(arr[i]){
		//	cout<<i<<endl;
			return true;
		}
	}
	return false;
}
int main()
{
	char s[2005];
	int t,i1=1;
	cin>>t;
	while(i1<=t)
	{

		memset(arr,0,sizeof(arr));
		memset(brr,0,sizeof(brr));
		cin>>s;
		int len=strlen(s);
		for(int i=0;i<len;i++)
			arr[(int)s[i]-(int)'A']++;
		cout<<"Case #"<<i1<<": ";
		i1++;
		while(test())
		{
			int x;

		//	cin>>x;
			while(arr[19]&&arr[22]&&arr[14])
			{
				brr[2]++;
		//		cout<<"2";
			arr[19]--;arr[22]--;arr[14]--;		
			}
				while(arr[5]&&arr[14]&&arr[20]&&arr[17])
			{
				brr[4]++;
		//		cout<<"4";
			arr[5]--;arr[14]--;arr[17]--;arr[20]--;		
			}

				while(arr[25]&&arr[4]&&arr[17]&&arr[14])
			{
				brr[0]++;
			//	cout<<"0";
				arr[25]--;arr[4]--;arr[17]--;arr[14]--;		
			}				
			while(arr[14]&&arr[13]&&arr[4])
			{
				brr[1]++;
		//		cout<<"1";
				arr[14]--;arr[13]--;arr[4]--;		
			}
		//	cout<<"a";
				
				while(arr[18]&&arr[8]&&arr[23])
			{
				brr[6]++;
		//		cout<<"6";
			arr[18]--;arr[8]--;arr[23]--;		
			}
			while(arr[5]&&arr[8]&&arr[21]&&arr[4])
			{
				brr[5]++;
		//		cout<<"5";
			arr[5]--;arr[8]--;arr[21]--;arr[4]--;		
			}
		
			while(arr[4]&&arr[8]&&arr[6]&&arr[7]&&arr[19])
			{
				brr[8]++;
		//		cout<<"8";
			arr[4]--;arr[8]--;arr[6]--;arr[7]--;arr[19]--;		
			}
			
			while(arr[18]&&((arr[4]-1)>0)&&arr[21]&&arr[13])
			{
				brr[7]++;
			//	cout<<"7";
				arr[18]--;arr[4]--;arr[21]--;arr[13]--;arr[4]--;		
			}
			while(((arr[13]-1)>0)&&arr[8]&&arr[4])
			{
				brr[9]++;
			//	cout<<"9--";
				arr[13]--;arr[8]--;arr[4]--;arr[13]--;		
			}
			while(arr[19]&&arr[17]&&((arr[4]-1)>0)&&arr[7])
			{
				brr[3]++;
			//	cout<<"3";
				arr[17]--;arr[19]--;arr[4]--;arr[7]--;arr[4]--;		
			}
			
			//cout<<"aaa";
	
	
		
		
	
		
		//	cout<<endl;
		}
		for(int i=0;i<10;i++)
		{
			while(brr[i])
			{
				cout<<i;
				brr[i]--;
			}
		}
		cout<<endl;
	}
}