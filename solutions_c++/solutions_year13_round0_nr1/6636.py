#include<iostream.h>
#include<stdio.h>
void tic(int );
int T,i,j,k,gin[1000],flag,gin1=0;;
char a[1000][4][4];

void main()
{
	freopen("s1.in","r",stdin);
	freopen("gad.out","w",stdout);
	cin>>T;
	for(i=0;i<T;i++)
	{
		gin[i]=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>a[i][j][k];
				if(a[i][j][k]=='T')
				{
					gin[i]++;
				}
			}
		}
	}
	for(i=0;i<T;i++)
	{
		if(gin[i]>1)
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"There can be only one T\n";
		}
		else
		{
			flag=0;
			tic(flag);
		}
	}
}
void tic(int flag)
{
	for(j=0;j<4;j++)
	{
		if((a[i][j][0]=='X'||a[i][j][0]=='T')&&(a[i][j][1]=='X'||a[i][j][1]=='T')&&(a[i][j][2]=='X'||a[i][j][2]=='T')&&(a[i][j][3]=='X'||a[i][j][3]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"X won\n";
			flag=1;
			if(flag==1)
			{
				break;
			}
		}
		else if((a[i][j][0]=='O'||a[i][j][0]=='T')&&(a[i][j][1]=='O'||a[i][j][1]=='T')&&(a[i][j][2]=='O'||a[i][j][2]=='T')&&(a[i][j][3]=='O'||a[i][j][3]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"O won\n";
			flag=1;
			if(flag==1)
			{
				break;
			}
		}
	}
	if(flag==0)
	{
	for(k=0;k<4;k++)
	{
		if((a[i][0][k]=='X'||a[i][0][k]=='T')&&(a[i][1][k]=='X'||a[i][1][k]=='T')&&(a[i][2][k]=='X'||a[i][2][k]=='T')&&(a[i][3][k]=='X'||a[i][3][k]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"X won\n";
			flag=1;
			if(flag==1)
			{
				break;
			}
		}
		else if((a[i][0][k]=='O'||a[i][0][k]=='T')&&(a[i][1][k]=='O'||a[i][1][k]=='T')&&(a[i][2][k]=='O'||a[i][2][k]=='T')&&(a[i][3][k]=='O'||a[i][3][k]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"O won\n";
			flag=1;
			if(flag==1)
			{
				break;
			}
		}


	}
	}
      if(flag==0)
      {
	if((a[i][1][1]=='X'||a[i][1][1]=='T')&&(a[i][2][2]=='X'||a[i][2][2]=='T')&&(a[i][3][3]=='X'||a[i][3][3]=='T')&&(a[i][0][0]=='X'||a[i][0][0]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"X won\n";
		flag=1;
	}
      }
      if(flag==0)
      {
	/*else*/ if((a[i][1][1]=='O'||a[i][1][1]=='T')&&(a[i][2][2]=='O'||a[i][2][2]=='T')&&(a[i][3][3]=='O'||a[i][3][3]=='T')&&(a[i][0][0]=='O'||a[i][0][0]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"O won\n";
		flag=1;
	}
      }
    if(flag==0)
    {
	if((a[i][1][2]=='X'||a[i][1][2]=='T')&&(a[i][2][1]=='X'||a[i][2][1]=='T')&&(a[i][3][0]=='X'||a[i][3][0]=='T')&&(a[i][0][3]=='X'||a[i][0][3]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"X won\n";
		flag=1;
	}
    }
    if(flag==0)
    {
       /*	else*/ if((a[i][1][2]=='O'||a[i][1][2]=='T')&&(a[i][2][1]=='O'||a[i][2][1]=='T')&&(a[i][3][0]=='O'||a[i][3][0]=='T')&&(a[i][0][3]=='O'||a[i][0][3]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"O won\n";
		flag=1;
	}
    }
	if(flag==0)
	{
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[i][j][k]=='.')
				{
					gin1++;
				}
			}
		}
		if(gin1>0)
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"Game has not completed\n";
		}
		else
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"Draw\n";
		}
	}
	gin1=0;
}

