#include<cstdio>
#include<cstring>
int A[4][4];
char res()
{
	getchar();
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			char temp=getchar();
			switch(temp)
			{
			case 'X':
				A[i][j]=1;
				break;
			case 'O':
				A[i][j]=100;
				break;
			case 'T':
				A[i][j]=10;
				break;
			case '.':
				A[i][j]=0;
				break;
			default:
				A[i][j]=500;
				break;
		    }	
		}
		getchar();
	}
	for(int i=0;i<4;i++)
	{
		int sum=0;
		for(int j=0;j<4;j++)
		{
			sum+=A[i][j];
		}
		if(sum==4||sum==13)
			return 'X';
		else if(sum==400||sum==310)
			return 'O';
	}
	for(int i=0;i<4;i++)
	{
		int sum=0;
		for(int j=0;j<4;j++)
		{
			sum+=A[j][i];
		}
		if(sum==4||sum==13)
			return 'X';
		else if(sum==400||sum==310)
			return 'O';
	}
	int s=A[0][0]+A[1][1]+A[2][2]+A[3][3];
	if(s==4||s==13)
		return 'X';
	else if(s==400||s==310)
		return 'O';
	s=A[0][3]+A[1][2]+A[2][1]+A[3][0];
	if(s==4||s==13)
		return 'X';
	else if(s==400||s==310)
		return 'O';
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(A[i][j]==0)
				return 'N';
		}
	}
	return 'D';	
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	int test;
	scanf("%d",&test);
	int i=0;
	while(test--)
	{
		i++;
		char sol[30];
		char p=res();
		switch(p)
		{
			case 'X':
			{strcpy(sol,"X won");break; }
			case 'O':
				{strcpy(sol,"O won");break;}
			case 'N':
				{strcpy(sol,"Game has not completed");break;}
			case 'D':
				{strcpy(sol,"Draw");break;}
			default:
				break;
		}
		printf("Case #%d: %s\n",i,sol);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
