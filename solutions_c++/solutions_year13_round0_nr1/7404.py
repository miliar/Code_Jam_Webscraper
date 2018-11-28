#include <cstdio>
#include <memory>
#include <conio.h>

void main()
{
	char cdata[5][5];
	int data[4][4];
	FILE *r,*w;
	int n;
	int result[10];

	fopen_s(&r,"input.txt","r");
	fopen_s(&w,"output.txt","w");

	memset(data,0,sizeof(data));

	fscanf_s(r,"%d\n",&n);

	for(int k = 0; k < n ; k++)
	{
		int i,j;
		char c;
		int X = 0, O = 0;
		int check = 1; //게임 끝낫는지여부
		//input
		for( i = 0; i < 4 ; i++)
		{
			fscanf(r,"%s",cdata[i]);

			for( j=0; j<4;j++)
			{
				if(cdata[i][j] == 'X') data[i][j] = 1;
				else if(cdata[i][j] =='O') data[i][j] = 100;
				else if(cdata[i][j] =='T') data[i][j] = 5;
				else { data[i][j] = 0; check = 0; }
			}

		}
		result[0] = data[0][0]+data[0][1]+data[0][2]+data[0][3];
		result[1] = data[1][0]+data[1][1]+data[1][2]+data[1][3];
		result[2] = data[2][0]+data[2][1]+data[2][2]+data[2][3];
		result[3] = data[3][0]+data[3][1]+data[3][2]+data[3][3];

		result[4] = data[0][0]+data[1][0]+data[2][0]+data[3][0];
		result[5] = data[0][1]+data[1][1]+data[2][1]+data[3][1];
		result[6] = data[0][2]+data[1][2]+data[2][2]+data[3][2];
		result[7] = data[0][3]+data[1][3]+data[2][3]+data[3][3];

		result[8] = data[0][0] + data[1][1] + data[2][2] + data[3][3];
		result[9] = data[0][3] + data[1][2] + data[2][1] + data[3][0];

		for( j = 0 ; j < 10; j++)
		{
			if(result[j] == 8 || result[j] ==4){ X =1; break; }
			if(result[j] == 305 || result[j] == 400){ O =1; break; }
		}

		fprintf(w,"Case #%d: ",k+1);

		if( X == 0 && O == 0 && check) fprintf(w,"Draw\n");
		else if( X ==0 && O == 0) fprintf(w,"Game has not completed\n");
		else if( X == 1) fprintf(w,"X won\n");
		else if( O == 1) fprintf(w,"O won\n");
		fscanf(r,"\n");

	}
}