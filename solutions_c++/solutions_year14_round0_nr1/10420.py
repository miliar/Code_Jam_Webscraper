#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
int T =0 , valeur =0 , rows =0 , tab[2][4]={0} , nombre=0,compt=0;
ifstream Fichier("C:/Users/work/Desktop/A-Small/A-small-attempt0.txt");
ofstream output ("C:/Users/work/Desktop/A-Small/Output.txt") ;
// ouvrir le fichier !
if(Fichier)
{
Fichier >>T;
for (int n=0 ;n<T ;n++){
Fichier >> rows ;
for (int i=0 ; i<4 ; i++)
{
    for(int j=0 ; j<4 ;j++ )
    {
        Fichier >>nombre ;
        if ( rows==i+1) tab[0][j]=nombre ;
    }
}

Fichier >> rows ;
for (int i=0 ; i<4 ; i++)
{
    for(int j=0 ; j<4 ;j++ )
    {
        Fichier >>nombre ;
        if ( rows==i+1) tab[1][j]=nombre ;
    }
}

for (int i=0 ; i<4 ; i++)
{
    for(int j=0 ; j<4 ;j++ )
    {
        if (tab[0][i] == tab[1][j]) { valeur=tab[0][i] ;compt++ ; }
    }
    }

      if (compt==0 ) output <<"Case #"<<n+1<<": Volunteer cheated!"<<endl;
     if  (compt>1 ) output << "Case #"<<n+1<<": Bad magician!"<<endl;
    if(compt==1 ) output <<"Case #"<<n+1<<": "<<valeur<<endl;

    compt=0;

}

}
else
{
cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
}

    return 0;
}
