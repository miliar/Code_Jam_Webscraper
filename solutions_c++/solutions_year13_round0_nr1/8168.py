#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<fstream.h>
int dev;
int X(int ds[4][4])
{
	int i,j,k1=0,k2=0;
	for(i=0;i<4;i++)
	{
		k1=0;
		k2=0;
		for(j=0;j<4;j++)
		{
			if(ds[i][j]==1)
				k1++;
			if(ds[j][i]==1)
				k2++;
		}
		if(k1==4 || k2==4)
			break;
	}
	if(k1==4 || k2==4)
		return 1;
	k1=0;
	k2=0;
	for(i=0;i<4;i++)
	{
		if(ds[i][i]==1)
			k1++;
		if(ds[i][4-i-1]==1)
			k2++;
	}
	if(k1==4 || k2==4)
		return 1;
	else
		return 0;
}
int O(int ds[4][4])
{
	int i,j,k1=0,k2=0;
	for(i=0;i<4;i++)
	{
		k1=0;
		k2=0;
		for(j=0;j<4;j++)
		{
			if(ds[i][j]==2)
				k1++;
			if(ds[j][i]==2)
				k2++;
		}
		if(k1==4 || k2==4)
			break;
	}
	if(k1==4 || k2==4)
		return 1;
	k1=0;
	k2=0;
	for(i=0;i<4;i++)
	{
		if(ds[i][i]==2)
			k1++;
		if(ds[i][4-i-1]==2)
			k2++;
	}
	if(k1==4 || k2==4)
		return 1;
	else
		return 0;
}
void main()
{
	clrscr();
	int i,n,j,k,x,y,h;
	char **s,d[4][5];
	int ds[4][4];
	char ch,el[50];
	ifstream f1;
	f1.open("Code_Jam\\IS1.in");
	ofstream f2;
	f2.open("Code_Jam\\OS1.out");
	f1>>n;
	f1.getline(el,50,'\n');
	s=new char*[n];
	for(i=0;i<n;i++)
	{
		s[i]=new char[25];
		for(j=0;j<4;j++)
		{
			f1.getline(d[j],5,'\n');
			f1.getline(el,50,'\n');
			for(k=0;k<4;k++)
			{
				ch=d[j][k];
				if(ch=='X')
					ds[j][k]=1;

				else if(ch=='O')
					ds[j][k]=2;
				else if(ch=='.')
					ds[j][k]=0;
				else if(ch=='T')
				{
					ds[j][k]=3;
					x=j;
					y=k;
				}
			}
		}
		for(j=0;j<4;j++)
			cout<<d[j]<<"\n";
		getch();
		h=0;
		ds[x][y]=1;
		if(X(ds)==1)
		{
			strcpy(s[i],"X won");
			h=1;
		}
		ds[x][y]=2;
		if(O(ds)==1)
		{
			strcpy(s[i],"O won");
			h=1;
		}
		if(h==0)
		{
		dev=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(ds[j][k]==0)
					dev=1;
			}
		}
		if(dev==1)
			strcpy(s[i],"Game has not completed");
		else if(dev==0)
			strcpy(s[i],"Draw");
		}
		f1.getline(el,50,'\n');

	}
	cout<<"\n\n\n";
	for(i=0;i<n;i++)
	{
		f2<<"Case #"<<(i+1)<<": "<<s[i]<<"\n";
		cout<<"Case #"<<(i+1)<<": "<<s[i]<<"\n";
	}
	for(i=0;i<n;i++)
		delete []s[i];
	f1.close();
	f2.close();
	getch();
}