#include<iostream>

using namespace std;
char a[5][5];
char pom;
bool(nieskonczona)=false;
bool testa (int test)
{
    bool wypisz=false;
    if(a[0][0]!='X' && a[0][0]!='.' && a[0][1]!='X' && a[0][1]!='.' && a[0][2]!='X' && a[0][2]!='.' && a[0][3]!='X' && a[0][3]!='.') wypisz=true;
    if(a[1][0]!='X' && a[1][0]!='.' && a[1][1]!='X' && a[1][1]!='.' && a[1][2]!='X' && a[1][2]!='.' && a[1][3]!='X' && a[1][3]!='.') wypisz=true;
    if(a[2][0]!='X' && a[2][0]!='.' && a[2][1]!='X' && a[2][1]!='.' && a[2][2]!='X' && a[2][2]!='.' && a[2][3]!='X' && a[2][3]!='.') wypisz=true;
    if(a[3][0]!='X' && a[3][0]!='.' && a[3][1]!='X' && a[3][1]!='.' && a[3][2]!='X' && a[0][2]!='.' && a[3][3]!='X' && a[3][3]!='.') wypisz=true;

    if(a[0][0]!='X' && a[0][0]!='.' && a[1][0]!='X' && a[1][0]!='.' && a[2][0]!='X' && a[2][0]!='.' && a[3][0]!='X' && a[3][0]!='.') wypisz=true;
    if(a[0][1]!='X' && a[0][1]!='.' && a[1][1]!='X' && a[1][1]!='.' && a[2][1]!='X' && a[2][1]!='.' && a[3][1]!='X' && a[3][1]!='.') wypisz=true;
    if(a[0][2]!='X' && a[0][2]!='.' && a[1][2]!='X' && a[1][2]!='.' && a[2][2]!='X' && a[2][2]!='.' && a[3][2]!='X' && a[3][2]!='.') wypisz=true;
    if(a[0][3]!='X' && a[0][3]!='.' && a[1][3]!='X' && a[1][3]!='.' && a[2][3]!='X' && a[2][3]!='.' && a[3][3]!='X' && a[3][3]!='.') wypisz=true;

    if(a[0][0]!='X' && a[0][0]!='.' && a[1][1]!='X' && a[1][1]!='.' && a[2][2]!='X' && a[2][2]!='.' && a[3][3]!='X' && a[3][3]!='.') wypisz=true;
    if(a[0][3]!='X' && a[0][3]!='.' && a[1][2]!='X' && a[1][2]!='.' && a[2][1]!='X' && a[2][1]!='.' && a[3][0]!='X' && a[3][0]!='.') wypisz=true;

    if(wypisz==true)
    {
        cout<<"Case #"<<test<<": O won\n";
        return false;
    }
    else return true;
}
bool testb (int test)
{
    bool wypisz=false;
    if(a[0][0]!='O' && a[0][0]!='.' && a[0][1]!='O' && a[0][1]!='.' && a[0][2]!='O' && a[0][2]!='.' && a[0][3]!='O' && a[0][3]!='.') wypisz=true;
    if(a[1][0]!='O' && a[1][0]!='.' && a[1][1]!='O' && a[1][1]!='.' && a[1][2]!='O' && a[1][2]!='.' && a[1][3]!='O' && a[1][3]!='.') wypisz=true;
    if(a[2][0]!='O' && a[2][0]!='.' && a[2][1]!='O' && a[2][1]!='.' && a[2][2]!='O' && a[2][2]!='.' && a[2][3]!='O' && a[2][3]!='.') wypisz=true;
    if(a[3][0]!='O' && a[3][0]!='.' && a[3][1]!='O' && a[3][1]!='.' && a[3][2]!='O' && a[0][2]!='.' && a[3][3]!='O' && a[3][3]!='.') wypisz=true;

    if(a[0][0]!='O' && a[0][0]!='.' && a[1][0]!='O' && a[1][0]!='.' && a[2][0]!='O' && a[2][0]!='.' && a[3][0]!='O' && a[3][0]!='.') wypisz=true;
    if(a[0][1]!='O' && a[0][1]!='.' && a[1][1]!='O' && a[1][1]!='.' && a[2][1]!='O' && a[2][1]!='.' && a[3][1]!='O' && a[3][1]!='.') wypisz=true;
    if(a[0][2]!='O' && a[0][2]!='.' && a[1][2]!='O' && a[1][2]!='.' && a[2][2]!='O' && a[2][2]!='.' && a[3][2]!='O' && a[3][2]!='.') wypisz=true;
    if(a[0][3]!='O' && a[0][3]!='.' && a[1][3]!='O' && a[1][3]!='.' && a[2][3]!='O' && a[2][3]!='.' && a[3][3]!='O' && a[3][3]!='.') wypisz=true;

    if(a[0][0]!='O' && a[0][0]!='.' && a[1][1]!='O' && a[1][1]!='.' && a[2][2]!='O' && a[2][2]!='.' && a[3][3]!='O' && a[3][3]!='.') wypisz=true;
    if(a[0][3]!='O' && a[0][3]!='.' && a[1][2]!='O' && a[1][2]!='.' && a[2][1]!='O' && a[2][1]!='.' && a[3][0]!='O' && a[3][0]!='.') wypisz=true;

    if(wypisz==true)
    {
        cout<<"Case #"<<test<<": X won\n";
        return false;
    }
    else return true;
}
int main()
{
    int t;
    cin>>t;
    for(int test=1; test<=t; test++)
    {
        nieskonczona=false;
        for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
        {
            cin>>pom;
            if(pom=='.')nieskonczona=true;
            a[i][j]=pom;
        }
        bool czydalej=false;
        czydalej=testa(test);
        if(czydalej==true)
        czydalej=testb(test);
        if(czydalej==true)
        {
            if(nieskonczona==true)cout<<"Case #"<<test<<": Game has not completed\n";
            else cout<<"Case #"<<test<<": Draw\n";
        }

    }
}
