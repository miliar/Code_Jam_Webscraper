#include<iostream>
#include<conio.h>
using namespace std;
int arr[26];
int mmax()
{
	int ans=0;
	for(int i=0;i<26;i++)
	{
		if(arr[i]>arr[ans])
		ans=i;
	}
	return ans;
}
int mmax1(int m)
{
	int ans=-1;
	for(int i=0;i<26;i++)
	{
		if(i==m)
		continue;
		if(ans==-1 ||arr[i]>=arr[ans])
		ans=i;
	}
	return ans;
}
char fun(int x)
{
	arr[x]--;
	return (char)('A'+x);
}
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		for(int i=0;i<26;i++)
		arr[i]=0;
	
	cout<<"Case #"<<tt<<":";
		int n;
		cin>>n;
		int rem=0;
		for(int i=0;i<n;i++)
		{
			cin>>arr[i];
			rem+=arr[i];
		}	
		while(rem>0)
		{
		//	cout<<"rem"<<rem<<endl;
		//	getch();
			cout<<" ";
			int m1=mmax();
			int m2=mmax1(m1);
			if(m1==1 && m2==1)
			{
				cout<<fun(m1)<<fun(m2);
				rem-=2;
				continue;
			}
			else if(m2==0 && m1==1)
			{
				cout<<fun(m1);
				rem-=1;
				continue;
			}
			//case 2
			int ok=1;
			for(int i=0;i<26;i++)
			{
				if(arr[i]==0)
				continue;
				if((i==m1 || i==m2) && (arr[i]-1)*2>(rem-2))
				{
					ok=0;
				}
				else if(i!=m1 && i!=m2 && (arr[i])*2>(rem-2))
				{
					ok=0;
				}
				if(ok==0)
				break;
			}
			if(ok)
			{
				cout<<fun(m1)<<fun(m2);
				rem-=2;
				continue;
			}
			//case 3
			ok=1;
			for(int i=0;i<26;i++)
			{
				if(arr[i]==0)
				continue;
				if(i==m1 && (arr[i]-1)*2>(rem-1))
				{
					ok=0;
				}
				else if(i!=m1 && (arr[i])*2>(rem-1))
				{
					ok=0;
				}
				if(ok==0)
				break;
			}
			if(ok)
			{
				cout<<fun(m1);
				rem-=1;
				continue;
			}
						//case 1
			ok=1;
			for(int i=0;i<26;i++)
			{
				if(arr[i]==0)
				continue;
				if(i==m1 && (arr[i]-2)*2>(rem-2))
				{
					ok=0;
				}
				else if(i!=m1 && (arr[i])*2>(rem-2))
				{
					ok=0;
				}
				if(ok==0)
				break;
			}
			if(ok)
			{
				cout<<fun(m1)<<fun(m1);
				rem-=2;
				continue;
			}

		}
		cout<<endl;
		
	}
	
	
	
	return 0;
}
