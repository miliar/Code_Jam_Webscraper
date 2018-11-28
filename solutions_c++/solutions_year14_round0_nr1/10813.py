#include <stdio.h>

int n;
int arr[4][4], brr[4][4];
int resp[100], num[100];

void funcion(int x, int y, int pos)
{
    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            if(arr[x][i]==brr[y][j])
            {
                resp[pos]++;
                num[pos]=brr[y][j];
            }
        }
    }
}

int main()
{
	FILE* archivo_entrada=NULL;
	FILE *fout = fopen ("salida.txt", "w");
	archivo_entrada = fopen("A-small-attempt2.in","r");
	if(archivo_entrada==NULL)
		return -1;
	
    fscanf(archivo_entrada,"%d",&n);
    for(int i=0; i<n; i++)
    {
    	int row, row2;
        fscanf(archivo_entrada,"%d",&row);
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                fscanf(archivo_entrada,"%d",&arr[j][k]);
        fscanf(archivo_entrada,"%d",&row2);
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                fscanf(archivo_entrada,"%d",&brr[j][k]);
        funcion(row-1,row2-1,i);
    }

    for(int i=0; i<n; i++)
    {
    	int a = i+1;
        if(resp[i]==0)
        {
            fprintf(fout,"Case #%d",a);
            fprintf(fout,": Volunteer cheated!\n");
        }
        else if(resp[i]==1)
        {
            fprintf(fout,"Case #%d",a);
            fprintf(fout,": %d\n",num[i]);
        }
        else
        {
            fprintf(fout,"Case #%d",a);
            fprintf(fout,": Bad magician!\n");
        }
    }

    return 0;
}
