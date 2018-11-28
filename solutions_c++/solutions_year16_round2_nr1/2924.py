#include <iostream>
using namespace std;
char str[2001];
int number[10]={0};
	
void remove(char a,int nu,int len)
	{
		int r=0;
		int i=0;
		while(i<len&&r<nu)
		{
			if(str[i]==a)
			{
				str[i]='d';
				r++;
			}
			i++;
		}
	}
void check0(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='Z')
			{n++;
		str[i]='d';}
	
	}
		number[0]+=n;
	remove('E',n,len);
	remove('R',n,len);
	remove('O',n,len);
	
}
void check1(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='O')
			{n++;
		str[i]='d';}
		
	}
	number[1]+=n;
	remove('E',n,len);
	remove('N',n,len);
	
	
}
void check2(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='W')
			{n++;
		str[i]='d';}
	}
		number[2]+=n;
	remove('T',n,len);
	remove('O',n,len);
	
}
void check3(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='R')
			{n++;
		str[i]='d';}
	}
		number[3]+=n;
	remove('E',n,len);
	remove('H',n,len);
	remove('E',n,len);
	remove('T',n,len);
	
}
void check4(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='F')
			{n++;
		str[i]='d';}
	}
		number[4]+=n;
	remove('U',n,len);
	remove('R',n,len);
	remove('O',n,len);
	
}
void check5(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='V')
			{n++;
		str[i]='d';}
	}
		number[5]+=n;
	remove('E',n,len);
	remove('F',n,len);
	remove('I',n,len);
	
}
void check6(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='X')
			{n++;
		str[i]='d';}
	}
		number[6]+=n;
	remove('S',n,len);
	remove('I',n,len);

	
}
void check7(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='S')
			{n++;
		str[i]='d';}
	}
		number[7]+=n;
	remove('E',n,len);
	remove('V',n,len);
	remove('E',n,len);
	remove('N',n,len);
}
void check8(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='G')
			{n++;
		str[i]='d';}
	}
		number[8]+=n;
	remove('E',n,len);
	remove('I',n,len);
	remove('H',n,len);
	remove('T',n,len);
	
}
void check9(int len)
{
//	cout<<str<<endl;
	int i=0;
	int n=0;
	for(i=0;i<len;i++)
	{
		if(str[i]=='I')
			{n++;
		str[i]='d';}
	}
		number[9]+=n;
	remove('N',n,len);
	remove('N',n,len);
	remove('E',n,len);
	
}


int main() {

	int t;
	cin>>t;
	int count=1;
	int len;
	while(count<=t)
	{
		for(int i=0;i<10;i++)
			number[i]=0;
		len=0;
		cin>>str;
		for(int i=0;str[i]!='\0';i++)
		{
			len++;
		}
		check0(len);
		check8(len);
		check6(len);
		check7(len);
		check5(len);
		check4(len);
		check3(len);
		check2(len);
		check1(len);
		check9(len);
		cout<<"CASE #"<<count<<": ";
		for(int i=0;i<10;i++)
		{
			if(number!=0)
			{
				for(int j=0;j<number[i];j++)
				{
					cout<<i;
				}
			}
		}
		cout<<endl;
		//cout<<str<<endl;
		
		count++;
	}
	return 0;
}
