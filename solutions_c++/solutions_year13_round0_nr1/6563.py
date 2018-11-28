#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <cstring>
#include <string>

using namespace std;

#define HOME_PC
#define BOARD_SIZE 16

int main()
{
	int t,y=0;
	//16 bits to denote the positions of Xs, Os, and board Ts
	unsigned short winPos[] = {0x000F,0x00F0,0x0F00,0xF000,0x1111,0x2222,0x4444,0x8888,0x1248,0x8421};
	
#ifdef HOME_PC
	FILE *err = freopen ("in.txt","r",stdin);
	if(!err)
	{
		printf("Error opening file");
		exit(0);
	}

	freopen ("out.txt","w",stdout);
#endif

	scanf("%d", &t);

	while(y < t)
	{
		char c;
		unsigned short xPos=0,oPos=0,bMask=0;
		//Take input
		for(int i=0;i<BOARD_SIZE;i++)
		{
			//scanf("%c", &c);
			cin>>c;
			//printf("%d i, %c c\n",i,c);
			switch (c)
			{
				case 'X' :
				xPos |=(0x01<<i);
				//printf("shofting by %d\n", i);
				//printf("%d\n",xPos);
				break;
				case 'O' :
				oPos |=(0x01<<i);
				break;
				case 'T' :
				bMask |=(0x01<<i);
			}
		}

		//printf("xPos %x, oPos %x, bMask %x\n",xPos,oPos,bMask);

		bool win=false;

		for(int i=0;i<sizeof(winPos)/sizeof(unsigned short);i++)
		{
			if((winPos[i] & (xPos | bMask)) == winPos[i])
			{
				printf("Case #%d: X won\n",y+1);
				win = true;
				break;
			}
			
			if((winPos[i] & (oPos | bMask)) == winPos[i])
			{
				printf("Case #%d: O won\n",y+1);
				win = true;
				break;
			}

		}

		if(!win)
		{
			if((xPos | oPos | bMask) == 0xFFFF )
			{
				//No win and all squares occupied ! its a draw
				printf("Case #%d: Draw\n", y+1);

			}
			else
				printf("Case #%d: Game has not completed\n",y+1);
		}

		y++;
	}

	return 0;
}
