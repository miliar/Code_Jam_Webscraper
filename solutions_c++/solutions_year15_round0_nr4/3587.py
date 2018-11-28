#include<stdio.h>

int main()
{   int t,x,r,c,i,num;
	char mat[5][5][5];
	FILE *ip,*op;
	ip=fopen("input.txt","r");
	op=fopen("output.txt","w");
	
	mat[1][1][1]='G';
	mat[1][1][2]='R';
	mat[1][1][3]='R';
	mat[1][1][4]='R';
	
	mat[1][2][1]='G';
	mat[1][2][2]='G';
	mat[1][2][3]='R';
	mat[1][2][4]='R';
	
    mat[2][1][1]='G';
	mat[2][1][2]='G';
	mat[2][1][3]='R';
	mat[2][1][4]='R';
	
	mat[1][3][1]='G';
	mat[1][3][2]='R';
	mat[1][3][3]='R';
	mat[1][3][4]='R';

    mat[3][1][1]='G';
	mat[3][1][2]='R';
	mat[3][1][3]='R';
	mat[3][1][4]='R';

    mat[1][4][1]='G';
	mat[1][4][2]='G';
	mat[1][4][3]='R';
	mat[1][4][4]='R';
	
	mat[4][1][1]='G';
	mat[4][1][2]='G';
	mat[4][1][3]='R';
	mat[4][1][4]='R';

    mat[2][2][1]='G';
	mat[2][2][2]='G';
	mat[2][2][3]='R';
	mat[2][2][4]='R';

    mat[2][3][1]='G';
	mat[2][3][2]='G';
	mat[2][3][3]='G';
	mat[2][3][4]='R';
	
	mat[3][2][1]='G';
	mat[3][2][2]='G';
	mat[3][2][3]='G';
	mat[3][2][4]='R';

    mat[2][4][1]='G';
	mat[2][4][2]='G';
	mat[2][4][3]='R';
	mat[2][4][4]='R';

    mat[4][2][1]='G';
	mat[4][2][2]='G';
	mat[4][2][3]='R';
	mat[4][2][4]='R';
	
	mat[3][3][1]='G';
	mat[3][3][2]='R';
	mat[3][3][3]='G';
	mat[3][3][4]='R';

    mat[3][4][1]='G';
	mat[3][4][2]='G';
	mat[3][4][3]='G';
	mat[3][4][4]='G';
	
	mat[4][3][1]='G';
	mat[4][3][2]='G';
	mat[4][3][3]='G';
	mat[4][3][4]='G';

    mat[4][4][1]='G';
	mat[4][4][2]='G';
	mat[4][4][3]='R';
	mat[4][4][4]='G';

	fscanf(ip,"%d\n",&t);
	for(num=1;num<=t;num++)
	{  fscanf(ip,"%d %d %d\n",&x,&r,&c);
	   fprintf(op,"Case #%d: ",num);
	   if(mat[r][c][x]=='G')
	   {fprintf(op,"GABRIEL\n");
	   }
	   else
	   {fprintf(op,"RICHARD\n");
	   }

	}
	fclose(ip);
	fclose(op);
	return 0;
}
