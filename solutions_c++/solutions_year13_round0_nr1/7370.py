#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int tst,i,j,flag=0,l=0,m=0,n=0,q=0,p=0;
	int x[2],o[2],t[2],no[2];
	char a[4][4];
	scanf("%d",&tst);	
	while(tst--)
	{p++;
	flag=0;
	for(i=0;i<4;i++)
	scanf("%s",a[i]);
	for(i=0;i<4;i++)
        {
        l=m=n=q=0;
        memset(x,0,sizeof x);
        memset(o,0,sizeof o);
        memset(t,0,sizeof t);
        for(j=0;j<4;j++)
        {
        if(a[i][j]=='X')
        x[l++];
        else if(a[i][j]=='O')
        o[m++];
        else if(a[i][j]=='T')
        t[n++];
        else
        no[q++];
        }
	if(flag==0 ||flag==3)
	{
        if(l==4 || (l==3 && n==1))
        {flag=1;break;}
        else if(m==4 || (m==3 && n==1))
        {flag=2;break;}
        else if(q>0)
        flag=3;
        }}
	if(flag==0 || flag==3)
	{
        for(i=0;i<4;i++)
        {
        l=m=n=q=0;
        memset(x,0,sizeof x);
        memset(o,0,sizeof o);
        memset(t,0,sizeof t);
        for(j=0;j<4;j++)
        {
        if(a[j][i]=='X')
        x[l++];
        else if(a[j][i]=='O')
        o[m++];
        else if(a[j][i]=='T')
        t[n++];
        }
	if(flag==0||flag==3)
	{
        if(l==4 || (l==3 && n==1))
        {flag=1;break;}
        else if(m==4 || (m==3 && n==1))
        {flag=2;break;}
        }}}
	if(flag==0 || flag==3)
	{
        l=m=n=q=0;
        memset(x,0,sizeof x);
        memset(o,0,sizeof o);
        memset(t,0,sizeof t);
        for(i=0;i<4;i++)
	{
	for(j=0;j<4;j++)
	{
	if(i==j)
	{
	if(a[i][j]=='X')
        x[l++];
        else if(a[i][j]=='O')
        o[m++];
        else if(a[i][j]=='T')
        t[n++];
	}}}
	if(l==4 || (l==3 && n==1))
        flag=1;
        else if(m==4 || (m==3 && n==1))
        flag=2;
	}
	if(flag==0 || flag==3)
        {
        l=m=n=q=0;
        memset(x,0,sizeof x);
        memset(o,0,sizeof o);
        memset(t,0,sizeof t);
        for(i=0;i<4;i++)
        {
        for(j=0;j<4;j++)
        {
        if(i+j==3)
        {
        if(a[i][j]=='X')
        x[l++];
        else if(a[i][j]=='O')
        o[m++];
        else if(a[i][j]=='T')
        t[n++];
        }}}
        if(l==4 || (l==3 && n==1))
        flag=1;
        else if(m==4 || (m==3 && n==1))
        flag=2;
        }
	printf("Case #%d: ",p);
	if(flag==0)
	printf("Draw\n");
	else if(flag==1)
	printf("X won\n");
	else if(flag==2)
	printf("O won\n");
	else if(flag==3)
	printf("Game has not completed\n");
	}
	return 0;
}



	
	
	
	
