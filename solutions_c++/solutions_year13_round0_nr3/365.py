#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
vector<string>arr;
string nextPal(string str,long long* cb,long long pal)
{
	long long i,j,k,a,b,len,m;
	string str1="";
	char x,y,z;
	/*m=n;
	while(m>0)
	{
		str+='0'+m%10;
		m/=10;
	}*/
	len=str.length();
	a=0;
	for(i=0;i<(len+1)/2;i++)
	{
		if(str[i]!='9')
		{
			a=1;
			break;
		}
	}
	if(a==0||(*cb==0&&pal==0))
	{
		str="1";
		for(i=0;i<len-1;i++)
			str+='0';
		str+='1';
		*cb=(str.length()-1)/2;
	}
	else
	{
		x=str[len/2];
		if(x=='9'||pal==0)
		{
			i=len/2;
			j=(len-1)/2;
			for(;i>=0&&j<len;i++,j--)
			{
				if(j<*cb)
					pal=1;
				if(pal==0&&j>=*cb)
				{
					str[i]='0';
					str[j]='0';
				}
				else if(str[i]=='9')
				{
					str[i]='0';
					str[j]='0';
				}
				else
				{
					*cb=j;
					str[i]++;
					str[j]++;
					break;
				}
			}
		}
		else 
		{
			*cb=(len-1)/2;
			x++;
			str[len/2]=x;
			str[(len-1)/2]=x;
		}
	}
	/*n=0;
	for(i=0;i<str.length();i++)
		n=n*10+str[i]-'0';*/
	return str;
}
int checkPal(string str)
{
	long long i,m,j,x=0;
	/*m=n;
	while(m>0)
	{
		x=x*10+m%10;
		m/=10;
	}
	if(x==n)
		return 1;
	return 0;*/
	for(i=0,j=str.length()-1;j>i;j--,i++)
		if(str[i]!=str[j])
		{
			x=1;
			break;
		}
	if(x==1)
		return 0;
	return 1;
}
string mul(string str)
{
	int i,j,k,n,le=str.length(),cry,a,b;
	string str1="",str2,str3;
	char ar[102];
	for(i=0;i<102;i++)ar[i]='0';
	for(i=le-1;i>=0;i--)
	{
		str2="";
		j=le-i-1;
		while(j--)
			str2+='0';
		n=str[i]-'0';
		if(n==0)
			continue;
		cry=0;
		str3="";
		for(j=le-1;j>=0;j--)
		{
			k=str[j]-'0';
			k=k*n+cry;
			cry=k/10;
			k=k%10;
			str3+='0'+k;
		}
		if(cry!=0)
			str3+='0'+cry;
		str3=str2+str3;
		cry=0;
		for(k=0,j=100;k<str3.length();k++,j--)
		{
			a=str3[k]-'0';
			b=ar[j]-'0';
			a+=cry+b;
			if(a>9)
			{
				cry=1;
				a%=10;
			}
			else
				cry=0;
			ar[j]=a+'0';
		}
	}
	a=0;
	for(j=0;j<101;j++)
	{
		if(a==0&&ar[j]!='0')
			a=1;
		if(a==1)
			str1+=ar[j];
	}
	return str1;
}
void solve()
{
	long long i,j,n,m,cb;
	string str="101",str1="";
	arr.push_back("1");
	arr.push_back("4");
	arr.push_back("9");
	arr.push_back("121");
	arr.push_back("484");
	cb=1;
	while(str.length()<52)
	{
		//m=n*n;
		str1=mul(str);
		j=checkPal(str1);
		if(j==1)
			arr.push_back(str1);
		str=nextPal(str,&cb,j);
	}
}
int main()
{
	long long i,j,t,k,n,x;
	//fstream cin;
	string str,a,b;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Qualify\\C\\Large Input - 1.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Qualify\\C\\Large Output - 2.txt","w",stdout);
	cin>>t;
	//cin.ignore();
	solve();
	string str2="";
	for(i=arr.size()-1;i>=0;i--)
	{
		j=arr[i].length();
		j=101-j;
		k=str2.length();
		j=j-k;
		while(j--)
			str2+='0';
		arr[i]=str2+arr[i];
	}
	for(k=1;k<=t;k++)
	{
		n=0;
		//cin>>a>>b;
		cin>>a>>b;
		i=b.length();
		i=101-i;
		str2="";
		while(i--)
			str2+='0';
		b=str2+b;
		i=a.length();
		i=101-i;
		j=str2.length();
		i=i-j;
		while(i--)
			str2+='0';
		a=str2+a;
		for(i=0;i<arr.size();i++)
		{
			str=arr[i];
			j=str.compare(a);
			x=str.compare(b);
			if(j>=0&&x<=0)
				n++;
		}
		cout<<"Case #"<<k<<": "<<n<<endl;
	}
	return 0;
}