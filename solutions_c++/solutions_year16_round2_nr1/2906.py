#include<iostream>
#include<string>
#include<sstream>
#include<algorithm>
using namespace std;
int checkrem(string &s, char c)
{
	for(int i=0;i<s.size();i++)
	{
		if(c==s[i])
		{
			s=s.substr(0,i)+s.substr(i+1,s.size()-i-1);
			return 1;
		}
	}
	return 0;
}
void bubble_sort(string arr)
{
	for(int i=0;i<arr.size()-1;i++)
	{
		for(int j=0;j<arr.size()-i-1;j++)
		{
			if(arr[j]>arr[j+1])
			{
				int t=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=t;
			}
		}
	}
}
int checknum(int j,string &s)
{
	string s2=s;
	//bubble_sort(s2);
	if(j==0)
	{
		if(checkrem(s2,'Z')&&checkrem(s2,'E')&&checkrem(s2,'R')&&checkrem(s2,'O'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==1)
	{
		if(checkrem(s2,'O')&&checkrem(s2,'N')&&checkrem(s2,'E'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==2)
	{
		if(checkrem(s2,'T')&&checkrem(s2,'W')&&checkrem(s2,'O'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==3)
	{
		if(checkrem(s2,'T')&&checkrem(s2,'H')&&checkrem(s2,'R')&&checkrem(s2,'E')&&checkrem(s2,'E'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==4)
	{
		if(checkrem(s2,'F')&&checkrem(s2,'O')&&checkrem(s2,'U')&&checkrem(s2,'R'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==5)
	{
		if(checkrem(s2,'F')&&checkrem(s2,'I')&&checkrem(s2,'V')&&checkrem(s2,'E'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==6)
	{
		if(checkrem(s2,'S')&&checkrem(s2,'I')&&checkrem(s2,'X'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==7)
	{
		if(checkrem(s2,'S')&&checkrem(s2,'E')&&checkrem(s2,'V')&&checkrem(s2,'E')&&checkrem(s2,'N'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==8)
	{
		if(checkrem(s2,'E')&&checkrem(s2,'I')&&checkrem(s2,'G')&&checkrem(s2,'H')&&checkrem(s2,'T'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	if(j==9)
	{
		if(checkrem(s2,'N')&&checkrem(s2,'I')&&checkrem(s2,'N')&&checkrem(s2,'E'))
		{
			s=s2;
			return 1;
		}
		return 0;
	}
	
}

int main()
{
	ostringstream o;
	int t;
	string s,num="";
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>s;
		num="";
		cout<<"Case #"<<i+1<<": ";
		/*for(int j=0;j<10;j++)
		{
			string s2=s;			
			for(int k=0;k<10;k++)
			{
				while(checknum((j+k)%10,s2)==1)
				{
					int temp=j+k;
					cout<<temp;
				}
				
			}
			if(s2=="")
			{
				cout<<num;
				break;
			}
				
			
		}*/
		while(checknum(0,s)==1)
		{
			num+="0";
			
		}
		while(checknum(2,s)==1)
		{
			num+="2";
		}
		while(checknum(4,s)==1)
		{
			num+="4";
		}
		while(checknum(6,s)==1)
		{
			num+="6";
		}
		while(checknum(8,s)==1)
		{
			num+="8";
		}
		while(checknum(1,s)==1)
		{
			num+="1";
		}
		while(checknum(5,s)==1)
		{
			num+="5";
		}
		while(checknum(7,s)==1)
		{
			num+="7";
		}
		while(checknum(9,s)==1)
		{
			num+="9";
		}
		while(checknum(5,s)==1)
		{
			num+="5";
		}
		while(checknum(3,s)==1)
		{
			num+="3";
		}
		sort(num.begin(),num.end());
		cout<<num;
		cout<<endl;
		
	}
	return 0;
}
