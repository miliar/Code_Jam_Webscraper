#include<stdio.h>
#include<string.h>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<math.h>

using namespace std;
int palin(char qa[101]);
int root(char ip[101],char qa[101],int lim);
void arrmul(char a[100],char b[100]);
int arrcom (char a[100],char b[100]);
void arrmult(char a[100],int s,char a1[100]);
void arrsub(char a[100],char b[100],char c[100]);
int next(char a[100]);
void sqr(char a[101],char c[101]);
void arrmulty(char a[20002],char b[20002],char c[20002]);
int arradd1(char a[20002],char b[20002],char c[20002]);
void arrmul1 (char a[20002],int b,char c[20002]);
void str(char a[20002]);
int main()
{
	int tc,b,ans,j,i,p,k,o,x,lol;
	ifstream ifile("d:/palin.txt");
	ofstream ofile("d:/palinsq.txt");
	ifile>>tc;
	char ipa[101],qa[101],ipb[101],qb[101],abc[101];
	for (j=0;j<tc;j++)
	{
		ans=0;
		ifile>>ipa;
		root(ipa,qa,0);
		if (j==124)
		printf("%s %s\n",ipa,qa);
		ifile>>ipb;
		root(ipb,qb,1);
		//printf("%s",qb);
		lol=arrcom(qa,qb);
		while (lol==0||lol==2)
		{
			x=palin(qa);
			if (x==1)
			{
				sqr(qa,abc);
				if (palin(abc)==1)
				{
					++ans;
				}
			}
			next(qa);
			lol=arrcom(qa,qb);
			//printf("%s\n",qa);
		}
		ofile<<"Case #"<<j+1<<": "<<ans<<endl;
		//cout<<j;
	}
	return 0;
}

int palin(char qa[101])
{
	int len=strlen(qa),i=0;
	while (i<len&&qa[i]==qa[len-1-i])
	{
		i++;
	}
	if (i==len)
	return 1;
	else
	return 0;
}


int root(char ip[101],char q[101],int lim)
{
	int tc,j,n,tmp,o,t,p,lp,i,var;
	char rem[101],div[101],a[101],a1[101];
		n=strlen(ip);
		if (n%2==0)
		{
			tmp=10*(ip[0]-48)+ip[1]-48;
			q[0]=4;
			while (q[0]*q[0]<=tmp)
			++q[0];
			t=tmp-(q[0]-1)*(q[0]-1);
			o=0;
			while (t>0)
			{
				rem[o++]=t%10+48;
				t=t/10;
			}
			rem[o]=0;
			strrev(rem);
			rem[o++]=ip[2];
			rem[o++]=ip[3];
			rem[o]=0;
			q[0]=q[0]+48-1;
			q[1]=0;
			i=4;
		}
		else
		{
			tmp=ip[0]-48;
			q[0]=0;
			while (q[0]*q[0]<=tmp)
			++q[0];
			t=tmp-(q[0]-1)*(q[0]-1);
			o=0;
			while (t>0)
			{
				rem[o++]=t%10+48;
				t=t/10;
			}
			rem[o++]=ip[1];
			rem[o++]=ip[2];
			rem[o]=0;
			q[0]=q[0]+48-1;
			q[1]=0;
			i=3;
		}
		int qu=1;
		while (i<=n)
		{
			//printf("rem=%s q=%s a=%s a1=%s",rem,q,a,a1);
			arrmul(q,a);
			p=strlen(a);
			lp='1';
			a[p]=lp;	
			a[p+1]=0;
			arrmult(a,lp-48,a1);
			while (arrcom(a1,rem)==0)
			{
				lp++;
				a[p]=lp;
				arrmult(a,lp-48,a1);
			}
			if (arrcom(a1,rem)==1)
			{
				lp--;
				a[p]=lp;
				arrmult(a,lp-48,a1);
			}
			q[qu++]=lp;
			q[qu]=0;
			arrsub(rem,a1,rem);
			o=strlen(rem);
			rem[o++]=ip[i++];
			rem[o++]=ip[i++];
			rem[o]=0;
		}
		if (lim==0&&rem[0]>0)
		{
			var=qu;
			while (qu>0&&q[qu-1]=='9')
			{
				q[qu-1]='0';
				qu--;
			}
			if (qu==0)
			{
				q[qu]='1';
				q[var]='0';
				q[var+1]=0;
			}
			else
			{
				q[qu-1]++;
			}
		}
}

