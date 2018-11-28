#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		string s;
		cin>>s;
		int arr[26]={0};
		int tot=0;
		tot=s.length();
		for(int i=0;i<tot;i++)
		{
			arr[s[i]-'A']++;
		}
		cout<<"Case #"<<tt<<": ";
		int ans[10]={0};
		while(tot>0)
		{
			if(arr['Z'-'A']>0 && arr['E'-'A']>0 && arr['R'-'A']>0 && arr['O'-'A']>0 )
			{
				ans[0]++;
				arr['Z'-'A']--;
				arr['E'-'A']--;
				arr['R'-'A']--;
				arr['O'-'A']--;
				tot-=4;
			}
			else if(arr['S'-'A']>0 && arr['I'-'A']>0 && arr['X'-'A']>0 )
			{
				tot-=3;
				ans[6]++;
				arr['S'-'A']--;
				arr['I'-'A']--;
				arr['X'-'A']--;
			}
			else if(arr['E'-'A']>0 && arr['I'-'A']>0 && arr['G'-'A']>0 && arr['H'-'A']>0 && arr['T'-'A']>0 )
			{
				tot-=5;
				
				ans[8]++;
				arr['E'-'A']--;
				arr['I'-'A']--;
				arr['G'-'A']--;
				arr['H'-'A']--;
				arr['T'-'A']--;
			}
			else if(arr['S'-'A']>0 && arr['E'-'A']>1 && arr['V'-'A']>0 && arr['N'-'A']>0 )
			{
				tot-=5;
				
				ans[7]++;
				arr['S'-'A']--;
				arr['E'-'A']-=2;
				arr['V'-'A']--;
				arr['N'-'A']--;
			}
			else if(arr['F'-'A']>0 && arr['I'-'A']>0 && arr['V'-'A']>0 && arr['E'-'A']>0 )
			{
				tot-=4;
				
				ans[5]++;
				arr['F'-'A']--;
				arr['I'-'A']--;
				arr['V'-'A']--;
				arr['E'-'A']--;
			}
			else if(arr['F'-'A']>0 && arr['O'-'A']>0 && arr['U'-'A']>0 && arr['R'-'A']>0 )
			{
				tot-=4;
				
				ans[4]++;
				arr['F'-'A']--;
				arr['O'-'A']--;
				arr['U'-'A']--;
				arr['R'-'A']--;
			}
			else if(arr['N'-'A']>0 && arr['I'-'A']>0 && arr['N'-'A']>0 && arr['E'-'A']>0 )
			{
				tot-=4;
				
				ans[9]++;
				arr['N'-'A']--;
				arr['I'-'A']--;
				arr['N'-'A']--;
				arr['E'-'A']--;
			}
			else if(arr['T'-'A']>0 && arr['H'-'A']>0 && arr['R'-'A']>0 && arr['E'-'A']>1 )
			{
				tot-=5;
				
				ans[3]++;
				arr['T'-'A']--;
				arr['H'-'A']--;
				arr['R'-'A']--;
				arr['E'-'A']-=2;
			}
			else if(arr['T'-'A']>0 && arr['W'-'A']>0 && arr['O'-'A']>0 )
			{
				tot-=3;
				
				ans[2]++;
				arr['T'-'A']--;
				arr['W'-'A']--;
				arr['O'-'A']--;
			}
			else if(arr['O'-'A']>0 && arr['N'-'A']>0 && arr['E'-'A']>0 )
			{
				tot-=3;
				
				ans[1]++;
				arr['O'-'A']--;
				arr['N'-'A']--;
				arr['E'-'A']--;
			}
		}	
		for(int i=0;i<10;i++)
		{
			for(int j=0;j<ans[i];j++)
			cout<<i;
		}
		cout<<endl;
	}
	return 0;
}
