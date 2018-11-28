#include <iostream>
#include <sstream>
#include <string>
using namespace std;
#include <fstream>
#include<vector>
#include <stdio.h>      /* printf, fgets */
#include <stdlib.h>
#include <algorithm>

std::vector<string> split(string chaine)
{
    int i=0;
    int j=0;
    vector<string> chainesplit;

    while(j != chaine.size())
    {
        if (chaine[j] == ' ')
            {
                if(chaine[i] == ' ')
                    chainesplit.push_back(chaine.substr(i+1,j-i));
                else
                    chainesplit.push_back(chaine.substr(i,j-i));
                i = j;
            }
        j++;

    }
     if(chaine.size() == 1)
        chainesplit.push_back(chaine.substr(0,1));
    if(i+1 != chaine.size()) chainesplit.push_back(chaine.substr(i+1,j-i));
    return chainesplit;
}


int min_time1(vector<string> ligne)
{
    int sortie = 0;

    for(int j=1;j<ligne.size();j++)
    {
        //cerr<< ligne[j]<<endl;
        sortie += max(atoi(ligne[j-1].c_str()) - atoi(ligne[j].c_str()),0);

    }

    return sortie;
}

int min_time2(vector<string> ligne)
{
    int freq = 0;
    for(int j=1;j<ligne.size();j++)
    {
        freq = max(atoi(ligne[j-1].c_str()) - atoi(ligne[j].c_str()),freq);
    }
    freq = freq;
    int mange = 0;
cerr<< "freq 0 "<<freq<<endl;
    for(int j=0;j<ligne.size()-1;j++)
    {
        mange += min(atoi(ligne[j].c_str()),freq);
        cerr<< mange<<endl;
    }

    return mange;
}




int min_tir(int C,int W,int R)
{
    int a = (C/W);
    int reste = C%W;
    if(reste>0) reste = 1;
    return (a+W-1+reste)*R;

}

int main()
{
    vector<int> resultat;
    vector<string> vec;
    freopen("C:/Users/Firas/Documents/codejam2/result.out","w",stdout);
    ifstream fichier("C:/Users/Firas/Documents/codejam2/counter culture/A-small-attempt4.in", ios::in);  // on ouvre le fichier en lecture
    int Ncases = 0;


        if(fichier)  // si l'ouverture a réussi
        {
            string ligne;
            int cpt = 0;
            while(getline(fichier, ligne))  // tant que l'on peut mettre la ligne dans "contenu"
            {
                    if(cpt == 0)
                        Ncases = atoi(ligne.c_str());
                    else
                        {
                                cerr <<"case "<<cpt <<endl;
                                vector<string> NB = split(ligne);
                                int a1 = atoi(NB[0].c_str());
                                int a2 = atoi(NB[1].c_str());
                                int a3 = atoi(NB[2].c_str());


                                int res = min_tir(a2,a3,a1);
                                cerr << "case #"<< cpt<<": "<<res<<endl;
                                //string ss = res ;
                                resultat.push_back(res);

                        }
                    cpt++;
            }
                fichier.close();  // on ferme le fichier
        }
        else  // sinon
                cerr << "Impossible d'ouvrir le fichier !" << endl;


        //for(int h=0;h<vec.size();h++)
          //      cerr<<"vec size "<<vec[h]<<endl;



        ofstream fichier1("C:/Users/Firas/Documents/codejam2/counter culture/culture.out", ios::out | ios::trunc);  // ouverture en écriture avec effacement du fichier ouvert

        if(fichier1)
        {
                for(int j=0;j<resultat.size();j++)
                fichier1 << "Case #" << j+1 <<": "<< resultat[j] <<endl;

                //fichier1 <<resultat[j]<<endl;
                fichier1.close();
        }
        else
                cerr << "Impossible d'ouvrir le fichier !" << endl;

    return 0;
}
