#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void Stand_Up(){
fstream wejscie;
fstream wyjscie;
wejscie.open("inn.txt", ios::in);
wyjscie.open("outt.txt", ios::out);
int suma, tests, Smax, friends;
string Audience;

if(wejscie.good()==false)cout << "Cos sie spierdolilo" << endl;
if(wyjscie.good()==false)cout << "not again please" << endl;
wejscie >> tests;
for(int i=0; i<tests; i++){
    suma = 0; friends = 0;
    wejscie >> Smax >> Audience;
    for(int j=0; j<Smax+1; j++){
        //wyjscie << "suma " << suma << " j " << j << " friends" << friends << endl;
        if(suma >= j)suma += Audience[j] - 48;
        else{
            friends += j-suma;
            suma = j;
            suma += Audience[j] - 48;
            //wyjscie << "zmiana j " << j << " suma " << suma << "friends" << friends << endl;
        }
        //wyjscie << "Au " << Audience[j] << " " << endl;
        }
    //wyjscie << "suma " << suma << " j " << Smax << " friends" << friends << endl;
    wyjscie << "Case #" << i+1 << ": " << friends << endl;
}}

int main(){
Stand_Up();
return 0;
}
