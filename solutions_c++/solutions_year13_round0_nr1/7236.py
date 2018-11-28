#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
	if(argc == 2)
	{
		FILE *in = fopen(argv[1],"r");
		FILE *out = fopen("A.out","w");
		if(in != 0)
		{
			int z = 0;
                        char line[5][6];
			fgets(line[0], 10, in);
			int n = atoi(line[0]);
			for(int i = 1; i <= n; i++)
			{
				for(int j = 0; j < 5; j++)
				{
					fgets(line[j], 6, in);
				}
				
				int status = 3;
				int Xs = 0;
				int Os = 0;
				int Ts = 0;
				if(status == 3)
				{
					for(int j = 0; j < 4; j++)
					{
						if(line[j][j] == 'X')
							Xs++;
						else if(line[j][j] == 'O')
							Os++;
						else if(line[j][j] == 'T')
							Ts++;
					}
					if((Xs == 3 && Ts == 1) || (Xs == 4))
						status = 1;
					if((Os == 3 && Ts == 1) || (Os == 4))
						status = 2;	
				}

				Xs = 0;Os = 0;Ts = 0;
				if(status == 3)
				{
					for(int j = 0; j < 4; j++)
					{
						if(line[j][3-j] == 'X')
							Xs++;
						else if(line[j][3-j] == 'O')
							Os++;
						else if(line[j][3-j] == 'T')
							Ts++;
					}
					if((Xs == 3 && Ts == 1) || (Xs == 4))
						status = 1;
					if((Os == 3 && Ts == 1) || (Os == 4))
						status = 2;	
				}
				
				if(status == 3)
				{
					for(int j = 0; j < 4; j++)
					{						
						Xs = 0;Os = 0;Ts = 0;
						for(int k = 0; k < 4; k++)
						{
							if(line[k][j] == 'X')
								Xs++;
							else if(line[k][j] == 'O')
								Os++;
							else if(line[k][j] == 'T')
								Ts++;
						}
						if((Xs == 3 && Ts == 1) || (Xs == 4))
						{
							status = 1;
							break;
						}
						if((Os == 3 && Ts == 1) || (Os == 4))
						{
							status = 2;	
							break;
						}
					}
				}
				
				if(status == 3)
				{
					for(int j = 0; j < 4; j++)
					{						
						Xs = 0;Os = 0;Ts = 0;
						for(int k = 0; k < 4; k++)
						{
							if(line[j][k] == 'X')
								Xs++;
							else if(line[j][k] == 'O')
								Os++;
							else if(line[j][k] == 'T')
								Ts++;
						}
						if((Xs == 3 && Ts == 1) || (Xs == 4))
						{
							status = 1;
							break;
						}
						if((Os == 3 && Ts == 1) || (Os == 4))
						{
							status = 2;	
							break;
						}
					}
				}
				if(status == 3)
				{	
					int flag = 0;
					for(int j = 0; j < 4; j++)
					{
						for(int k = 0; k < 4; k++)
						{
							if(line[k][j] == '.')
							{
								status = 4;
								break;
							}
						}
						if(status != 3)
							break;
					}
				}
				fputs("Case #", out);
				char num[4];
				itoa(i, num, 10);
				fputs(num, out);
				fputs(": ", out);
				switch(status)
				{
					case 1:
						fputs("X won\n", out);
						break;
					case 2:
						fputs("O won\n", out);
						break;
					case 3:
						fputs("Draw\n", out);
						break;
					case 4:
						fputs("Game has not completed\n",out);
						break;
				}
			}
			fclose(out);
			fclose(in);
		}
	}
	return 1;
}
