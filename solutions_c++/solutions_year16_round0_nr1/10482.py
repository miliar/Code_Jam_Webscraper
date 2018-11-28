#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

// Attribue les nombres
int number(int N , int init )
{
     int i(init) ;
    int name(0);
    name = init*N;
    i++;
    return name ;
}

//Verifier si le chiffre du nombre courant a été deja enregistrer
bool Appartient (vector<int> &tab ,int digit)
{
    int n = tab.size();
    for(int s = 0 ; s < n ; s++ )
    {
       if( tab[s] == digit )
        return true ;
    }
       return false ;
}

//Decompose le nombre courant et enregistre ses chiffres sans doublons
void Reg_digits(vector<int> &tab , int name )
{
    int digit(0);
    bool b ;
    while(name != 0)
    {
        if( name >= 10)
          digit = name%10;
        else
          digit = name;
       b = Appartient(tab,digit);
        if ( b == false )
            tab.push_back(digit);
        name = name/10 ;
    }
}

int main()
{
    int name(0);
    ifstream input("input.txt");
    ofstream output("ouput.txt");
    int nberCases(0);

    if(input){
        input >> nberCases;
    }
    else
    {
        cout << "ERREUR: Impossible de lire le fichier. " << endl;
    }

    int i(0) ;
    while( i < nberCases)
    {
        vector<int> tab;
        input>>name;
        int tmp = name;

        if(input)
       {
         if(name == 0)
         {
          output<< "case #" << i+1 << ": " <<  "INSOMNIA" << endl;
         }
         else
         {
            int j = 1 ;
            while(tab.size() != 10 )
            {
                Reg_digits(tab,name);
                j++;
                name = number(tmp,j);
            }

       // cout<<"***************************************"<<endl;
          output<< "case #" << i+1 << ": " << name-tmp << endl;
         }
        }else{
             cout << "ERREUR: Impossible d' ouvrir le fichier. " << endl;
        }
      i++;
    }
    input.close();
    return 0;
}
