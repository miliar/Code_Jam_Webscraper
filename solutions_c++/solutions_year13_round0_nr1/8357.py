#include <cstdio>
#include <cstdlib>
#include <stack>
#include <queue>
#include <list>
#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <deque>
#include <functional>
#define inf 0x3f3f3f3f


using namespace std;

int main()
{
	int casos;scanf("%d",&casos);
	for(int c=1;c<=casos;c++)
	{
		char matriz[4][4];
		for(int t=0;t<4;t++)
		{
			for(int l=0;l<4;l++)
			{
				cin>>matriz[t][l];
			}
		}
		/*char lol;cin>>lol;*/
		/*for(int t=0;t<4;t++)
		{
			for(int l=0;l<4;l++)
			{
				printf("%c",matriz[t][l]);
			}
			printf("\n");
		}*/
		bool incompleto=false;
		//	Caso diagonal principal
		if(matriz[0][0]==matriz[1][1] && matriz[1][1]==matriz[2][2] && matriz[2][2]==matriz[3][3] && matriz[0][0]!='.'){printf("Case #%d: %c won\n",c,matriz[0][0]);}
		else if(matriz[0][0]=='T' && matriz[2][2]!='.' && matriz[1][1]==matriz[2][2] && matriz[2][2]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[1][1]);}
		else if(matriz[1][1]=='T' && matriz[2][2]!='.' && matriz[0][0]==matriz[2][2] && matriz[2][2]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
		else if(matriz[2][2]=='T' && matriz[1][1]!='.' && matriz[0][0]==matriz[1][1] && matriz[1][1]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
		else if(matriz[3][3]=='T' && matriz[1][1]!='.' && matriz[0][0]==matriz[1][1] && matriz[1][1]==matriz[2][2]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
		else
		{
			//	Caso diagonal secundaria
			if(matriz[0][3]==matriz[1][2] && matriz[1][2]==matriz[2][1] && matriz[2][1]==matriz[3][0] && matriz[0][3]!='.'){printf("Case #%d: %c won\n",c,matriz[0][3]);}
			else if(matriz[0][3]=='T' && matriz[2][1]!='.' && matriz[1][2]==matriz[2][1] && matriz[2][1]==matriz[3][0]){printf("Case #%d: %c won\n",c,matriz[1][2]);}
			else if(matriz[1][2]=='T' && matriz[2][1]!='.' && matriz[0][3]==matriz[2][1] && matriz[2][1]==matriz[3][0]){printf("Case #%d: %c won\n",c,matriz[0][3]);}
			else if(matriz[2][1]=='T' && matriz[1][2]!='.' && matriz[0][3]==matriz[1][2] && matriz[1][2]==matriz[3][0]){printf("Case #%d: %c won\n",c,matriz[0][3]);}
			else if(matriz[3][0]=='T' && matriz[1][2]!='.' && matriz[0][3]==matriz[1][2] && matriz[1][2]==matriz[2][1]){printf("Case #%d: %c won\n",c,matriz[0][3]);}
			else
			{
				// Casos columna 1
				if(matriz[0][0]==matriz[1][0] && matriz[1][0]==matriz[2][0] && matriz[2][0]==matriz[3][0] && matriz[0][0]!='.'){printf("Case #%d: %c won\n",c,matriz[0][0]);}
				else if(matriz[0][0]=='T' && matriz[0][2]!='.' && matriz[0][1]==matriz[0][2] && matriz[0][2]==matriz[0][3]){printf("Case #%d: %c won\n",c,matriz[0][1]);}
				else if(matriz[0][1]=='T' && matriz[0][2]!='.' && matriz[0][0]==matriz[0][2] && matriz[0][2]==matriz[0][3]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
				else if(matriz[0][2]=='T' && matriz[0][1]!='.' && matriz[0][0]==matriz[0][1] && matriz[0][1]==matriz[0][3]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
				else if(matriz[0][3]=='T' && matriz[0][1]!='.' && matriz[0][0]==matriz[0][1] && matriz[0][1]==matriz[0][2]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
				else
				{
					// Casos columna 2
					if(matriz[0][1]==matriz[1][1] && matriz[1][1]==matriz[2][1] && matriz[2][1]==matriz[3][1] && matriz[0][1]!='.'){printf("Case #%d: %c won\n",c,matriz[0][1]);}
					else if(matriz[0][1]=='T' && matriz[2][1]!='.' && matriz[1][1]==matriz[2][1] && matriz[2][1]==matriz[3][1]){printf("Case #%d: %c won\n",c,matriz[1][1]);}
					else if(matriz[1][1]=='T' && matriz[2][1]!='.' && matriz[0][1]==matriz[2][1] && matriz[2][1]==matriz[3][1]){printf("Case #%d: %c won\n",c,matriz[0][1]);}
					else if(matriz[2][1]=='T' && matriz[1][1]!='.' && matriz[0][1]==matriz[1][1] && matriz[1][1]==matriz[3][1]){printf("Case #%d: %c won\n",c,matriz[0][1]);}
					else if(matriz[3][1]=='T' && matriz[1][1]!='.' && matriz[0][1]==matriz[1][1] && matriz[1][1]==matriz[2][1]){printf("Case #%d: %c won\n",c,matriz[0][1]);}
					else
					{
						// Casos columna 3
						if(matriz[0][2]==matriz[1][2] && matriz[1][2]==matriz[2][2] && matriz[2][2]==matriz[3][2] && matriz[0][2]!='.'){printf("Case #%d: %c won\n",c,matriz[0][2]);}
						else if(matriz[0][2]=='T' && matriz[2][2]!='.' && matriz[1][2]==matriz[2][2] && matriz[2][2]==matriz[3][2]){printf("Case #%d: %c won\n",c,matriz[1][2]);}
						else if(matriz[1][2]=='T' && matriz[2][2]!='.' && matriz[0][2]==matriz[2][2] && matriz[2][2]==matriz[3][2]){printf("Case #%d: %c won\n",c,matriz[0][2]);}
						else if(matriz[2][2]=='T' && matriz[1][2]!='.' && matriz[0][2]==matriz[1][2] && matriz[1][2]==matriz[3][2]){printf("Case #%d: %c won\n",c,matriz[0][2]);}
						else if(matriz[3][2]=='T' && matriz[1][2]!='.' && matriz[0][2]==matriz[1][2] && matriz[1][2]==matriz[2][2]){printf("Case #%d: %c won\n",c,matriz[0][2]);}
						else
						{
		
							// Casos columna 4
							if(matriz[0][3]==matriz[1][3] && matriz[1][3]==matriz[2][3] && matriz[2][3]==matriz[3][3] && matriz[0][3]!='.' ){printf("Case #%d: %c won\n",c,matriz[0][3]);}
							else if(matriz[0][3]=='T' && matriz[2][3]!='.' && matriz[1][3]==matriz[2][3] && matriz[2][3]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[1][3]);}
							else if(matriz[1][3]=='T' && matriz[2][3]!='.' && matriz[0][3]==matriz[2][3] && matriz[2][3]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[0][3]);}
							else if(matriz[2][3]=='T' && matriz[1][3]!='.' && matriz[0][3]==matriz[1][3] && matriz[1][3]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[0][3]);}
							else if(matriz[3][3]=='T' && matriz[1][3]!='.' && matriz[0][3]==matriz[1][3] && matriz[1][3]==matriz[2][3]){printf("Case #%d: %c won\n",c,matriz[0][3]);}
							else
							{
								// Casos fila 1
								if(matriz[0][0]==matriz[0][1] && matriz[0][1]==matriz[0][2] && matriz[0][2]==matriz[0][3] && matriz[0][0]!='.'){printf("Case #%d: %c won\n",c,matriz[0][0]);}
								else if(matriz[0][0]=='T' && matriz[0][2]!='.' && matriz[0][1]==matriz[0][2] && matriz[0][2]==matriz[0][3]){printf("Case #%d: %c won\n",c,matriz[0][1]);}
								else if(matriz[0][1]=='T' && matriz[0][2]!='.' && matriz[0][0]==matriz[0][2] && matriz[0][2]==matriz[0][3]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
								else if(matriz[0][2]=='T' && matriz[0][1]!='.' && matriz[0][0]==matriz[0][1] && matriz[0][1]==matriz[0][3]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
								else if(matriz[0][3]=='T' && matriz[0][1]!='.' && matriz[0][0]==matriz[0][1] && matriz[0][1]==matriz[0][2]){printf("Case #%d: %c won\n",c,matriz[0][0]);}
								else
								{
									// Casos fila 2
									if(matriz[1][0]==matriz[1][1] && matriz[1][1]==matriz[1][2] && matriz[1][2]==matriz[1][3] && matriz[1][0]!='.'){printf("Case #%d: %c won\n",c,matriz[1][0]);}
									else if(matriz[1][0]=='T' && matriz[1][2]!='.' && matriz[1][1]==matriz[1][2] && matriz[1][2]==matriz[1][3]){printf("Case #%d: %c won\n",c,matriz[1][1]);}
									else if(matriz[1][1]=='T' && matriz[1][2]!='.' && matriz[1][0]==matriz[1][2] && matriz[1][2]==matriz[1][3]){printf("Case #%d: %c won\n",c,matriz[1][0]);}
									else if(matriz[1][2]=='T' && matriz[1][1]!='.' && matriz[1][0]==matriz[1][1] && matriz[1][1]==matriz[1][3]){printf("Case #%d: %c won\n",c,matriz[1][0]);}
									else if(matriz[1][3]=='T' && matriz[1][1]!='.' && matriz[1][0]==matriz[1][1] && matriz[1][1]==matriz[1][2]){printf("Case #%d: %c won\n",c,matriz[1][0]);}
									else
									{
										// Casos fila 3
										if(matriz[2][0]==matriz[2][1] && matriz[2][1]==matriz[2][2] && matriz[2][2]==matriz[2][3] && matriz[2][0]!='.'){printf("Case #%d: %c won\n",c,matriz[2][0]);}
										else if(matriz[2][0]=='T' && matriz[2][2]!='.' && matriz[2][1]==matriz[2][2] && matriz[2][2]==matriz[2][3]){printf("Case %d: #%c won\n",c,matriz[2][1]);}
										else if(matriz[2][1]=='T' && matriz[2][2]!='.' && matriz[2][0]==matriz[2][2] && matriz[2][2]==matriz[2][3]){printf("Case %d: #%c won\n",c,matriz[2][0]);}
										else if(matriz[2][2]=='T' && matriz[2][1]!='.' && matriz[2][0]==matriz[2][1] && matriz[2][1]==matriz[2][3]){printf("Case %d: #%c won\n",c,matriz[2][0]);}
										else if(matriz[2][3]=='T' && matriz[2][1]!='.' && matriz[2][0]==matriz[2][1] && matriz[2][1]==matriz[2][2]){printf("Case %d: #%c won\n",c,matriz[2][0]);}
										else
										{
											
											// Casos fila 4
											if(matriz[3][0]==matriz[3][1] && matriz[3][1]==matriz[3][2] && matriz[3][2]==matriz[3][3] && matriz[3][0]!='.'){printf("Case #%d: %c won\n",c,matriz[3][0]);}
											else if(matriz[3][0]=='T' && matriz[3][2]!='.' && matriz[3][1]==matriz[3][2] && matriz[3][2]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[3][1]);}
											else if(matriz[3][1]=='T' && matriz[3][2]!='.' && matriz[3][0]==matriz[3][2] && matriz[3][2]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[3][0]);}
											else if(matriz[3][2]=='T' && matriz[3][1]!='.' && matriz[3][0]==matriz[3][1] && matriz[3][1]==matriz[3][3]){printf("Case #%d: %c won\n",c,matriz[3][0]);}
											else if(matriz[3][3]=='T' && matriz[3][1]!='.' && matriz[3][0]==matriz[3][1] && matriz[3][1]==matriz[3][2]){printf("Case #%d: %c won\n",c,matriz[3][0]);}
											else
											{
												
												for(int i=0;i<4;i++){for(int j=0;j<4;j++){if(matriz[i][j]=='.'){incompleto=true;break;}}}
												if(incompleto){printf("Case #%d: Game has not completed\n",c);}else{printf("Case #%d: Draw\n",c);}
											}
										}
									}
								}
							}
					}
					}
				}
			}
		}
		
		
		
		
		
		
		
		
		
		
	}
	return 42;
}
