#include<iostream>
using namespace std;
int row(char a[4][4])
{
	int i,j;
	for(i=0;i<4;i++)
	{
		if((a[i][0]=='X'||a[i][0]=='T')&&(a[i][1]=='X'||a[i][1]=='T')&&(a[i][2]=='X'||a[i][2]=='T')&&(a[i][3]=='X'||a[i][3]=='T'))
		{
			return 1;
		}
		else if((a[i][0]=='O'||a[i][0]=='T')&&(a[i][1]=='O'||a[i][1]=='T')&&(a[i][2]=='O'||a[i][2]=='T')&&(a[i][3]=='O'||a[i][3]=='T'))
		{
			return 2;
		}
	}
	return 0;
}
int col(char a[4][4])
{
	int i,j;
	for(i=0;i<4;i++)
	{
		if((a[0][i]=='X'||a[0][i]=='T')&&(a[1][i]=='X'||a[1][i]=='T')&&(a[2][i]=='X'||a[2][i]=='T')&&(a[3][i]=='X'||a[3][i]=='T'))
		{
			return 1;
		}
		else if((a[0][i]=='O'||a[0][i]=='T')&&(a[1][i]=='O'||a[1][i]=='T')&&(a[2][i]=='O'||a[2][i]=='T')&&(a[3][i]=='O'||a[3][i]=='T'))
		{
			return 2;
		}
	}
	return 0;
}
int diag(char a[4][4])
{
	int i,j;
	if((a[0][0]=='X'||a[0][0]=='T')&&(a[1][1]=='X'||a[1][1]=='T')&&(a[3][3]=='X'||a[3][3]=='T')&&(a[2][2]=='X'||a[2][2]=='T'))
		return 1;
	else if((a[0][0]=='O'||a[0][0]=='T')&&(a[1][1]=='O'||a[1][1]=='T')&&(a[2][2]=='O'||a[2][2]=='T')&&(a[3][3]=='O'||a[3][3]=='T'))
		return 2;
	else
		return 0;
}
int diag2(char a[4][4])
{
	int i,j;
	if((a[0][3]=='X'||a[0][3]=='T')&&(a[1][2]=='X'||a[1][2]=='T')&&(a[2][1]=='X'||a[2][1]=='T')&&(a[3][0]=='X'||a[3][0]=='T'))
		return 1;
	else if((a[0][3]=='O'||a[0][3]=='T')&&(a[1][2]=='O'||a[1][2]=='T')&&(a[2][1]=='O'||a[2][1]=='T')&&(a[3][0]=='O'||a[3][0]=='T'))
		return 2;
	else
		return 0;
}
int incomp(char a[4][4])
{
	int i,j;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(a[i][j]=='.')
				return 1;
		}
	}
	return 0;
}
int main()
{
	char a[4][4];
	int i,j,k,n,w[1000],r,c,d,d2;
	cin>>n;
	for(i=0;i<n;i++)
	{
		for(k=0;k<4;k++)
		for(j=0;j<4;j++)
			cin>>a[k][j];
		r=row(a);
		c=col(a);
		d=diag(a);
		d2=diag2(a);
		if(r==1||c==1||d==1||d2==1)
			w[i]=1;
		else if(r==2||c==2||d==2||d2==2)
			w[i]=2;
		else if(incomp(a))
			w[i]=3;
		else
			w[i]=0;
	}
	for(i=0;i<n;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		if(w[i]==1)
			cout<<"X won";
		if(w[i]==2)
			cout<<"O won";
		if(w[i]==3)
			cout<<"Game has not completed";
		if(w[i]==0)
			cout<<"Draw";
		cout<<"\n";
	}
	return 0;
}



