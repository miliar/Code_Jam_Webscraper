#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <list>
#include <sstream>
#include <string>
#include <cstring>

#include <memory.h>
#include <algorithm>
#include <cmath>

using namespace std;

#define N 4
int Direccion_i[8] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int Direccion_j[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
#define Hay_T M[pos][i] ==  'T'
#define Origen_es_ElemF M[pos][i] == M[pos][pos]
#define Origen_es_ElemC M[i][pos] == M[pos][pos]
bool EsGanador( char M[N][N], int pos )
{
    int i=0; int cont; char aux;
    //REVISAR FILA
    cont = 0;   aux = M[pos][i];
    for (i=0; i < N; i++)
    {

        if ( Origen_es_ElemF || M[pos][i] ==  'T'  ) cont ++ ;
        if ( cont == 4 ) return true;
    }
    //REVISAR COLUMNA EN CASO DE QUE NO HAYA GANADOR EN FILA
    cont = 0;    aux = M[i][pos];
    for (i=0; i< N; i++)
    {

        if ( Origen_es_ElemC || M[i][pos] ==  'T' ) cont++;
        if ( cont == 4 ) return true;
    }
    //REVISAR DIAGONAL PRINCIPAL... PUEDE QUE HAYA GANADO AQUI...
    cont=0; aux = M[i][i];
    if (pos==0)
    {
        for (i=0; i < N; i++)
        {

            if ( M[i][i] == M[pos][pos] || M[i][i] ==  'T' ) cont++ ;
            if ( cont == 4 ) return true;
        }
    }
    return false;
}
bool Existen_Puntos( char M[N][N] )
{
    int i=0,j=0;
    for(i=0; i < N; i ++)
    {
        for( j=0; j< N ; j++)
        {
            if ( M[i][j] == '.') return true;
        }
    }
    return false;
}
int main()
{
    #ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
    #endif
    int casos; int i=0,j=0; int cont;
	scanf("%d", &casos); getchar();
	int cont_casos=1;
	while  ( casos -- )
	{
		char M[N][N];
        //LECTURA
		for(i=0; i < N; i ++)
		{
			for( j=0; j< N ; j++)
			{
                scanf( "%c", &M[i][j]);
			}getchar();
		}if(casos)getchar();
		//BUSQUEDA EN FILAS, COLUMNAS Y DP
		char ganador=' ';
		for(i=0; i < N; i ++)
		{
			if( M[i][i]!= '.' && EsGanador( M, i) )
			{
				ganador = M[i][i];
			}
		}
		if ( ganador == ' ' )
        {
            //REVISAR DIAGONAL SEC, Puede que haya un ganador aqui...
            cont=0; char aux = M[0][N-1]; int h = 0;
            for (i=N - 1 ; i >= 0 ; i-- )
            {
                if( M[h][i] != '.' )
                {
                    if ( M[h][i] == M[0][N-1] || M[h][i] ==  'T' ) cont++ ;
                    if ( cont == 4 ) ganador = M[0][N-1];
                }
                h++;
            }
        }
        printf("Case #%d: ", cont_casos++);
        if ( ganador != ' ' ) printf ( "%c won\n", ganador);
            else if( Existen_Puntos( M ) )
                    printf("Game is not over yet\n");
                else printf("Draw\n");

	}
	fclose(stdout);
    //getchar();
	return 0;
}
