#include <iostream>
#include <cstring>
using namespace std;
int a[10];
int b[26];
void function()
{
	if(b[25]!=0)
	{//z//zero
		a[0]=b[25];
		b[4]=b[4]-b[25];
		b[17]=b[17]-b[25];
		b[14]=b[14]-b[25];
		b[25]=0;
	}
	if(b[23]!=0)
	{//x//six
		a[6]=b[23];
		b[18]=b[18]-b[23];
		b[8]=b[8]-b[23];
		b[23]=0;
	}
	if(b[22]!=0)
	{//w//two
		a[2]=b[22];
		b[19]=b[19]-b[22];
		b[14]=b[14]-b[22];
		b[22]=0;
	}
	if(b[20]!=0)
	{//u//four
		a[4]=b[20];
		b[5]=b[5]-b[20];
		b[14]=b[14]-b[20];
		b[17]=b[17]-b[20];
		b[20]=0;
	}
	if(b[6]!=0)
	{//g//eight
		a[8]=b[6];
		b[4]=b[4]-b[6];
		b[8]=b[8]-b[6];
		b[7]=b[7]-b[6];
		b[19]=b[19]-b[6];
		b[6]=0;
	}
	if(b[18]!=0)
	{
		//s//seven
		a[7]=b[18];
		b[4]=b[4]-2*b[18];
		b[21]=b[21]-b[18];
		b[13]=b[13]-b[18];
		b[18]=0;
	}
	if(b[5]!=0)
		{//v//five
			a[5]=b[5];
			b[21]=b[21]-b[5];
			b[8]=b[8]-b[5];
			b[4]=b[4]-b[5];
			b[5]=0;
		}
	if(b[14]!=0)
	{
		a[1]=b[14];
	}
	if(b[8]!=0)
	{
		a[9]=b[8];
	}
	if(b[19]!=0)
	{
		a[3]=b[19];
	}
}

int main()
{
	int t,l,c,i,j;
	char s[2001];
	cin>>t;
	for(j=0;j<t;j++)
	{
		cin>>s;
		l=strlen(s);
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<l;i++)
		{
			c = s[i]-65;
			b[c]=b[c]+1;
		}
		function();
		cout<<"Case #"<<j+1<<": ";
		for(i=0;i<10;i++)
		{
			if(a[i]!=0)
			{
				while(a[i]!=0)
				{
					cout<<i;
					a[i]=a[i]-1;
				}
			}
		}
		cout<<endl;
	}
	
	return 0;
}