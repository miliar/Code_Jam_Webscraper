//ab.95
#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
int L,X,R,C,T;
ifstream fin;
fin.open("GCJT.txt");
ofstream fin2;
fin2.open("GCJRES.txt");
fin>>T;
L=T;
while(T--)
{
fin>>X>>R>>C;
if(X==1){
fin2<<"Case #"<<L-T<<": "<<"GABRIEL"<<endl;
continue;
}
if(X>(R*C))
{
fin2<<"Case #"<<L-T<<": "<<"RICHARD"<<endl;
continue;
}
if((R*C)%X!=0)
{
fin2<<"Case #"<<L-T<<": "<<"RICHARD"<<endl;
continue;
}
if(X==2)
{
if((R*C)%2==0)
{
fin2<<"Case #"<<L-T<<": "<<"GABRIEL"<<endl;
continue;
}
}
if(X==3)
{
    if(R*C==3)

     {
fin2<<"Case #"<<L-T<<": "<<"RICHARD"<<endl;
continue;
}
        else if(R*C==6)
        {
            {
fin2<<"Case #"<<L-T<<": "<<"GABRIEL"<<endl;
continue;
}

        }
 else if(R*C==9)
            {
fin2<<"Case #"<<L-T<<": "<<"GABRIEL"<<endl;
continue;
}
else if (R*C==12)
    {
fin2<<"Case #"<<L-T<<": "<<"GABRIEL"<<endl;
continue;
}
}
if(X==4)
{
    if(R*C==4)
     {
fin2<<"Case #"<<L-T<<": "<<"RICHARD"<<endl;
continue;
}
else if(R*C==8)
            {
fin2<<"Case #"<<L-T<<": "<<"RICHARD"<<endl;
continue;
}
else if(R*C==12)
     {
fin2<<"Case #"<<L-T<<": "<<"GABRIEL"<<endl;
continue;
}
else if (R*C==16)
     {
fin2<<"Case #"<<L-T<<": "<<"GABRIEL"<<endl;
continue;
}
}
}
}
