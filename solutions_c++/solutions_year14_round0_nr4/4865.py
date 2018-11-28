#include<iostreamd.h>
#include<conio.h>
#include<stdio.h>
#include<fstream.h>
void main()
{
clrscr();
int n,i,j,test;
float a[100],b[100];
freopen("ppp.in","r",stdin);
freopen("res.txt","w",stdout);
cin>>test;
for(int c1=1;c1<=test;c1++)
{
cin>>n;
for(i=0;i<n;i++)
cin>>a[i];
for(i=0;i<n;i++)
cin>>b[i];
for(i=0;i<n-1;i++)
{
for(j=0;j<n-i-1;j++)
{
if(a[j]<a[j+1])
{
float tmp=a[j];
a[j]=a[j+1];
a[j+1]=tmp;
}
}
}
for(i=0;i<n-1;i++)
{
for(j=0;j<n-i-1;j++)
{
if(b[j]<b[j+1])
{
float tmp=b[j];
b[j]=b[j+1];
b[j+1]=tmp;
}
}
}
int res=0,res1=0;
float c[100];
for(i=0;i<n;i++)
c[i]=b[i];
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(a[i]>c[j]&&c[j]!=-1)
{
c[j]=-1;
res1++;
break;
}
}
}
for(i=0;i<n;i++)
{
int flag=0;
for(j=0;j<n;j++)
{
if(flag==1)
break;
if(a[i]>b[j]&&b[j]!=-1)
{
	res++;
	for(int k=n-1;k>=0;k--)
	{
	if(b[k]!=-1)
	{
		b[k]=-1;
		flag=1;
		break;
	}
	}
}
else if(a[i]<b[j])
{
	b[j]=-1;
	flag=1;
}
}
}
cout<<"Case #"<<c1<<": "<<res1<<" "<<res<<endl;
}
getch();
}