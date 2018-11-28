

#include <stdio.h>
#include <iostream>

using namespace std;


FILE *fp;



typedef union
{
	char buf[16];
	char board[4][4];
}game;

char temp;

game g;


#define xwon  "X won\0"
#define owon  "O won\0"
#define draw  "Draw\0"
#define nyc   "Game has not completed\0"

char rs[4][30] = {nyc, xwon, owon, draw};

typedef enum
{
	NYC,
	XWON,
	OWON,
	DRAW
}game_states;


int main()
{
	int t;
	
	//fp = fopen("A-small.in", "r");
	//fp = fopen("A-large.in", "r");

	//fscanf(fp, "%d", &t);
	//fscanf(fp, "%d", &t);

	cin >> t;
	//cout << t << "\n";
	
	
	int i = 1;
	
	for(; i <= t; i++)
	{
		int result = DRAW;
	
		int j,k,l,m,n;
		
		//cin >> temp;
		//cout << "s *** " << endl;
		
		int game_progress = 16;
		
		
		int Xr[] = {0,0,0,0};
		int Xc[] = {0,0,0,0};
		int Xd1 = 0, Xd2 = 0;
		int Xtot = 0;
		
		int Or[] = {0,0,0,0};
		int Oc[] = {0,0,0,0};
		int Od1 = 0, Od2 = 0;
		int Otot = 0;
		
		int count = 0;
		
		for(int r = 0; r < 4; r++)
		{
			for(int c = 0; c < 4; c++)
			{
				cin >> temp;
				
				//cout << "cs - " << temp << endl;
				while(temp == '\n')
				{
					//cout << "csn - " << temp << endl;
					cin >> temp;
				}
				
				//cout << "cc - " << temp << endl;
				
				count++;
				
				if((temp == 'X') || (temp == 'T'))
				{
					Xtot++;
					Xr[r]++;
					Xc[c]++;
				
					if(r == c)
					{
						Xd1++;
					}
					if((r + c) == 3)
					{
						Xd2++;
					}

					/*
					cout << "Xr[" << r << "]: " << Xr[r] << endl;
					cout << "Xc[" << c << "]: " << Xc[c] << endl;
					cout << "Xtot: " << Xtot << endl;
					cout << "Xd1: "<< Xd1 << endl;
					cout << "Xd2: "<< Xd2 << endl << endl;
					*/
					
					if ((Xr[r] == 4) || (Xc[c] == 4) || (Xd1 == 4) || (Xd2 == 4))
					{
						result = XWON;
						c = 4;
						r = 4;
						continue;
					}
					
					
					
				}
				if((temp == 'O') || (temp == 'T'))
				{
					Otot++;
					Or[r]++;
					Oc[c]++;
					
					if(r == c)
					{
						Od1++;
					}
					if((r + c) == 3)
					{
						Od2++;
					}
					
					/*
					cout << "Or[" << r << "]: " << Or[r] << endl;
					cout << "Oc[" << c << "]: " << Oc[c] << endl;
					cout << "Otot: " << Otot << endl;
					cout << "Od1: "<< Od1 << endl;
					cout << "Od2: "<< Od2 << endl << endl;					
					*/
					
					
					if ((Or[r] == 4) || (Oc[c] == 4) || (Od1 == 4) || (Od2 == 4))
					{
						result = OWON;
						c = 4;
						r = 4;
						
						continue;
						
					}
					
				}
				
				if(temp == '.')
				{
					result = NYC;
				}
			}
			
			
		}
		


		while(count < 16)
		{
			cin >> temp;
			while(temp == '\n')
			{
				//cout << "cen - " << temp << endl;
				cin >> temp;
			}
			
			//cout << "cep - " << temp << endl;
			
			count++;
		}
		
		
		cout << "Case #" << i << ": " << rs[result] << endl;
	
		
	

		
		//cout <<endl;
	
	
	}
	
	
	return 0;
}



