#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
string s;
int myfuction(void);
void swap(int,int);
void reverse(int,int);
bool valid(void);
int findend(void);
int findfirstnegative(void);
int main()
{
	int t,t1=1;
	cin >> t;
	while(t1<=t)
	{
		int ans;
		//string s;
		cin >> s;
		if(valid())
		{
			cout<<"Case #"<<t1<<": "<<0<<endl;
		}
		else
		{
			ans=myfuction();
			cout<<"Case #"<<t1<<": "<<ans<<endl;
		}
		t1++;
	}
}
int myfuction(void)
{
	//cout<<"myfunchello"<<endl;
	int end,count=0,firstneg;
	//end=findend(s);
	while(!valid())
	{
		end=findend();
		//cout << end << endl;
		if(s[0]=='-')
		{
			//cout << "hello"<<endl;
			swap(0,end);
			reverse(0,end);
			count++;
		}
		else
		{
			firstneg=findfirstnegative();
			swap(0,firstneg);
			count++;
			swap(0,end);
			reverse(0,end);
			count++;
		}
	}
	return count;
}
void swap(int start,int end)
{
	int i;
	for(i=start;i<=end;i++)
	{
		if(s[i]=='+')
		{
			s[i]='-';
		}
		else
		{
			s[i]='+';
		}
	}
}
void reverse(int start,int end)
{
	char temp;
	while(start<end)
	{
		temp=s[start];
		s[start]=s[end];
		s[end]=temp;
		start++;
		end--;
	}
}
bool valid(void)
{
	int i,flag=0;
	for(i=0;i<(int)s.size();i++)
	{
		if(s[i]=='-')
		{
			flag=1;
			break;
		}
	}
	if(flag==0)
		return true;
	else
		return false;
}
int findend(void)
{
	int i,end;
	for(i=0;i<(int)s.size();i++)
	{
		if(s[i]=='-')
			end=i;
	}
	return end;
}
int findfirstnegative(void)
{
	int i,end;
	for(i=0;i<(int)s.size();i++)
	{
		if(s[i]=='-')
		{
			end=i;
			break;
		}
	}
	return end-1;
}