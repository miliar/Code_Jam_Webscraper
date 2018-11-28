#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int verificare(int *v,int shylvl)
{
    int prieteni=0,s=v[0];
    for(int i=1;i<=shylvl;i++)
    {
        if(s>=i)
        {
           s+=v[i];
        }

        else
        {
            if(v[i])
            {
                prieteni+=i-s;
                s+=v[i]+(i-s);
            }

        }
    }
    return prieteni;
}

void citire(char *inputfile,char *outputfile,int nrc,int shylvl,int *v)
{
    ifstream f(inputfile);
    ofstream g(outputfile);
    f>>nrc;
    char *str;
    int n;
    for(int i=0;i<nrc;i++)
    {
        f>>shylvl;
        v=new int[shylvl+1];
        str=new char[shylvl];
        for(int j=0;j<shylvl+1;j++)
        {
            f>>str[j];
            v[j]=str[j] - '0';
        }
        g<<"Case #"<<i+1<<": "<<verificare(v,shylvl)<<endl;
    }

}



int main()
{
    int nrcase,shylvl;
    int *v;
    citire("A-small-attempt5.in","prieteni.out",nrcase,shylvl,v);

    return 0;
}
