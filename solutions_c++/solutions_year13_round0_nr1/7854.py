#include <iostream>

char check(char p1,char p2,char p3,char p4)
{
	char p[4]={p1,p2,p3,p4};
	char s=0;
	for (int i=0;i<4;i++)
	{
		if(p[i]=='T')
		{
			continue;
		}

		if (p[i]=='.')
		{
			return 0;
		}

		if (s==0)
		{
			s=p[i];
		}
		else if (s!=p[i])
		{
			return 0;
		}
	}
	return s;
}


void main()
{

	int T;
	std::cin>>T;
	char tmp;
	for(int t=0;t<T;t++)
	{
		
		char board[4][4]={0};
		int full=1;
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				std::cin>>board[i][j];
				if (board[i][j]=='.')
				{
					full=0;
				}
			}
		}
		//std::cin>>tmp;

		int r=0;

		for (int i=0;i<4;i++)
		{
			r=check(board[i][0],board[i][1],board[i][2],board[i][3]);
			if (r!=0)
			{
				break;
			}
			r=check(board[0][i],board[1][i],board[2][i],board[3][i]);
			if (r!=0)
			{
				break;
			}
		}

		if (r==0)
		{
			
			r=check(board[0][0],board[1][1],board[2][2],board[3][3]);
			if (r==0)
			{
				r=check(board[0][3],board[1][2],board[2][1],board[3][0]);
			}
		}
		std::cout<<"Case #"<<t+1<<": ";

		if(r!=0)
		{
			char str[2]={r,0};
			std::cout<<str<<" won";
		}
		else if (full==1)
		{
			std::cout<<"Draw";
		}
		else
		{
			std::cout<<"Game has not completed";
		}
		std::cout<<std::endl;

	}
}