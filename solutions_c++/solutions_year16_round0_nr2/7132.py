#include<bits/stdc++.h>
using namespace std;

char str[100];

int getlength()
{
	int count=0, i=0;
	while(1)
	{
		if((int)str[i]==43 || (int)str[i]==45)
			count++;
		else
			break;
		i++;
	}
		
	return count;
}
bool check()
{
	int i;
	int len=getlength(), count=0;
	for(i=0; i<len; i++)
		if((int)str[i]!=43)
			break;
	if(i==len)
		return true;
	else return false;
			
}
void flip(int end)
{
	for(int i=0; i<end; i++)
	{
		if((int)str[i]==43)
			str[i]='-';
		else
			str[i]='+';
	}
}
int getlast()
{
	int i=getlength()-1;
	while(i>=0)
	{
		if((int)str[i]==45)
			return i;
		i--;
	}
	
}
int main()
{
	int n;
	cin>>n;
	
	for(int z=0; z<n; z++)
	{
		scanf("%s", &str);
		int len=getlength();
		int end=getlast();
		int count=0;
		retrace:
		// last should be the last '-' encountered.
		char first=str[0];
		if(len==1 && (int)str[len-1]==45)
			cout<<"Case #"<<(z+1)<<": 1"<<endl;
		else if(len==1 && (int)str[len-1]==43)
			cout<<"Case #"<<(z+1)<<": 0"<<endl;
		else
		{
			for(int i=1; i<len; i++)
			{
				if((int)str[i]!=(int)first)
					{
						flip(i);
						/*cout<<endl;
						for(int i=0; i<len; i++)
						cout<<str[i]<<" ";*/
						count++;
						//cout<<"check="<<check;
						if(!check())
							goto retrace;
						else break;
					}
			}
			if((int)str[0]==43)
				cout<<"Case #"<<(z+1)<<": "<<count<<endl;
			else
				cout<<"Case #"<<(z+1)<<": "<<(count+1)<<endl;
			count=0;		
		}
	}
	
	return 0;
}









