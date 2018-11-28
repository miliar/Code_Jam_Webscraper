//ab.95
#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
int smax,T,k;
int var1,var2;
ifstream fin;
fin.open("GCJT.txt");
ofstream fin2;
fin2.open("GCJRES.txt");
fin>>T;
var2=T;
while(T--)
{
    k=0;
    fin>>smax;
    string s;
    char*c=(char*)malloc(sizeof(char)*(smax+1));
    //getchar();
    fin.ignore();
   getline(fin,s);
    int*p=(int*)malloc(sizeof(int)*(smax+1));
    int*sum=(int*)malloc(sizeof(int)*(smax+1));
    *sum=(s[0]-'0');
    for(var1=0;var1<=smax;var1++)
    {
        *(p+var1)=(s[var1]-'0');
        if(var1>0)
        *(sum+var1)=*(sum+var1-1)+*(p+var1);
    }
    for(var1=0;var1<=smax;var1++)

    for(var1=1;var1<=smax;var1++)
        {

            if(*(sum+var1-1)+k<var1)
            {
                k=k+var1-(*(sum+var1-1)+k);

            }
        }

        fin2<<"Case #"<<var2-T<<": "<<k<<endl;
}
return 0;
}