void arrmul(char a[100],char b[100])
{
	strrev(a);
	int le=strlen(a);
	int tmp=0,i;
	for (i=0;i<le;i++)
	{
		tmp=tmp/10+(a[i]-48)*2;
		b[i]=tmp%10+48;
	}
	while (tmp>=10)
	{
		tmp=tmp/10;
		b[i++]=tmp%10+48;
	}
	b[i]=0;
	strrev(a);
	strrev(b);
}

int arrcom (char a[100],char b[100])
{
	int n,m,i=0;
	n=strlen(a);
	m=strlen(b);
	if (n>m)
	{
		return 1;
	}
	else if (n==m)
	{
		while (i<n&&a[i]==b[i])
		i++;
		if (i<n&&a[i]>b[i])
		return 1;
		else if (i==n)
		return 2;
		else
		return 0;
	}
	else
	return 0;
}

void arrmult(char a[100],int s,char a1[100])
{
	int i,tmp=0;
	strrev(a);
	for (i=0;i<strlen(a);i++)
	{
		tmp=tmp/10+(a[i]-48)*s;
		a1[i]=tmp%10+48;
	}
	while (tmp>0)
	{
		tmp=tmp/10;
		a1[i++]=tmp%10+48;
	}
	while (a1[i-1]=='0') i--;
	a1[i]=0;
	
	strrev(a1);
	strrev(a);
}


void arrsub(char a[100],char b[100],char c[100])
{
	int n,m,i,j;
	strrev(a);
	strrev(b);
	n=strlen(a);
	m=strlen(b);
	for (i=0;i<m;i++)
	{
		if (a[i]<b[i])
		{
			j=i+1;
			while (a[j]==0)j++;
			for (;j>i;j--)
			{
				a[j]--;
				if (j!=i+1)
				a[j-1]=10;
			}
			a[i]=a[i]+10;
		}
		c[i]=a[i]-b[i]+48;
	}
	while  (i<n)
	{
		c[i]=a[i];
		i++;
	}
	while (c[i-1]=='0')i--;
	c[i]='\0';
	strrev(c);
	strrev(b);
}

