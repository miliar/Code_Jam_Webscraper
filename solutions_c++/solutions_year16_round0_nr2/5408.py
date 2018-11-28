#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int t;
string input;
bool cek(string a)
{
	for(int i=0;i<a.length();i++)
	{
		if(a[i]=='-')
		return false;
	}
	return true;
}
void ubah(string &a,int idx)
{
	for(int i=0;i<=idx;i++)
	{
		if(a[i]=='-')
		a[i]='+';
		else
		a[i]='-';
	}
}
void tukar(string &a,int idx)
{
	char temp;
	for(int i=0;i<(idx-1)/2;i++)
	{
		temp=a[i];
		a[i]=a[idx-i];
		a[idx-i]=temp;
	}
	ubah(a,idx);
}
void positif(string &a)
{
	int idx=0;
	while(a[idx]=='+')
	{
		a[idx]='-';
		idx++;
	}
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int times=0;
		cin>>input;
		for(int j=1;j<input.length();j++)
		{
			if(input[j]!=input[j-1])
			times++;
		}
		if(input[input.length()-1]=='-')
		times++;
		printf("Case #%d: %d\n",i,times);
	}
}
