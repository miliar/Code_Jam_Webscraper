#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int stringToInt(string myStream)
{
    istringstream buffer(myStream);
    int value;
    buffer >> value;
    return value;
}


int Correspondance(int* tab1,int* tab2)
{
    int nbCorrespondance = 0;
    for (int i = 0 ; i<4 ; i++)
    {
        for (int j=0 ; j<4 ; j++)
        {
            if (tab1[i] == tab2[j])
               nbCorrespondance ++;
        }
    }
    return nbCorrespondance;
}

int gzgzegGZG(int* tab1,int* tab2)
{
    for (int i = 0 ; i<4 ; i++)
    {
        for (int j=0 ; j<4 ; j++)
        {
            if (tab1[i] == tab2[j])
               return tab1[i];
        }
    }
}
int main()
{
    ifstream fichier("A-small-attempt0.in", ios::in);
    ofstream fichier2("output.out", ios::out | ios::trunc);
    int numberCase = 0;
    if (fichier)
    {
        string contenu;
        getline(fichier, contenu); //on récupère le nomnre de grid
        numberCase = stringToInt(contenu);
        for (int i =0 ; i<numberCase ; i++)
        {
            vector <string> grid1, grid2;
            getline(fichier, contenu);  //on récupère le numero de ligne
            int numeroLigne1 = stringToInt(contenu);
            for (int j=0 ; j<4 ; j++)
            {
                getline(fichier, contenu);
                grid1.push_back(contenu);

            }

            getline(fichier, contenu);  // on met dans "contenu" la ligne
            int numeroLigne2 = stringToInt(contenu);
            for (int j=0 ; j<4 ; j++)
            {
                getline(fichier, contenu);
                grid2.push_back(contenu);
            }

            //on transforme la ligne  numeroLigne1  en tableau
            int tab1[4], tab2[4];
            istringstream iss1(grid1[numeroLigne1-1]);
            istringstream iss2(grid2[numeroLigne2-1]);
            for ( int j=0 ; j<4 ; j++)
            {

                string sub1;
                iss1 >> sub1;
                tab1[j] = stringToInt(sub1);

                string sub2;
                iss2 >> sub2;
                tab2[j] = stringToInt(sub2);

            }

            int nbCorrespodance = Correspondance(tab1, tab2);
            fichier2 << "Case #" << i+1 <<": ";
            if (nbCorrespodance == 1)
                fichier2 << gzgzegGZG(tab1, tab2) << endl;
            else if (nbCorrespodance == 0)
                fichier2 << "Volunteer cheated!" << endl;
            else
                fichier2 << "Bad magician!" << endl;

        }
    }
    return 0;
}
