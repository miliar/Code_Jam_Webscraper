#include<stdio.h>
#include<conio.h>
int check(char ip[4][4])
{
	int diag[2]={-2,-2},hor[4]={-2,-2,-2,-2},vert=-2,result = 0,i,j;
	int cont = 0;
	for (i=0;i<4;i++)
	{
	
	vert = -2;
		for(j=0;j<4;j++)
		{
			char x= ip [i][j];
			int val=0;
			if (x == '.')
			{
				cont =3;
				vert = -1;
				hor[j] = -1;
				if (i == j)
				diag[0] = -1;
				else if ((i + j) == 3 )
				diag[1] = -1;
			}
			else
			{
			if (x == 'X')
			val = 1;
			else if (x == 'O')
			val = 2 ;  
			else if (x == 'T')
			val = 3;
				if (vert == -2)
				{ 
					vert = val;
				}
				else if (vert != -1)
				{
					vert = vert & val ;
				}
				if (hor[j] == -2)
				{ 
					hor[j] = val;
				}
				else if (hor[j] != -1)
				{
					hor[j] = hor[j] & val ;
				}
				if (i == j)
				{
					if (diag[0] == -2)
					{ 
						diag[0] = val;
					}
					else if (diag[0] != -1)
					{
						diag[0] = diag[0] & val ;
					}
				}
				else if ((i + j) == 3 )
				{
					if (diag[1] == -2)
					{ 
						diag[1] = val;
					}
					else if (diag[1] != -1)
					{
						diag[1] = diag[1] & val ;
					}
				}											
			}			
			
		}
	if (vert == 1 || vert == 2)
	return vert;
	}

	for (i=0;i<2;i++)
     {
     	if((diag[i] == 1)|| (diag[i] == 2))
     	return diag[i];
     }
     for (i=0;i<4;i++)
     {
     	if((hor[i] == 1)|| (hor[i] == 2))
     	return hor[i];
     }
	 /*result = (((hor[0]==-1)?0:hor[0]-1)|((hor[1]==-1)?0:hor[1]-1) | ((hor[2]==-1)?0:hor[2]-1) | ((hor[3]==-1)?0:hor[3]-1) | ((vert==-1)?0:vert-1) |((diag[0]==-1)?0:diag[0]-1) | ((diag[1]==-1)?0:diag[1]-1));
     if (result == 0)
      return 1;
      if (result == 1)
      return 2;*/
      
      return cont;
}
main(){
	int n,i,j,z;
	int m;
	char ip[4][4];
	scanf("%d",&n);
	scanf("%c",&m);
	{
	int arr[n];
	for (i=0;i<n;i++)
	{
		for (j=0;j<4;j++)
		{
			for (z=0;z<4;z++)
			{
				scanf("%c",&ip[j][z]);
			}
			scanf("%c",&m);
		}
		scanf("%c",&m);
		arr[i]=check(ip);
	}
	for (i=0;i<n;i++)
	{
		printf("Case #%d: ",i+1);
		if (arr[i] == 0)
		{
			printf("Draw\n");
		}
		else if (arr[i] == 3)
		{
			printf("Game has not completed\n");
		}
		else if (arr[i] == 1)
		{
			printf("X won\n");
		}
		else if (arr[i] == 2)
		{
			printf("O won\n");
		}
		
	}
	}
	getch();
	getch();
}
