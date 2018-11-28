#include <iostream>
#include <fstream>

using namespace std;

int* transChaineTab(string chaine);

int main()
{
    ifstream input("input.in");
    ofstream output("output.out");
    if(input == NULL)
        return 1;
    int T, sMax, nbre, caisse;
    string s;
    int *tab;
    input >> T;
    for(int i = 0; i < T; i++){
        nbre = 0;
        caisse = 0;
        input >> sMax;
        input >> s;
        tab = transChaineTab(s);
        for(int j(0); j < s.size(); j++){
            if(tab[j] == 0){
                if(caisse == 0)
                    nbre++;
                else
                    caisse--;
            }else{
                caisse += tab[j]-1;
            }
        }
        output << "Case #" << i+1 << ": " << nbre;

        if(i+1 < T)
            output << endl;
    }
    return 0;
}

int* transChaineTab(string chaine){
    int taille = chaine.size();
    int *tab = new int[taille];
    for(int i(0); i < taille; i++)
        tab[i] = chaine[i] - '0';
    return tab;
}

