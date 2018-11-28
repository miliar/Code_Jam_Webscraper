#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void Ecrire(string Vertical,string Horizontal,string Diagonales_D,string Diagonales_G,int i,bool Pas_Terminer)
{
    string mon_fichier = "A-small.out";
    ofstream fichier_tampon(mon_fichier.c_str(), ios::app);

    if((Horizontal=="OOOO") || (Diagonales_D=="OOOO") ||  (Diagonales_G=="OOOO"))
           {
                fichier_tampon<<"Case #"<<i<<": O won"<<endl;
           } else if (Horizontal=="XXXX" || Diagonales_D=="XXXX" ||  Diagonales_G=="XXXX")
           {
                fichier_tampon<<"Case #"<<i<<": X won"<<endl;
           }else
           {
                for(int k=0; k<4;k++)
                {
                    if(Vertical[k]=='O' ||Vertical[k]=='X' )
                    {
                        fichier_tampon<<"Case #"<<i<<": "<<Vertical[k]<<" won"<<endl;
                      return;
                    }
                }
                if (Pas_Terminer) fichier_tampon<<"Case #"<<i<<": Game has not completed"<<endl;
                else fichier_tampon<<"Case #"<<i<<": Draw"<<endl;
            }
}

int main()
{
    string mon_fichier = "A-small-attempt.in";  // je stocke dans la chaîne mon_fichier le nom du fichier à ouvrir
    ifstream fichier(mon_fichier.c_str(), ios::in);
    if(! fichier)  // si l'ouverture a réussi
    {
        cerr << "Erreur à l'ouverture !" << endl;
        return 0;
    }
    mon_fichier = "A-small.out";
    ofstream fichier_tampon(mon_fichier.c_str(), ios::out | ios::trunc);
    fichier_tampon.close();
    int Nbr_cas=0;
    fichier>>Nbr_cas;
    //cout<<Nbr_cas<<endl;
    for(int i=1;i<=Nbr_cas;i++)
    {
    cout<<endl<<i<<endl;
    string Vertical="    ";
    string Horizontal="    ";
    string Diagonales_D="    ";
    string Diagonales_G="    ";

    bool Pas_Terminer=false;
    string ligne;
    fichier>>ligne;
    //cout<<ligne<<endl;
    if (ligne=="") fichier>>ligne; //cout<<ligne<<endl;}

    Horizontal=ligne;
    Vertical=ligne;
    Diagonales_D=ligne;
    Diagonales_G=ligne;
    Diagonales_D[0]=ligne[3];

    for(int k=1; k<4;k++)
    {
        if (ligne=="....")
        {
            Pas_Terminer=true;
            for(int l=k; l<4;l++)
            {
                fichier>>ligne;
            }
            break;
        }
        fichier>>ligne;

        // Gagner horizontalement
        if(Horizontal=="OOOO" || Horizontal=="OOOT" || Horizontal=="OOTO" || Horizontal=="OTOO" || Horizontal=="TOOO" || Horizontal=="XXXX" || Horizontal=="XXXT" || Horizontal=="XXTX" ||  Horizontal=="XTXX"|| Horizontal=="TXXX")
        {
            for(int l=k+1; l<4;l++)
            {
                fichier>>ligne;
            }
            break;

        }
        Horizontal=ligne;

        // Gagner horizontalement
        for(int j=0; j<4;j++)
        {
            if(!(Vertical[j]==ligne[j] || ligne[j]=='T' || Vertical[j]=='T'))
            {
                if (ligne[j]=='.' && !Pas_Terminer) Pas_Terminer=true;
                Vertical[j]='?';
            } else Vertical[j]=ligne[j]=='T'?Vertical[j]:ligne[j];
        }

        if(!(Diagonales_G[k-1]==ligne[k] || ligne[k]=='T'|| Diagonales_G[k]=='T' || Diagonales_G[k-1]=='T'))
        {
            Diagonales_G[k]='?';
        }else
        {
            if(Diagonales_G[k-1]=='T')
            {
                Diagonales_G[k-1]=ligne[k];
            }
            Diagonales_G[k]=Diagonales_G[k-1];
        }

        if(!(Diagonales_D[k-1]==ligne[3-k] || ligne[3-k]=='T' || Diagonales_D[k-1]=='T' || Diagonales_D[k]=='T'))
        {
            Diagonales_D[k]='?';
        }else
        {

            if(Diagonales_D[k-1]=='T')
            {
                Diagonales_D[k-1]=ligne[3-k];
            }
            Diagonales_D[k]=Diagonales_D[k-1];
       }
      }

        if(Horizontal=="OOOO" || Horizontal=="OOOT" || Horizontal=="OOTO" || Horizontal=="OTOO" || Horizontal=="TOOO")
        {
            Horizontal="OOOO";

        } else if(Horizontal=="XXXX" || Horizontal=="XXXT" || Horizontal=="XXTX" ||  Horizontal=="XTXX"|| Horizontal=="TXXX")
        {
            Horizontal="XXXX";
        }
       Ecrire(Vertical,Horizontal,Diagonales_D,Diagonales_G,i,Pas_Terminer);

    }







    return 0;
}
