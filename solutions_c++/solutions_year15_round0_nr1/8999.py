#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include<fstream>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int numero(char c)
{
if(c=='0')
return 0;
if(c=='1')
return 1;
if(c=='2')
return 2;
if(c=='3')
return 3;
if(c=='4')
return 4;
if(c=='5')
return 5;
if(c=='6')
return 6;
if(c=='7')
return 7;
if(c=='8')
return 8;
if(c=='9')
return 9;

}

int main(){
	int n_istanze;
	int maxlevel;
	in>>n_istanze;


int somma=0;
int result=0;
int pos;
string stringa;

for(int caso=1; caso<=n_istanze; caso++)
{
    //cout<<caso<<endl;
    in>>maxlevel;
    in>>stringa;
    somma=numero(stringa[0]);
    result=0;
    //cout<<"somma "<<somma<<endl;
  //  cout<<"somma iniziale = "<<numero(stringa[0]);

    for(int i=1; i<=maxlevel; i++)
    {
        if(numero(stringa[i])!=0)
        if(i > somma){
            result= result + ( i - somma);
            somma += (i-somma);
        }
        somma=somma + numero(stringa[i]);
         //  cout<<"ciclo  "<<i<<"  somma "<<somma<<" res  "<<result<<endl;
    }

out<<"Case #"<<caso<<": "<<result<<endl;

}
out.close();
return 0;
}