int next(char a[100])
{
	int tc,i,j,n,x,y;
		n=strlen(a);
		if (n%2==0)
		{
			i=0;
			while (i<=(n-1)/2&&a[(n-1)/2-i]==a[(n-1)/2+1+i])
			i++;
			if (i==(n+1)/2)
			{
				x=0;
				while (x<=(n-1)/2&&a[(n-1)/2-x]=='9')
				{
					a[(n-1)/2-x]=a[(n-1)/2+x+1]='0';
					x++;
				}
				if (x==(n+1)/2)
				{
					a[0]='1';
					a[n]='1';
					a[n+1]=0;
				}
				else
				{
					a[(n-1)/2-x]++;
					a[(n-1)/2+x+1]++;
				}
			}
			else
			{
				if (a[(n-1)/2-i]>a[(n-1)/2+1+i])
				{
					for (y=i;y<=(n-1)/2;y++)
					a[(n-1)/2+1+y]=a[(n-1)/2-y];
				}
				else
				{
					x=0;
					while (x<=(n-1)/2&&a[(n-1)/2-x]=='9')
					{
						a[(n-1)/2-x]=a[(n-1)/2+x+1]='0';
						x++;
					}
					a[(n-1)/2-x]++;
					a[(n-1)/2+x+1]++;
					for (y=x;y<=(n-1)/2;y++)
					a[(n-1)/2+1+y]=a[(n-1)/2-y];
				}
			}
		}
		else
		{
			i=0;
			while (i<=(n-1)/2&&a[(n-1)/2-i]==a[(n-1)/2+i])
			i++;
			if (i==(n+1)/2)
			{
				x=0;
				while (x<=(n-1)/2&&a[(n-1)/2-x]=='9')
				{
					a[(n-1)/2-x]=a[(n-1)/2+x]='0';
					x++;
				}
				if (x==(n+1)/2)
				{
					a[0]='1';
					a[n]='1';
					a[n+1]=0;
				}
				else
				{
					if (x==0);
					else
					a[(n-1)/2-x]++;
					a[(n-1)/2+x]++;
				}
			}
			else
			{
				if (a[(n-1)/2-i]>a[(n-1)/2+i])
				{
					for (y=i;y<=(n-1)/2;y++)
					a[(n-1)/2+y]=a[(n-1)/2-y];
				}
				else
				{
					x=0;
					while (x<=(n-1)/2&&a[(n-1)/2-x]=='9')
					{
						a[(n-1)/2-x]=a[(n-1)/2+x]='0';
						x++;
					}
					if (x==0);
					else
					a[(n-1)/2-x]++;
					a[(n-1)/2+x]++;
					
					for (y=x;y<=(n-1)/2;y++)
					a[(n-1)/2+y]=a[(n-1)/2-y];
				}
			}
		}
}


void sqr(char a[101],char c[101])
{
	int tc;
	arrmulty(a,a,c);
}

void arrmulty(char a[20002],char b[20002],char c[20002])
{
	str(b);
	int n=strlen(b),i,m,p;
	char d[20002];
	arrmul1(a,b[0]-48,c);
	for (i=1;i<n;i++)
	{
		arrmul1(a,b[i]-48,d);
		m=strlen(d);
		for (p=m;p<i+m;p++)
		{
			d[p]=48;
		}
		d[p]=0;
		arradd1(c,d,c);
	}
}

int arradd1(char a[20002],char b[20002],char c[20002])
{
	int tmp,i;
	str(a);
	str(b);
	int n=strlen(a),m=strlen(b);
	if (n>=m)
	{
		tmp=a[0]+b[0]-96;
		for (i=1;i<m;i++)
		{
			c[i-1]=tmp%10+48;
			tmp=a[i]+b[i]-96+tmp/10;
		}
		for (i=m;i<n;i++)
		{
			c[i-1]=tmp%10+48;
			tmp=a[i]+tmp/10-48;
		}
		while(tmp>0)
		{
			c[i-1]=tmp%10+48;
			tmp=tmp/10;
			i++;
		}
	}
	if (m>n)
	{
		tmp=a[0]+b[0]-96;
		for (i=1;i<n;i++)
		{
			c[i-1]=tmp%10+48;
			tmp=a[i]+b[i]+tmp/10-96;
		}
		for (i=n;i<m;i++)
		{
			c[i-1]=tmp%10+48;
			tmp=b[i]+tmp/10-48;
		}
		while(tmp>0)
		{
			c[i-1]=tmp%10+48;
			tmp=tmp/10;
			i++;
		}
	}
	c[i-1]=0;
	str(c);
}

void arrmul1 (char a[20002],int b,char c[20002])
{
	str(a);
	int n,i,tmp=0;
	n=strlen(a);
	tmp=b*(a[0]-48);
	for (i=1;i<n;i++)
	{
		c[i-1]=tmp%10+48;
		tmp=b*(a[i]-48)+tmp/10;
	}
	while(tmp>0)
	{
		c[i-1]=tmp%10+48;
		tmp=tmp/10;
		i++;
	}
	c[i-1]=0;
	str(c);
	str(a);
}

void str(char a[20002])
{
	int i=0,j=strlen(a)-1;
	char t;
	while (i<j)
	{
		t=a[i];
		a[i]=a[j];
		a[j]=t;
		i++;
		j--;
	}
}
