#include<cstdio>
#include<string>
using namespace std;
void print(char bd[4][4])
{
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;++j)printf("%c",bd[i][j]);
		printf("\n");
	}
	printf("\n");
}
string getState(char bd[4][4])
{
	// check each row.
	int x,y;
	for(int i=0;i<4;i++)
	{
		x=0;y=0;
		for(int j=0;j<4;j++)
		{
			switch(bd[i][j])
			{
				case 'X':x++;break;
				case 'O':y++;break;
				case 'T':x++;y++;break;
			}
		}
		if (x==4)
			return "X won";
		if(y==4)
			return "O won";
	}
	
	// check each col.
	for(int i=0;i<4;i++)
	{
		x=0;y=0;
		for(int j=0;j<4;j++)
		{
			switch(bd[j][i])
			{
				case 'X':x++;break;
				case 'O':y++;break;
				case 'T':x++;y++;break;
			}
		}
		if (x==4)
			return "X won";
		if(y==4)
			return "O won";
	}
	
	x=0;y=0;
	// check diagonal 1.
	for(int i=0;i<4;i++)
	{
		switch(bd[i][i])
		{
			case 'X':x++;break;
			case 'O':y++;break;
			case 'T':x++;y++;break;
		}
	}
	if (x==4)
		return "X won";
	if(y==4)
		return "O won";
	
	x=0;y=0;
	// check diagonal 2.
	for(int i=0;i<4;i++)
	{
		switch(bd[i][4-i-1])
		{
			case 'X':x++;break;
			case 'O':y++;break;
			case 'T':x++;y++;break;
		}
	}
	if (x==4)
		return "X won";
	if(y==4)
		return "O won";
	
	// total count
	for(int i =0;i<4;i++)for(int j=0;j<4;j++)if(bd[i][j]=='.')
		return "Game has not completed";
	return "Draw";
}
int main()
{
	int T;
	char bd[4][4];
	scanf(" %d", &T);
	for(int i =0; i<T; ++i)
	{
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				scanf(" %c", &bd[j][k]);
		}
		
		string ans = getState(bd);
		printf("Case #%d: %s\n", i+1, ans.c_str());
		//print(bd);
	}
	return 0;
}
