#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <utility>

using namespace std ;

typedef int** t_grille ;
struct s_lawn
{
    t_grille Grille;
    int taille_ligne ;
    int taille_colonne ;
}; typedef s_lawn t_lawn ;

typedef int* table_max ;

int max_col (t_lawn Jardin ,int col)
{
   int max = 0 ;
   int i ;
   for (i=0;i<Jardin.taille_ligne;++i)
   {
    if (Jardin.Grille[i][col]>max)
    {
        max = Jardin.Grille[i][col] ;
    }
   }
   return max ;
}

int max_ligne (t_lawn Jardin ,int ligne)
{
   int max = 0 ;
   int i ;
   for (i=0;i<Jardin.taille_colonne;++i)
   {
    if (Jardin.Grille[ligne][i]>max)
    {
        max = Jardin.Grille[ligne][i] ;
    }
   }
   return max ;
}

int main()
{

ifstream file("B-large.in", ifstream::in);
ofstream file2("out.txt", ofstream::out);

int nb;
file >> nb;
int ligne,col ;
int val  ;

for(int m = 0; m < nb; ++m)
{
    int possible = 0 ;
    file >> ligne ;
    file >> col ;
    //allocation dynamique
    t_lawn Jardin ;
    table_max max_lignes , max_colonnes ;
    Jardin.Grille = (t_grille)malloc(ligne*sizeof(int*));
	int i,j,k ;
	for (i=0; i<ligne; i++)
	{
		Jardin.Grille[i] =(int*) malloc(col*sizeof(int));
	}
    Jardin.taille_colonne = col ;
    Jardin.taille_ligne = ligne;
    max_lignes =(int*) malloc(ligne*sizeof(int));
    max_colonnes =(int*) malloc(col*sizeof(int));
    for(j=0;j < ligne; ++j)
    {
        for (k=0;k<col;++k)
        {
            file >> val;
            Jardin.Grille [j][k] = val ;
        }
    }
    for (j=0;j <ligne;++j)
    {
       max_lignes[j] = max_ligne(Jardin,j) ;
    }
    for (k=0;k <col;++k)
    {
       max_colonnes[k] = max_col(Jardin,k) ;
    }
    for (j=0;j<ligne;++j)
    {
        for(k=0;k<col;++k)
        {
            if (Jardin.Grille[j][k]<max_lignes[j] && Jardin.Grille[j][k]<max_colonnes[k])
            {
                possible = 1 ;
                break;
            }
        }
        if (possible == 1)
        {
            break ;
        }
    }
  if (possible == 1)
  {
      file2 << "Case #" << m+1 << ": NO" << std::endl;
  }
  else
  {
       file2 << "Case #" << m+1 << ": YES" << std::endl;
  }
}
return 0 ;
}

