#include<iostream>

using namespace std;

int mul[10][10];

int main()
{
	int t,state=0;
	cin>>t;
	for(int test=0;test<t;test++){
		state=0;
	mul[1][1]=1;
	mul[1][2]=2;
	mul[1][3]=3;
	mul[1][4]=4;
	mul[2][1]=2;
	mul[2][2]=-1;
	mul[2][3]=4;
	mul[2][4]=-3;
	mul[3][1]=3;
	mul[3][2]=-4;
	mul[3][3]=-1;
	mul[3][4]=2;
	mul[4][1]=4;
	mul[4][2]=3;
	mul[4][3]=-2;
	mul[4][4]=-1;
	int l,x,a,b,c,i,j,k;
	int prefixsum[100000];
	int suffixsum[100000];
	string str2;
	string str1="";
	cin >> l >> x;
	cin >> str2;
	for(i=0;i<x;i++)
		str1+=str2;
	cout<<"Case #"<<test+1<<": ";
	for(i=0;i<str1.length();i++)
	{
		if(i==0)
		{
			if(str1[i]=='1')
				prefixsum[i]=1;
			else
				prefixsum[i]=str1[i]-'g';
		}
		else
		{
			if(str1[i]=='1')
				prefixsum[i]=prefixsum[i-1];
			else
			{
				if(prefixsum[i-1]>0)
					prefixsum[i]=mul[prefixsum[i-1]][str1[i]-'g'];
				else
					prefixsum[i]=(-1)*mul[(-1)*prefixsum[i-1]][str1[i]-'g'];
			}
		}
	}
	for(i=str1.length()-1;i>=0;i--)
	{
		if(i==str1.length()-1)
		{
			if(str1[i]=='1')
				suffixsum[i]=1;
			else
				suffixsum[i]=str1[i]-'g';
		}
		else
		{
			if(str1[i]=='1')
				suffixsum[i]=suffixsum[i+1];
			else
			{
				if(suffixsum[i+1]>0)
					suffixsum[i]=mul[str1[i]-'g'][suffixsum[i+1]];
				else
					suffixsum[i]=(-1)*mul[str1[i]-'g'][(-1)*suffixsum[i+1]];
			}
		}
	}
	//for(i=0;i<l*x;i++)cout<<prefixsum[i]<<" ";cout<<endl;
	//for(i=0;i<l*x;i++)cout<<suffixsum[i]<<" ";cout<<endl;
	for(i=0;i<str1.length();i++)
	{
		if(prefixsum[i]==2)
		{
			int sum=-10;
			for(j=i+1;j<str1.length();j++)
			{
				if(sum==3)
				{
					if(suffixsum[j]==4)
					{
						state=1;
						break;
					}
				}
				if(sum==-10)
				{
					if(str1[j]=='1')
						sum=1;
					else
						sum=str1[j]-'g';
				}
				else
				{
					if(str1[j]!='1' && sum>0)
						sum=mul[sum][str1[j]-'g'];
					else if(str1[j]!='1' && sum<0)
						sum=(-1)*mul[sum*(-1)][str1[j]-'g'];
				}
				if(state==1)
					break;
			}
		}
			if(state==1)
				break;
	}
	if(state==0)
	cout<<"NO\n";
	else cout<<"YES\n";
	}
	return 0;
}
