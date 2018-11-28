#include <iostream>
#include <stdio.h>
#include <cmath>
#include <fstream>
using namespace std;

double medium (double c,double f,double t,double null)
{

double res = 0.0;
while (t > (c*(f+null)/f) )
{
    res+=c/null;
    null+=f;
}
res+=t/null;
return res;
}
int main ()
{
    // lets rock again ants and cats.. :P
    ifstream ant;
    ant.open("ant.in");
    FILE * ptrmy; // precision requird
    ptrmy = fopen("cat4.txt","w");
    int f;
    ant>>f;
    for(int F = 1;  F <= f;F++)
    {
        double c,f,t;
        ant>>c>>f>>t;
        double  p = medium(c,f,t,2.0);
        fprintf(ptrmy,"Case #");
        fprintf(ptrmy,"%d",F);
        fprintf(ptrmy,": ");
        fprintf(ptrmy,"%.7f \n",p);
    }

    fclose(ptrmy);
}
