#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;
ifstream in ("RevengeofthePancakes.in");
ofstream out ("RevengeofthePancakes.out");
char clatite[105];
bool fata[105];
int rot;
bool verificare()
{
    for(int i=0;i<strlen(clatite);i++)
        if(fata[i]==0)
            return 0;
    return 1;
}
void schimbare()
{
    int p=1, i;
    for(i=1;i<strlen(clatite);i++)
        if(fata[i]!=fata[i-1])
        {
            p=i;
            break;
        }
    if (i == strlen(clatite))
       p = strlen(clatite);
    bool sc[105];
    for(int i=0;i<p;i++)
        sc[i]=!fata[p-i-1];
    for(int i=0;i<p;i++)
        fata[i]=sc[i];
}
void adv()
{
    for(int i=0;i<strlen(clatite);i++)
        if(fata[i]==1)
            return ;
    for(int i=0;i<strlen(clatite);i++)
        fata[i]=1;
    rot++;
}
void rezolvare()
{
    while(verificare()==0)
    {
        rot++;
        schimbare();
        adv();
    }
}
void conversie()
{
    for(int i=0;i<strlen(clatite);i++){
        if(clatite[i]=='+')
            fata[i]=1;
        else
            fata[i]=0;
    }
}
int main()
{
    int t;
    in>>t;
    in.getline(clatite,105);
    for(int i=0;i<t;i++)
    {
        in.getline(clatite,105);
        conversie();
        rezolvare();
        out<<"Case #"<<i+1<<": "<<rot<<"\n";
        rot=0;
    }
    return 0;
}
