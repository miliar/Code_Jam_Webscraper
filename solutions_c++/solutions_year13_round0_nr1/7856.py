#include <stdio.h>
#include <string.h>

char matriz[6][6];

struct nodo{
	int num;
	char ca;
};

int main()
{
	int casos;
	int caso=1;
	scanf("%d\n",&casos);
	while(casos--)
	{
		nodo arrey[6];
		nodo arrex[6];
		int puntos=0;
		char cad[1000];
		for(int i=0;i<4;i++)
			gets(matriz[i]);
		gets(cad);
	
		for(int i=0;i<4;i++)
		 {
		 	int conx=0,cony=0,conx2=0,cony2=0;
		 	for(int j=0;j<4;j++)
		  	{
		  		if(matriz[i][j]=='.') puntos++;
		  		if(matriz[i][j]=='X'||matriz[i][j]=='T') conx++;
		  		if(matriz[i][j]=='O'||matriz[i][j]=='T') cony++;
		  		if(matriz[j][i]=='X'||matriz[j][i]=='T') conx2++;
		  		if(matriz[j][i]=='O'||matriz[j][i]=='T') cony2++;
		 	}
		 
		 	if(conx>cony) 
		 	{
		 		arrex[i].num=conx;
		 		arrex[i].ca='X';
		 	}
		 	else
		 	{
		 		arrex[i].num=cony;
		 		arrex[i].ca='O';
		 	}
		 	if(conx2>cony2) 
		 	{
		 		arrey[i].num=conx2;
		 		arrey[i].ca='X';
		 	}
		 	else
		 	{
		 		arrey[i].num=cony2;
		 		arrey[i].ca='O';
		 	}
		  }
	
			int x1=0,x2=0,y1=0,y2=0;
			for(int i=0,j=3;i<4;i++,j--)
			{
				if(matriz[i][i]=='X'||matriz[i][i]=='T') x1++;
		  		if(matriz[i][i]=='O'||matriz[i][i]=='T') y1++;
		  		if(matriz[i][j]=='X'||matriz[i][j]=='T') x2++;
		  		if(matriz[i][j]=='O'||matriz[i][j]=='T') y2++;
			}
			
		 	if(x1>y1) 
		 	{
		 		arrex[4].num=x1;
		 		arrex[4].ca='X';
		 	}
		 	else
		 	{
		 		arrex[4].num=y1;
		 		arrex[4].ca='O';
		 	}
		 	if(x2>2) 
		 	{
		 		arrey[4].num=x2;
		 		arrey[4].ca='X';
		 	}
		 	else
		 	{
		 		arrey[4].num=y2;
		 		arrey[4].ca='O';
		 	}	  
		//  for(int i=0;i<5;i++)
		  // printf("%d %c %d %c\n",arrex[i].num,arrex[i].ca,arrey[i].num,arrey[i].ca);
		  int ban1=0,ban2=0;
		  int es1=0,es2=0;
		  for(int i=0;i<5;i++)
		  {
		  	if(arrex[i].num==4) 
		  	{
		  	 ban1=1;
		  	 if(arrex[i].ca=='X')
		  	  es1=1;
		  	}
		  	if(arrey[i].num==4)
		  	{
		  		ban2=1;
		  		if(arrey[i].ca=='X')
		  		es2=1;
		  		
		  	}
		  }

		  
		 if(ban1==1&&ban2==0)
		  {
		  	if(es1==1)
		  	printf("Case #%d: X won\n",caso++);
		  	else
		  	printf("Case #%d: O won\n",caso++);
		  	continue;	
		  	
		  }
		  if(ban1==0&&ban2==1)
		  {
		  	if(es2==1)
		  	printf("Case #%d: X won\n",caso++);
		  	else
		  	printf("Case #%d: O won\n",caso++);
		  	continue;
		  }
		  if((ban1==1&&ban2==1)&&(es1==es2))
		  {
		    	if(es2==1)
		  	printf("Case #%d: X won\n",caso++);
		  	else
		  	printf("Case #%d: O won\n",caso++);
		  	continue;
		  }
		  
		  if((ban1==1&&ban2==1)||puntos==0)
		  {
		   
		   printf("Case #%d: Draw\n",caso++);
		   continue;
		  }
		  if((ban1==0&&ban2==0)&&puntos>0)
		  printf("Case #%d: Game has not completed\n",caso++);
		 
		
	}
	
	
	return 0;
}
