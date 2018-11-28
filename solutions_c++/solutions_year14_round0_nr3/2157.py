#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int n,n2,m2,m,k,i,j,t,a,l,b[100][100];
	ifstream fcin("txt.in");
	ofstream fcout("txt.out");
	fcin>>a;
	for(l=1;l<=a;l++)
	{
	 fcout<<"Case #"<<l<<":\n";
	fcin>>n;n2=n;
	fcin>>m;m2=m;
	if(n>m){k=n;n=m;m=k;}
	fcin>>k;
	k=n*m-k;
	t=k/m*m;
	k=k-t;
	if(n==1)
		{for(i=1;i<=m;i++)
			if(i==1)b[1][i]='c';
			else if(i<=t+k)b[1][i]='.';
		else b[1][i]='*';
		}
	else if(n==2)
			if(((t+k)%2==1||t+k==2)&&t+k!=1){fcout<<"Impossible\n";b[1][1]='m';}
			else 
				for(i=1;i<=n;i++)
					{
					 for(j=1;j<=m;j++)
						if(i+j==2)b[i][j]='c';
						else if(j<=(t+k)/2)b[i][j]='.';
						else b[i][j]='*';
					}
			
	else if(t>=2*m)
		if(t+k==7||t+k==5||t+k==3||t+k==2){fcout<<"Impossible\n";b[1][1]='m';}
		else {
		for(i=1;i<=t/m;i++)
		{
			for(j=1;j<=m;j++)
			if(i+j==2)b[i][j]='c';
			else 
			if(i!=t/m||j!=m)
				 b[i][j]='.';
		}
	if(k==1&&t/m!=2){k++;b[t/m][m]='*';}
	else if(k==1&&t/m==2){k=k+2;b[t/m][m]='*';b[t/m-1][m]='*';}
	else {b[t/m][m]='.';j++;}
	for(j=1;j<=m;j++)
	if(j<=k)b[t/m+1][j]='.';
	else b[t/m+1][j]='*';
	for(i=t/m+2;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			b[i][j]='*';
		}
	}
	else if((t+k)%2==0)
	{
		if(t+k==2){fcout<<"Impossible\n";b[1][1]='m';}
		else 
		{
			for(i=1;i<=2;i++)
				{
					for(j=1;j<=m;j++)
						if(i+j==2)b[i][j]='c';
					else if(j<=(t+k)/2)b[i][j]='.';
					else b[i][j]='*';
				}
			for(i=3;i<=n;i++)
				{
					for(j=1;j<=m;j++)
						b[i][j]='*';
				}
		}
	}
	else 
	{
		if(t+k<=7&&t+k>1)
			{fcout<<"Impossible\n";b[1][1]='m';}
		else if(k==1)
			for(i=1;i<=n;i++)
				for(j=1;j<=m;j++)
					if(i+j==2)b[i][j]='c';
				    else b[i][j]='*';
		else{ if (k%2==0)
				if(k==0){t=t-3;k=3;}
				else {k--;t++;}
				if(k==1)
				{k=k+2;
				 t=t-2;}
				else {t=t+k-3;k=3;}
				for(i=1;i<=n;i++)
					{
						for(j=1;j<=m;j++)
							if(i+j==2)b[i][j]='c';
						else if(i<3&&j<=t/2)b[i][j]='.';
						    else if(i==3&&j<=k)b[i][j]='.';
							else b[i][j]='*';
					}
			}
	}
	if(b[1][1]=='c')
		if(n2<m2)
			for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			fcout<<(char)b[i][j];
			fcout<<'\n';
		}
		else 
			for(i=1;i<=n2;i++)
		{
			for(j=1;j<=m2;j++)
			fcout<<(char)b[j][i];
			fcout<<'\n';
		}
	}
	return 0;
}