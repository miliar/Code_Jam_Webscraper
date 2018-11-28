//ab.95
#include<iostream>
#include<string.h>
#include<fstream>
#include<stdlib.h>
using namespace std;
typedef unsigned long long ull;
int hsh[10];

int main()
{
ull var1,var2,var3,var4;
ull T,N,sum=0,s2=0,fall=0;



ifstream fin;
fin.open("GCJTA.txt");
ofstream fin2;
fin2.open("GCJRESA.txt");

fin>>T;

var2=T;
while(T--)
{
    var3=1;
    sum=0;
    s2=0;
    fin>>N;

    while((fall != 1 && N != 0 ))
    {
        fall=1;
        var4=var3*N;
        while(var4 != 0)
        {
            if(hsh[var4%10] == 0 )
                hsh[var4%10]=1;
            var4=var4/10;
        }
        for(var1=0;var1<=9;var1++)
        {
            fall=fall*hsh[var1];
        }
        var3=var3+1;

    }
    var4=(var3-1)*N;
    for(var1=0;var1<10;var1++)
        hsh[var1]=0;

    if(N!=0)
    {
        fin2<<"Case #"<<var2-T<<": "<<var4<<endl;

    }
    else
    {
        fin2<<"Case #"<<var2-T<<": "<<"INSOMNIA"<<endl;

    }

    fall=0;
}

fin.close();
fin2.close();

return 0;

}
