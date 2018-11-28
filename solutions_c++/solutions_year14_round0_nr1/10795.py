#include <cstdio>
#include <iostream>
using namespace std;
int main()
{
	int T; scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		int i,j,aux,fila1,fila2,resultado=0,imp;
		int mat1[4][4];
		int mat2[4][4];
		scanf("%d",&fila1);
		for(i=0;i<4;i++){for(j=0;j<4;j++){scanf("%d",&aux);mat1[i][j]=aux;}}
		scanf("%d",&fila2);
		for(i=0;i<4;i++){for(j=0;j<4;j++){scanf("%d",&aux);mat2[i][j]=aux;}}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(mat1[fila1-1][i]==mat2[fila2-1][j])
				{
					//printf("el numero igual es: %d\n",mat1[fila1-1][i]);
					imp=mat1[fila1-1][i];resultado++;
				}
			}
		}
		//cout<<"--------------------------\n";
		if(resultado==0){printf("Case #%d: Volunteer Cheated!\n",t+1);}
		else if(resultado==1){printf("Case #%d: %d\n",t+1,imp);}
		else{printf("Case #%d: Bad magician!\n",t+1);}
	}
	return 42;
}
