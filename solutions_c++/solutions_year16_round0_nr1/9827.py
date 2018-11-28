//
//  main.cpp
//  Codejam-Couting sheep
//
//  Created by Lucas Prieels on 9/04/16.
//  Copyright © 2016 Lucas Prieels. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int tableau[10];


int longueur(int nbr)
{
    int nombre=0;
    do {
        ++nombre;
        nbr /= 10;
    } while (nbr>0);
    return nombre;
}

void compter(int x, int tableau[])
{
    int tab[6];
    if (longueur(x)==6)
    {
        tab[0]= x/100000  %10;
        tab[1]= x/10000   %10;
        tab[2]= x/1000    %10;
        tab[3]= x/100     %10;
        tab[4]= x/10      %10;
        tab[5]= x         %10;
    }
    if (longueur(x)==5)
    {
        tab[0]= x/10000   %10;
        tab[1]= x/1000    %10;
        tab[2]= x/100     %10;
        tab[3]= x/10      %10;
        tab[4]= x         %10;
    }
    if (longueur(x)==4)
    {
        tab[0]= x/1000    %10;
        tab[1]= x/100     %10;
        tab[2]= x/10      %10;
        tab[3]= x         %10;
    }
    if (longueur(x)==3)
    {
        tab[0]= x/100     %10;
        tab[1]= x/10      %10;
        tab[2]= x         %10;
    }
    if (longueur(x)==2)
    {
        tab[0]= x/10      %10;
        tab[1]= x         %10;
    }
    if (longueur(x)==1)
    {
        tab[0]= x         %10;
    }
    for (int i=0; i<longueur(x); i++)
    {
        ++tableau[tab[i]];
    }
}
int main()
{
    ifstream fin ("/Users/Lucas/Downloads/codejam_couting_sheep.in");
    ofstream fout ("/Users/Lucas/Downloads/codejam_couting_sheep.out");
    int nbrfois;
    fin >> nbrfois;
    for (int i=1; i<=nbrfois; i++)
    {
        for (int i=0; i<10; i++)
        {
            tableau[i]=0;
        }        int nbr;
        fin >> nbr;
        int nombre=nbr;
        if (nbr==0)
        {
            fout << "case #" << i << ": INSOMNIA" << endl;
        }
        else
        {
            do {
                compter(nbr, tableau);
                nbr+=nombre;
            } while (not(tableau[0]>0 and tableau[1]>0 and tableau[2]>0 and tableau[3]>0 and tableau[4]>0 and tableau[5]>0 and tableau[6]>0 and tableau[7]>0 and tableau[8]>0 and tableau[9]>0));
            fout << "case #" << i << ": " << nbr-nombre << endl;
        }
    }
    return 0;
}
