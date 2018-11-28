#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<fstream>
using namespace std;
int l,n,t,k,t2,p,over,o=0;
char s[100010],c;
void time(char x,char y,char& a,int& b)
{
	if(x=='1')
	{
		if(y=='i')
		{
			a='i';
			b=0;
		}
		else if(y=='j')
		{
			a='j';
			b=0;
		}
		else
		{
			a='k';
			b=0;
		}
	}
	else if(x=='i')
	{
		if(y=='i')
		{
			a='1';
			b=1;
		}
		else if(y=='j')
		{
			a='k';
			b=0;
		}
		else
		{
			a='j';
			b=1;
		}
	}
	else if(x=='j')
	{
		if(y=='i')
		{
			a='k';
			b=1;
		}
		else if(y=='j')
		{
			a='1';
			b=1;
		}
		else
		{
			a='i';
			b=0;
		}
	}
	else
	{
		if(y=='i')
		{
			a='j';
			b=0;
		}
		else if(y=='j')
		{
			a='i';
			b=1;
		}
		else
		{
			a='1';
			b=1;
		}
	}
}
int add(int x)
{
	x++;
	if(x==l)
	{
		p++;
		if(p==n)
			over=1;
		return 0;
	}
	else
		return x;
}
int main()
{
	fstream file1,file2;
	file1.open("a.in",ios::in);
	file2.open("b.txt",ios::out);
	int h;
	file1>>h; //scanf("%d",&h);
	while(h--)
	{
		file1>>l>>n; //scanf("%d%d",&l,&n);
		file1>>s; //scanf("%s",s);
		o++;
		t=over=p=k=0;
		c=s[k];
		while(!(t==0&&c=='i'))
		{
			k=add(k);
			if(over)
			{
				file2<<"Case #"<<o<<": NO\n"; //printf("Case #%d: NO\n",o);
				break;
			}
			time(c,s[k],c,t2);
			t^=t2;
		}
		if(over)
			continue;
		k=add(k);
		if(over)
			continue;
		c=s[k];
		while(!(t==0&&c=='j'))
		{
			k=add(k);
			if(over)
			{
				file2<<"Case #"<<o<<": NO\n"; //printf("Case #%d: NO\n",o);
				break;
			}
			time(c,s[k],c,t2);
			t^=t2;
		}
		if(over)
			continue;
		k=add(k);
		if(over)
			continue;
		c=s[k];
		while(1)
		{
			k=add(k);
			if(over)
			{
				//file2<<"Case #"<<o<<": NO\n"; //printf("Case #%d: NO\n",o);
				break;;
			}
			time(c,s[k],c,t2);
			t^=t2;
		}
		if(c=='k'&&t==0)
			file2<<"Case #"<<o<<": YES\n"; //printf("Case #%d: YES\n",o);
		else
			file2<<"Case #"<<o<<": NO\n";
	}
 	return 0;
}

