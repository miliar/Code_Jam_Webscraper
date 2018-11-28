#include <stdio.h>

int grilla[102][102];

void clean_grilla()
{
	int i,j;
	for(i = 0; i < 102; i++)
		for(j = 0; j < 102; j++)
			grilla[i][j] = -1;
}

int main ()
{
	FILE * in, *out;
	in = fopen ("B-large.in","r");
	out = fopen ("small.out","w");
	//leer archivo
	int nro_casos;
	int N,M;

	int i,j,k;
	
	int caso_activo = 1;

	fscanf(in, "%d", &nro_casos);

	for(caso_activo = 1 ; caso_activo <= nro_casos ; caso_activo++)
	{
		bool tiene_solucion = true;

		fscanf(in, "%d %d", &N, &M);
		clean_grilla();
		//printf("\n N %d M %d", N, M);

		for(i = 1 ; i <= N ; i++)
			for(j = 1 ; j <= M ; j++)
				fscanf(in, "%d", &grilla[i][j]);

		//todo leído, momento de verificar la condición

		for(i = 1 ; i <= N ; i++)
			for(j = 1 ; j <= M ; j++)
			{
				bool vert_cond = false, hor_cond = false;
				int centro;
				centro = grilla[i][j];
				for(k = 1 ; k <= M ; k++)
				{
					if(k == j) continue;
					if(grilla[i][k] > centro)
						hor_cond = true;
				}
				for(k = 1 ; k <= N ; k++)
				{
					if(k == i) continue;
					if(grilla[k][j] > centro)
						vert_cond = true;
				}
				if(hor_cond && vert_cond)
					tiene_solucion = false;
			
				
			}

		if(tiene_solucion)
		{
			fprintf(out,"Case #%d: YES\n", caso_activo);
		}
		else
			fprintf(out, "Case #%d: NO\n", caso_activo);
	}

	fclose (in);
	fclose (out);
	return 0;
}
