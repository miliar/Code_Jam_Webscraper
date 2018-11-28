#include <stdio.h>

void output(int casenum, int result)
{
	printf("Case #%d: ",casenum +1);
	switch(result)
	{
		case 0:
			printf("Draw");
			break;
		case 1:
			printf("X won");
			break;
		case 2:
			printf("O won");
			break;
		case 3:
			printf("Game has not completed");
			break;
		default:
			printf("Not support");
			break;

	}
	printf("\n");
}

int main()
{
	unsigned int num =0;
	if(!scanf("%d", &num)) return -1;
	for(int i =0; i < num; ++i)
	{

		int  board[5][5] = {
			{0,0,0,0,0},
			{0,0,0,0,0},
			{0,0,0,0,0},
			{0,0,0,0,0},
			{0,0,0,0,0}
		};

		char chess =0;
		scanf("%c",&chess);

		for(int j=0; j < 4; ++j )
			for(int k=0; k < 5; ++k)
			{
				if(scanf("%c",&chess))
				{
					int encode = 0;
					switch((int)chess)
					{
						case (int)'X':
							board[j][k] = 1;
							break;
						case (int)'O':
							board[j][k] = 2;
							break;
						case (int)'T':
							board[j][k] = 5;
							break;
						case (int)'.':
							board[j][k] = 0;
							break;
						default:
							//board[j][k] = -1;
							break;
					}		
				}
			}

		int row =0;
		int column = 0;
		for(int j=0; j < 4; ++j )
		{
			row =0;
			bool rowhast = false;
			bool rowhasempty = false;
			for(int k=0; k < 4; ++k)
			{
				int cellvalue = board[j][k];
				if(cellvalue == 1 || cellvalue ==2)
				{
					row += cellvalue;
				}
				else if(cellvalue == 5 )
				{
					rowhast = true;
				}
				else
				{
					rowhasempty = true;
				}
			}

			if(rowhasempty)
			{
				board[j][4] = 3;
			}
			else if(rowhast)
			{
				if(row %3 == 0 && row/3 ==1)
				{
					board[j][4] = 1;
				}
				else if(row % 6 == 0 && row/6 ==1)
				{
					board[j][4] = 2;
				}
				else 
				{	
					board[j][4] = 0; // draw
				}
			}
			else
			{

				if(row %4 == 0 && row/4 ==1)
				{
					board[j][4] = 1;
				}
				else if(row %8 == 0 && row /8 == 1)
				{
					board[j][4] = 2;
				}
				else 
				{	
					board[j][4] = 0; // draw
				}
			}
		}

		for(int k=0; k < 4; ++k )
		{
			row =0;
			bool rowhast = false;
			bool rowhasempty = false;
			for(int j=0; j < 4; ++j)
			{
				int cellvalue = board[j][k];
				if(cellvalue == 1 || cellvalue ==2)
				{
					row += cellvalue;
				}
				else if(cellvalue == 5 )
				{
					rowhast = true;
				}
				else
				{
					rowhasempty = true;
				}
			}

			if(rowhasempty)
			{
				board[4][k] = 3;
			}
			else if(rowhast)
			{
				if(row % 3 == 0 && row/3 ==1)
				{
					board[4][k] = 1;
				}
				else if(row % 6 == 0 && row /6 ==1)
				{
					board[4][k] = 2;
				}
				else 
				{	
					board[4][k] = 0; // draw
				}
			}
			else
			{

				if(row % 4 == 0 && row /4 ==1)
				{
					board[4][k] = 1;
				}
				else if(row %8 == 0 && row /8 == 1)
				{
					board[4][k] = 2;
				}
				else 
				{	
					board[4][k] = 0; // draw
				}
			}
		}

		int csum =0;
		bool cnotcomplete = false;
		bool xwin = false;
		bool owin = false;
		for(int k=0; k <4; ++k)
		{
			int cellvalue = board[4][k];
			csum += cellvalue;
			if(cellvalue == 3)
				cnotcomplete = true;
			if(cellvalue == 1)
				xwin = true;
			if(cellvalue  == 2)
				owin = true;
		}

		if(xwin)
		{
			output(i,1);
			continue;
		}
		if(owin)
		{
			output(i,2);
			continue;
		}		

		int rsum =0;
		bool rnotcomplete = false;
		xwin =false;
		owin = false;

		for(int j=0; j<4; ++j)
		{
			int cellvalue = board[j][4];
			csum += cellvalue;
			if(cellvalue == 3)
				rnotcomplete = true;
			if(cellvalue == 1)
				xwin = true;
			if(cellvalue  == 2)
				owin = true;
		}


		if(xwin)
		{
			output(i,1);
			continue;
		}
		if(owin)
		{
			output(i,2);
			continue;
		}

		/*	
			printf("case %d\n",i);
			for(int j=0; j < 5; ++j )
			{
			for(int k=0; k < 5; ++k)
			{
			printf("%d,",board[j][k]);
			}
			printf("\n");
			}
		 */

		// diagnose
		int sumdia1 = 0;
		bool dia1hast= false;
		bool dia1draw = false;
		bool dia1hasempty = false;
		xwin = false;
		owin = false;
		for(int l=0; l<4; ++l)
		{
			int cellvalue = board[l][l];
			if(cellvalue ==1 || cellvalue ==2)
			{
				sumdia1 += cellvalue;
			}
			else if(cellvalue ==5)
			{	
				dia1hast = true;
			}
			else if(cellvalue == 0)
			{
				dia1hasempty = true;
			}
		}
		if(dia1hast)
		{

			if(sumdia1 % 3 == 0 && sumdia1/3 ==1)
			{
				xwin =true;
			}
			else if(sumdia1 % 6 == 0 && sumdia1 /6 ==1)
			{
				owin = true;
			}
			else 
			{
				dia1draw = true;	
			}
		}
		else
		{

			if(sumdia1 % 4 == 0 && sumdia1 /4 ==1)
			{
				xwin = true;
			}
			else if(sumdia1 %8 == 0 && sumdia1 /8 ==1)
			{
				owin = true;
			}
			else 
			{
				dia1draw = true;	
			}
		}

		if(!dia1hasempty)
		{
			if(xwin)
			{
				output(i,1);
				continue;
			}
			if(owin)
			{
				output(i,2);
				continue;
			}
		}

		// diagnose
		int sumdia2 = 0;
		bool dia2hast= false;
		bool dia2draw = false;
		bool dia2hasempty = false;
		xwin = false;
		owin = false;
		for(int l=0; l < 4; ++l)
		{
			for(int m=0; m < 4; ++m)
			{
				if(l+m == 3)
				{
					int cellvalue = board[l][m];
					if(cellvalue ==1 || cellvalue ==2)
					{
						sumdia2 += cellvalue;
					}
					else if(cellvalue ==5)
					{	
						dia2hast = true;
					}
					else if(cellvalue == 0)
						dia2hasempty = true;
				}
			}
		}
		if(dia2hast)
		{

			if(sumdia2 % 3 == 0 && sumdia2/3 ==1)
			{
				xwin =true;
			}
			else if(sumdia2 % 6 == 0 && sumdia2 /6 ==1)
			{
				owin = true;
			}
			else 
			{
				dia2draw = true;	
			}
		}
		else
		{

			if(sumdia2 % 4 == 0 && sumdia2 /4 ==1)
			{
				xwin = true;
			}
			else if(sumdia2 %8 == 0 && sumdia2 /8 ==1)
			{
				owin = true;
			}
			else 
			{
				dia2draw = true;	
			}
		}

		if(!dia2hasempty)
		{
			if(xwin)
			{

				output(i,1);
				continue;
			}
			if(owin)
			{
				output(i,2);
				continue;
			}
		}
		if(rsum ==0 && csum==0 && dia1draw && dia2draw)
		{
			output(i,0);
			continue;
		}				
		if(cnotcomplete || rnotcomplete)
		{
			output(i,3);
			continue;
		}		
	}
	return 0;
}
