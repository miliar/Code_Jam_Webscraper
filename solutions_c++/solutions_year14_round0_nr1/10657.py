#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int T;
int f;
int s;
int mat1[4][4];
int mat2[4][4];
int compt = 0;
bool res;
int last;
int main()
{
	FILE * fin = fopen("A-small-attempt2.in","rw+");
	FILE * fout = fopen("A-small-attempt2.out","w+");
	 fscanf(fin,"%d",&T);
	 for(int i = 1 ; i <= T ; ++i)
	{
		compt = 0;
		fscanf(fin,"%d",&f);
	 	for(int j = 0 ; j < 4 ; ++j)
		{
			fscanf(fin,"%d %d %d %d",&mat1[j][0],&mat1[j][1],&mat1[j][2],&mat1[j][3]);
		}
		fscanf(fin,"%d",&s);
	 	for(int j = 0 ; j < 4 ; ++j)
		{
			fscanf(fin,"%d %d %d %d",&mat2[j][0],&mat2[j][1],&mat2[j][2],&mat2[j][3]);
		}
		--f;
		--s;
		for(int j = 0 ; j < 4 ; ++j)
		{
			if(mat1[f][j] == mat2[s][0])
			{
				last = mat2[s][0];
				compt++;
			}
			if(mat1[f][j] == mat2[s][1])
			{
				last = mat2[s][1];
				compt++;
			}
			if(mat1[f][j] == mat2[s][2])
			{
				last = mat2[s][2];
				compt++;
			}
			if(mat1[f][j] == mat2[s][3])
			{
				last = mat2[s][3];
				compt++;
			}
		}
		switch(compt)
		{
			case 0:
				fprintf(fout,"Case #%d: Volunteer cheated!\n",i);
				break;
			case 1:
				fprintf(fout,"Case #%d: %d\n",i,last);
				break;
			default:
				fprintf(fout,"Case #%d: Bad magician!\n",i);
				break;
		}
	}
	fclose(fin);
	fclose(fout);
return 0;

}

