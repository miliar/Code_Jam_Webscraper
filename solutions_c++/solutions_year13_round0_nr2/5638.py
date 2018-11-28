#include<fstream.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<iomanip.h>
#include<ctype.h>
#include<process.h>
#include<stdio.h>
#include<stdlib.h>
#include<iostream.h>
int fu()
{int a[10][10];int l=0;
int r;
cin>>r;
int c;
cin>>c;
int i,j,k,g,h,m=0;
	for(i=0;i<r;i++)
	       for(j=0;j<c;j++)
			cin>>a[i][j];

for(i=0;i<r;i++)
for(j=0;j<c;j++)
if(a[i][j]==1)
{g=0;h=0;
for(l=0;l<r;l++)
if(a[l][j]==2)
 g=1;

 for(k=0;k<c;k++)
 if(a[i][k]==2)
 h=1;

if((g==1)&&(h==1))
m=1;
}
if(m==1)
return 0;
else
return 1;
}


void main()
{clrscr();
int n;
cin>>n;
int b[100],k=0;
for(int i=0;i<n;i++)
b[k++]=fu();
for(int j=0;j<k;j++)
{cout<<"Case #"<<j+1<<": ";
if(b[j]==0)
cout<<"No";
else if(b[j]==1)
cout<<"Yes";
}
getch();
}