#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;

string IntToString(double Mon_Nbr)
{
    // créer un flux de sortie
    std::ostringstream oss;
    // écrire un nombre dans le flux
    oss << Mon_Nbr;
    // récupérer une chaîne de caractères

    return oss.str();
}


bool Palindrome(double Mon_Nbr){
    string Ma_Chaine=IntToString(Mon_Nbr);
    int Taille=Ma_Chaine.size();
    for(int i=0;i<Taille/2;i++)
    {
        if(Ma_Chaine[i]!=Ma_Chaine[Taille-i-1]) return false;

    }
   //cout<<Ma_Chaine<<endl;
    return true;
}



int main()
{
    //// Uouvrir Les fichiers
    string mon_fichier = "C-small-attempt.in";  // je stocke dans la chaîne mon_fichier le nom du fichier à ouvrir
    ifstream fichier(mon_fichier.c_str(), ios::in);
    if(! fichier)  // si l'ouverture a réussi
    {
        cerr << "Erreur à l'ouverture !" << endl;
        return 0;
     }
     mon_fichier = "C-small.out";
    ofstream fichier_tampon(mon_fichier.c_str(), ios::out | ios::trunc);

    //Recupere le nombre de tests
     string Mes_Chaine="";
     int Nbr_cas=0;

     getline(fichier,Mes_Chaine);
     istringstream iss(Mes_Chaine);
     iss>>Nbr_cas;


     for(int i=1;i<=Nbr_cas;i++)
     {
        //Recuperer la hauteur et la longueur des matrices
         getline(fichier,Mes_Chaine);
         //   cout<<Mes_Chaine<<endl;
         istringstream iss(Mes_Chaine );
         float Borne_Min=-1;
         float Borne_Max=-1;
         string mot;
         while ( std::getline( iss, mot, ' ' ) )
        {
            istringstream s( mot );
            if(Borne_Min>=0)
            {
                s>>Borne_Max;
                break;
            }
            else s>> Borne_Min;
        }
        float Limite_Max=sqrt(Borne_Max);
        float Limite_Min=floor(sqrt(Borne_Min));
        int nbr_Pal=0;
        //cout<<Limite_Min<<" "<<Limite_Max<<endl;
        while (Limite_Min<=Limite_Max)
        {
            if (Palindrome(Limite_Min))
            {
                    float Mon_Carre=Limite_Min*Limite_Min;
                    if (Mon_Carre>=Borne_Min && Mon_Carre<=Borne_Max  )
                    {
                        if (Palindrome(Mon_Carre)) nbr_Pal++;

                    }

            }

            Limite_Min+=1;
        }
         fichier_tampon<<"Case #"<<i<<": "<<nbr_Pal<<endl;
         //cout<<"Case #"<<i<<": "<<nbr_Pal<<endl;



}
}
