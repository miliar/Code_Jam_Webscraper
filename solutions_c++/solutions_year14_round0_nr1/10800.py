#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    int tableau1[4];
    int tableau2[4];
    int tableau3[4];
    int T(0);
    int numeroligne(0);
    int compteur(0);
    int nbrecommun(0);
    int carteCommune(0);
    string chaine;
    string nomfichier1("smallpratice.out");
    ifstream ft("A-small-attempt0.in");
    ofstream fs(nomfichier1.c_str(),ios::app);
       ft>>T;
       if(ft!=NULL)
       {
        for(int i(0);i<T;i++)
        {

           ft>>numeroligne;
           compteur=0;
           while(compteur<numeroligne)
           {
               getline(ft,chaine);
               compteur+=1;
           }
           for(int j(0);j<4;j++)
           {
               ft>>tableau1[j];
           }
           if(numeroligne<4)
           {
               compteur=0;
               while(compteur<4-numeroligne)
               {
                   for(int m(0);m<4;m++)
                   {
                       ft>>tableau3[m];
                   }
                   compteur+=1;
               }
           }
           ft>>numeroligne;
           compteur=0;
           while(compteur<numeroligne)
           {
               getline(ft,chaine);
               compteur+=1;
           }
           for(int k(0);k<4;k++)
           {
               ft>>tableau2[k];
           }
           if(numeroligne<4)
           {
               compteur=0;
               while(compteur<4-numeroligne)
               {
                   for(int m(0);m<4;m++)
                   {
                       ft>>tableau3[m];
                   }
                   compteur+=1;
               }
           }
           nbrecommun=0;
           for(int s(0);s<4;s++)
           {
               int n(0);
               while(n<4)
               {
                   if(tableau1[n]==tableau2[s])
                   {
                       nbrecommun+=1;
                       carteCommune=tableau1[n];
                   }
                   n+=1;
               }
           }
           if(nbrecommun==0)
           {
               fs<<"Case #"<<i+1<<": Volunteer cheated!\n"<<endl;
           }else{
               if(nbrecommun==1)
               {
                   fs<<"Case #"<<i+1<<": "<<carteCommune<<"\n"<<endl;
               }else{
                   fs<<"Case #"<<i+1<<": Bad magician!\n"<<endl;
               }
           }
        }

       }
    return 0;
}
