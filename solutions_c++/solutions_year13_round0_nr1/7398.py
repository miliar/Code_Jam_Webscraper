#include <fstream.h>
#include <iostream.h>

#define DOT 0
#define T 1
#define X 2
#define O 3


int main()
{
	ifstream cin ("A-large.in");
	ofstream cout ("A-large.out");
	
	int cases;
	cin>>cases;
	int map[4][4];
	//0 .
	//1 T
	//2 X
	//3 O
	
	char line[4][10];
	int n;
	
	
	for(int t=1; t<=cases; t++)
	{
		n=0;
		for(int i=0;i<4;i++)
		cin>>line[i];
		
		for(int i=0;i<4;i++)
		{
			for(int j=0; j<4; j++)
			{
				switch(line[i][j])
				{
				case '.':
					map[i][j]=0;
					n++;
					break;
				case 'T':
					map[i][j]=1;
					break;
				case 'X':
					map[i][j]=2;
					break;
				case 'O':
					map[i][j]=3;
					break;
				}
			}
		}

		int winflag=0;
		//check every line
		for(int S=X; S<=O; S++)
		{
			int i,j;
			winflag=0;
			for(i=0; i<4; i++)
			{
				for(j=0; j<4; j++)
				{
					if(map[i][j]!=T && map[i][j]!=S)
						break;
				}
				if(j==4)
				{
					//S WIN;
					winflag =1;
					if(S==X)
					{
						cout<<"Case #"<<t<<": X won"<<endl;
					}
					else
					{
						cout<<"Case #"<<t<<": O won"<<endl;
					}
				}
			}
			if(winflag==1)
				break;
			for(i=0;i<4; i++)
			{
				for(j=0; j<4; j++)
				{
					if(map[j][i]!=T && map[j][i]!=S)
						break;
				}
				if(j==4)
				{
					//S WIN;
					winflag=1;
					if(S==X)
					{
						cout<<"Case #"<<t<<": X won"<<endl;
					}
					else
					{
						cout<<"Case #"<<t<<": O won"<<endl;
					}
				}
			}
			if(winflag==1)
				break;
			for(j=0;j<4; j++)
			{
				if(map[j][j]!=T && map[j][j]!=S)
					break;
			}
			if(j==4)
			{
				//S WIN;
				winflag=1;
				if(S==X)
				{
					cout<<"Case #"<<t<<": X won"<<endl;
				}
				else
				{
					cout<<"Case #"<<t<<": O won"<<endl;
				}
				break;
			}
			for(j=0;j<4; j++)
			{
				if(map[3-j][j]!=T && map[3-j][j]!=S)
					break;
			}
			if(j==4)
			{
				//S WIN;
				winflag=1;
				if(S==X)
				{
					cout<<"Case #"<<t<<": X won"<<endl;
				}
				else
				{
					cout<<"Case #"<<t<<": O won"<<endl;
				}
				break;
			}
		}
		if(winflag == 0)
		{
			if(n==0)
			{
				cout<<"Case #"<<t<<": Draw"<<endl;
			}
			else
			{
				cout<<"Case #"<<t<<": Game has not completed"<<endl;
			}
		}
	}
	cin.close();
	cout.close();
	
	return 0;
}