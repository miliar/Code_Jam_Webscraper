#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	char a[10][10];
	int xrow[10][10],xcol[10][10],orow[10][10],ocol[10][10];
	bool flagA,flagB;
	int diag1x,diag2x,diag1o,diag2o;
	int i,j,t,n,cases,sum;
	cin>>cases;
	t=0;n=4;
	while (t<cases)
	{
		sum=0;
		for(i=1;i<=n;i++)
		  for(j=1;j<=n;j++) 
		    {
		    	cin>>a[i][j];
		    	if (a[i][j]!='.') sum++;
		    }
		memset(xrow,0,sizeof(xrow));
		memset(xcol,0,sizeof(xcol));
		memset(orow,0,sizeof(orow));
		memset(ocol,0,sizeof(ocol));
		diag1x=diag2x=diag1o=diag2o=0;
		flagA=false;flagB=false;
		
		for(i=1;i<=n;i++)
		  for(j=1;j<=n;j++)
		    if (a[i][j]=='X'||a[i][j]=='T') xrow[i][j]=xrow[i][j-1]+1;
		    else xrow[i][j]=xrow[i][j-1];
		for(i=1;i<=n;i++)
		  for(j=1;j<=n;j++)
		    if (a[i][j]=='X'||a[i][j]=='T') xcol[i][j]=xcol[i-1][j]+1;
		    else xcol[i][j]=xcol[i-1][j];
		for(i=1;i<=n;i++)
		  for(j=1;j<=n;j++)
		    if (a[i][j]=='O'||a[i][j]=='T') orow[i][j]=orow[i][j-1]+1;
		    else orow[i][j]=orow[i][j-1];
		for(i=1;i<=n;i++)
		  for(j=1;j<=n;j++)
		    if (a[i][j]=='O'||a[i][j]=='T') ocol[i][j]=ocol[i-1][j]+1;
		    else ocol[i][j]=ocol[i-1][j];
		for(i=1;i<=n;i++) if (a[i][i]=='X'||a[i][i]=='T') diag1x++;
		for(i=1;i<=n;i++) if (a[i][i]=='O'||a[i][i]=='T') diag1o++;
		for(i=1;i<=n;i++) if (a[i][n-i+1]=='X'||a[i][n-i+1]=='T') diag2x++;
		for(i=1;i<=n;i++) if (a[i][n-i+1]=='O'||a[i][n-i+1]=='T') diag2o++;
		
		for(i=1;i<=n;i++)
		{
			if (xrow[i][4]==4) flagA=true;
			if (xcol[4][i]==4) flagA=true;
			if (orow[i][4]==4) flagB=true;
			if (ocol[4][i]==4) flagB=true;
		}	
		if (diag1x==4||diag2x==4) flagA=true;
		if (diag1o==4||diag2o==4) flagB=true;
		
		cout<<"Case #"<<++t<<": ";
		if (flagA&&!flagB) cout<<"X won"<<endl;
		else if (flagB&&!flagA) cout<<"O won"<<endl;
		else if (sum==16) cout<<"Draw"<<endl;
		else if (!flagA&&!flagB) cout<<"Game has not completed"<<endl;
	} 
}
