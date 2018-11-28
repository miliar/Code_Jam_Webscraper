// Author:   Charles AUGUSTE

#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <stdlib.h>

using namespace std;

int main(){
    ifstream fichier("D:/Charles/cours/Ponts/Info/GG/Sheep/test.txt", ios::in);
    if(fichier){
        ofstream fichier2("D:/Charles/cours/Ponts/Info/GG/Sheep/answer.txt", ios::out | ios::trunc);
        if(fichier2){
            string ligne;
            getline(fichier,ligne);
            int T = atoi(ligne.c_str());
            for (int i=0; i<T; ++i){
                int entier=0;
                int sol =0;
                bool t[10]={false};
                getline(fichier,ligne);
                entier = atoi(ligne.c_str());
                if (entier==0)
                    fichier2 << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
                else{
                    while (!(t[0] && t[1] && t[2] && t[3] && t[4] && t[5] && t[6] && t[7] && t[8] && t[9])){
                        sol+=entier;
                        stringstream ss;
                        ss << sol;
                        ligne = ss.str();
                        for (int j=0; j<ligne.size(); ++j){
                            t[int(ligne[j])-'0']=true;
                        }
                    }
                    fichier2 << "Case #" << i+1 << ": " << sol << endl;
                }
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
