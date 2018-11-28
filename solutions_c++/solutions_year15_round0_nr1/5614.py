#include <iostream>
#include <fstream>


using namespace std;

    string people;

    int numerito(int k)
    {
        switch (people[k])
        {
       case '0':return 0;
        break;
       case '1':return 1;
        break;
       case '2':return 2;
        break;
       case '3':return 3;
        break;
       case '4':return 4;
        break;
       case '5':return 5;
        break;
       case '6':return 6;
        break;
       case '7':return 7;
        break;
       case '8':return 8;
        break;
       case '9':return 9;
        break;

        }
    }


int main()
{
    ifstream in("A-large.in");
    ofstream out("salida.out");


    int t,pen,i,shy,k;
    long int invitados,cont;
in>>t;
    for(k=1;k<=t;k++)
    {
        invitados=0;
        cont=0;
    in>>pen>>people;
    for(i=0;i<=pen;i++)
    {
        if(cont<i)
        {
         invitados=invitados+i-cont;
         cont=i;
        }
        shy=numerito(i);
        cont=cont+shy;


    }
    out<<"Case #"<<k<<": "<<invitados<<endl;

    }


    in.close();
    out.close();
    return 0;
}
