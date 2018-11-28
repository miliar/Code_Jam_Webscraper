#include<iostream.h>
#include<stdio.h>
void tac(int );
int TIC,i,j,k,CAP[1000],JHANDA,CNT=0;;
char TOE[1000][4][4];

void main()
{
	freopen("Alarge.in","r",stdin);
	freopen("alarge.out","w",stdout);
	cin>>TIC;
	for(i=0;i<TIC;i++)
	{
		CAP[i]=0;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				cin>>TOE[i][j][k];
				if(TOE[i][j][k]=='T')
				{
					CAP[i]++;
				}
			}
		}
	}
	for(i=0;i<TIC;i++)
	{
		if(CAP[i]>1)
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"There can be only one T\n";
		}
		else
		{
			JHANDA=0;
			tac(JHANDA);
		}
	}
}
void tac(int JHANDA)
{
	for(j=0;j<4;j++)
	{
		if((TOE[i][j][0]=='X'||TOE[i][j][0]=='T')&&(TOE[i][j][1]=='X'||TOE[i][j][1]=='T')&&(TOE[i][j][2]=='X'||TOE[i][j][2]=='T')&&(TOE[i][j][3]=='X'||TOE[i][j][3]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"X won\n";
			JHANDA=1;
			if(JHANDA==1)
			{
				break;
			}
		}
		else if((TOE[i][j][0]=='O'||TOE[i][j][0]=='T')&&(TOE[i][j][1]=='O'||TOE[i][j][1]=='T')&&(TOE[i][j][2]=='O'||TOE[i][j][2]=='T')&&(TOE[i][j][3]=='O'||TOE[i][j][3]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"O won\n";
			JHANDA=1;
			if(JHANDA==1)
			{
				break;
			}
		}
	}
	if(JHANDA==0)
	{
	for(k=0;k<4;k++)
	{
		if((TOE[i][0][k]=='X'||TOE[i][0][k]=='T')&&(TOE[i][1][k]=='X'||TOE[i][1][k]=='T')&&(TOE[i][2][k]=='X'||TOE[i][2][k]=='T')&&(TOE[i][3][k]=='X'||TOE[i][3][k]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"X won\n";
			JHANDA=1;
			if(JHANDA==1)
			{
				break;
			}
		}
		else if((TOE[i][0][k]=='O'||TOE[i][0][k]=='T')&&(TOE[i][1][k]=='O'||TOE[i][1][k]=='T')&&(TOE[i][2][k]=='O'||TOE[i][2][k]=='T')&&(TOE[i][3][k]=='O'||TOE[i][3][k]=='T'))
		{
			cout<<"Case #"<<i+1<<": ";
			cout<<"O won\n";
			JHANDA=1;
			if(JHANDA==1)
			{
				break;
			}
		}


	}
	}
      if(JHANDA==0)
      {
	if((TOE[i][1][1]=='X'||TOE[i][1][1]=='T')&&(TOE[i][2][2]=='X'||TOE[i][2][2]=='T')&&(TOE[i][3][3]=='X'||TOE[i][3][3]=='T')&&(TOE[i][0][0]=='X'||TOE[i][0][0]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"X won\n";
		JHANDA=1;
	}
      }
      if(JHANDA==0)
      {
	/*else*/ if((TOE[i][1][1]=='O'||TOE[i][1][1]=='T')&&(TOE[i][2][2]=='O'||TOE[i][2][2]=='T')&&(TOE[i][3][3]=='O'||TOE[i][3][3]=='T')&&(TOE[i][0][0]=='O'||TOE[i][0][0]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"O won\n";
		JHANDA=1;
	}
      }
    if(JHANDA==0)
    {
	if((TOE[i][1][2]=='X'||TOE[i][1][2]=='T')&&(TOE[i][2][1]=='X'||TOE[i][2][1]=='T')&&(TOE[i][3][0]=='X'||TOE[i][3][0]=='T')&&(TOE[i][0][3]=='X'||TOE[i][0][3]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"X won\n";
		JHANDA=1;
	}
    }
    if(JHANDA==0)
    {
       /*	else*/ if((TOE[i][1][2]=='O'||TOE[i][1][2]=='T')&&(TOE[i][2][1]=='O'||TOE[i][2][1]=='T')&&(TOE[i][3][0]=='O'||TOE[i][3][0]=='T')&&(TOE[i][0][3]=='O'||TOE[i][0][3]=='T'))
	{
		cout<<"Case #"<<i+1<<": ";
		cout<<"O won\n";
		JHANDA=1;
	}
    }
	if(JHANDA==0)
	{
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(TOE[i][j][k]=='.')
				{
					CNT++;
				}
			}
		}
		if(CNT>0)
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
	CNT=0;
}

