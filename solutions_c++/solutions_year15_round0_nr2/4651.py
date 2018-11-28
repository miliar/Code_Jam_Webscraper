#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#define N 30000
using namespace std;

void Cakes(){
fstream wejscie;
fstream wyjscie;
wejscie.open("inn.txt", ios::in);
wyjscie.open("outt.txt", ios::out);
if(wejscie.good()==false)cout << "Cos sie spierdolilo" << endl;
if(wyjscie.good()==false)cout << "not again please" << endl;
int Pancakes[N],Pancakes2[N],tests,diners; // data
int minimum, minutes, minutes2;


wejscie >> tests;
for(int i=0;i<tests;i++){
    wejscie >> diners;
    for(int j=0;j<diners;j++)wejscie >> Pancakes[j];
    for(int j=0;j<diners;j++)Pancakes[j] *= -1;
    sort(Pancakes, Pancakes+diners);
    for(int j=0;j<diners;j++)Pancakes[j] *= -1;
        //for(int j=0;j<diners;j++)wyjscie << Pancakes[j] << " ";
    for(int j=0;j<diners;j++)Pancakes2[j] = Pancakes[j];

    minutes = 0;
    minutes2 = 2;
    minimum = Pancakes[0];
        while(Pancakes[0]!=1){
        Pancakes[diners+minutes] = Pancakes[0]/2;
        Pancakes[0] -= Pancakes[diners+minutes];
        //wyjscie << "WTF " << Pancakes[0] <<" " << Pancakes[diners+minutes]/2;
        minutes++;
        for(int j=0;j<diners+minutes;j++)Pancakes[j] *= -1;
        sort(Pancakes, Pancakes+diners+minutes);
        for(int j=0;j<diners+minutes;j++)Pancakes[j] *= -1;
            //for(int j=0;j<diners+minutes;j++)wyjscie << Pancakes[j] << " ";
            //wyjscie << endl;
        if(minimum > Pancakes[0]+minutes)minimum = Pancakes[0]+minutes;
}
    if(Pancakes2[0]==9){
        Pancakes2[0] = 3; Pancakes2[diners] = 3; Pancakes2[diners+1] = 3;
        for(int j=0;j<diners+minutes2;j++)Pancakes2[j] *= -1;
        sort(Pancakes2, Pancakes2+diners+minutes2);
        for(int j=0;j<diners+minutes2;j++)Pancakes2[j] *= -1;
        if(minimum > Pancakes2[0]+minutes2)minimum = Pancakes2[0]+minutes2;
        while(Pancakes2[0]!=1){
            Pancakes2[diners+minutes2] = Pancakes2[0]/2;
            Pancakes2[0]-=Pancakes2[diners+minutes2];
            minutes2++;
            for(int j=0;j<diners+minutes2;j++)Pancakes2[j] *= -1;
            sort(Pancakes2, Pancakes2+diners+minutes2);
            for(int j=0;j<diners+minutes2;j++)Pancakes2[j] *= -1;
                //for(int j=0;j<diners+minutes2;j++)wyjscie << Pancakes2[j] << " ";
                //wyjscie << endl;
            if(minimum > Pancakes2[0]+minutes2)minimum = Pancakes2[0]+minutes2;
    }}
    wyjscie << "Case #" << i+1 << ": " << minimum << endl;
}}


int main(){
Cakes();
return 0;
}
