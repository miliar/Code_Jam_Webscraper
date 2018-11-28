#include <iostream>
#include <cstdio>
#include <vector>
#include <conio.h>
#include <string>
#include <fstream>

using namespace std;



ofstream izlazni("out.txt");


int provjeri_korijen(int A){

int B;
int i;
B = 1;

for( i = B; i < A; i++ ){
    if(i*i == A) return i;
}

if(i*i == A ) return i;


return 0;
}


int provjeri_palindrom( int A ){
if( A / 10 == 0 ) return 1;

int niz[100];
int duljina;
int i;
int var;
int usporedbe;

var = A;
duljina=0;
for(i=0;i<100;i++) niz[i] = 0;

i=0;
while(var>0){
    niz[i]=var%10;
    i++;
    var=var/10;
}
duljina = i;

if( duljina%2 == 0 ) usporedbe = duljina/2;
else usporedbe=(duljina-1)/2;

int brojac;
brojac =0;

for( i = 0; i < usporedbe; i++ ){
    if(niz[i] == niz[duljina-1-i]) brojac++;
}


if(brojac == usporedbe) return 1;
else return 0;
}



int provjeri(int A, int B){
int i;
int broj;
broj = 0;


for( i = A; i <= B; i++ )
{
    if( !provjeri_palindrom(i) ) continue;

    if( !provjeri_korijen(i) ) continue;

    int X = provjeri_korijen(i);

    if( !provjeri_palindrom(X) ) continue;

    broj++;
}

return broj;
}

int main(){
int T;
int A;
int B;
int izlaz;
int i;
izlaz = 0;

ifstream ulazniTok("ulaz2.txt");
ulazniTok>>T;

for( i = 0; i < T ; i++ ){

    ulazniTok >> A;
    ulazniTok >> B;

      izlaz = provjeri(A,B);
      izlazni << "Case #"<< i+1 <<": "<< izlaz<<"\n" ;


}


return 0;
}
