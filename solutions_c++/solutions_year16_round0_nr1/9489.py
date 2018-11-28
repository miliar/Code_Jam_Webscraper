#include <iostream>
#include<vector>
#include<fstream>
#include<cmath>
using namespace std;
ofstream rezfille;
ifstream ulfille;
int main()
{
    ulfille.open("A-large.in");

    rezfille.open("rezultati.txt");
    int bzvz;
    ulfille>>bzvz;
    vector<int> ulazi;

    for(int x=0;x<bzvz;x++ )
    {
        int pom;
        ulfille>>pom;
        ulazi.push_back(pom);
    }



    for(int x=0;x<bzvz;x++ )
    {
        int pocetni=ulazi[x];
        bool negpoc=false;
        if(pocetni<0)
        {
        pocetni=abs(pocetni);
        negpoc=true;
        }
     vector<bool> cifre(9);
    int number;
    number=pocetni;
    int pamtim;
    int cifra;
    int rez;
    bool kraj;
    if (pocetni==0)
    {
        rezfille<<"Case #"<<x+1<<": INSOMNIA"<<"\n";
        kraj==false;

    }
    else
    {

    do
    {
        rez=number;
        do{
        cifra=rez%10;
        rez=rez/10;
        cifre[cifra]=true;
        }while(rez !=0);

         kraj=true;
        for(int i=0;i<=9;i++)
        {
            if(cifre[i]==false)
                {
                    kraj=false;
                    break;
                }
        }
        if(!kraj)
        {
        number+=pocetni;
        }
        else
        {
            rezfille<<"Case #"<<x+1<<": ";
            if(negpoc)
            {
                number=(-1)*number;
            rezfille<<number<<"\n";
            }
            else
                rezfille<<number<<"\n";

        }
    }while(!kraj);
    }
}
    ulfille.close();
    rezfille.close();
    return 0;
}
