#include<iostream>
#include<cstdio>

using namespace std;

char A[4][4];
void llena()
{
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			A[i][j]='.';
}

char hor(int x)
{
	int con=0;
	char tmp=A[x][0];
		if(tmp=='T')
			tmp=A[x][1];
	for(int i=0;i<4;i++)
		if(A[x][i]==tmp ||A[x][i]=='T')
			con++;
	if(con==4)
		return tmp;
	return '0';	
}

char ver(int y)
{
	int con=0;
	char tmp=A[0][y];
		if(tmp=='T')
			tmp=A[1][y];
	for(int i=0;i<4;i++)
		if(A[i][y]==tmp ||A[i][y]=='T')
			con++;
	if(con==4)
		return tmp;
	return '0';	
}



char busq()
{
	for(int i=0;i<4;i++)
	{
		if(hor(i)=='X' || hor(i)=='O')
			return hor(i);
		if(ver(i)=='X' || ver(i)=='O')
			return ver(i);	
	}
	char tmp=A[0][0]; //diag1
	int con=0;
	if(tmp=='T')
		tmp=A[1][1];
	for(int i=0;i<4;i++)
		if(A[i][i]==tmp ||A[i][i]=='T')
			con++;
	if(con==4)
		return tmp;	
	
	tmp=A[0][3]; //diag2
	con=0;
	if(tmp=='T')
		tmp=A[1][2];
	for(int i=0;i<4;i++)
		if(A[i][3-i]==tmp ||A[i][3-i]=='T')
			con++;
	if(con==4)
		return tmp;
	
	con=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(A[i][j]!='.')
				con++;
	if(con==16)
		return '1';
	return '2';
}

int main()
{
	int t;
	char qq;
	scanf("%d",&t);
	for(int q=1;q<=t;q++)
	{
		llena();
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>A[i][j];
		printf("Case #%d: ",q);
		qq=busq();
		if( qq=='X' || qq=='O')
			printf("%c won\n",qq);
		else if(qq=='1')
			puts("Draw");
		else
			puts("Game has not completed");
	}
}
