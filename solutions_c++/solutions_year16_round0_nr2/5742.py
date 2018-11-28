// Author:   Charles AUGUSTE

#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main(){
    ifstream fichier("D:/Charles/cours/Ponts/Info/GG/Pancake/test.txt", ios::in);
    if(fichier){
        ofstream fichier2("D:/Charles/cours/Ponts/Info/GG/Pancake/answer.txt", ios::out | ios::trunc);
        if(fichier2){
            char signe;
            string ligne;
            getline(fichier,ligne);
            int T = atoi(ligne.c_str());
            for (int i=0; i<T; ++i){
                int compteur=0;
                getline(fichier,ligne);
                signe=ligne[0];
                for (int j=1; j<ligne.size(); ++j){
                    if (ligne[j]!=signe)
                        compteur+=1;
                    signe=ligne[j];
                }
                if (signe=='-')
                    compteur+=1;
                fichier2 << "Case #" << i+1 << ": " << compteur << endl;
            }
            fichier.close();
            fichier2.close();
        }
        else
            cerr << "Erreur à l'ouverture !" << endl;
    }
        else
                cerr << "Impossible d'ouvrir le fichier !" << endl;
        return 0;
}
