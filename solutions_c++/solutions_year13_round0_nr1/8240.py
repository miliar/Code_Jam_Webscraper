#include<fstream>
#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{

ifstream in;
ofstream ou;
int n,m=1,i,j,k;
char a[4][4],ar;


in.open("A-small-attempt.in",ios::in);
if(!in)
{
cout<<"input File error";
return 0;
}
ou.open("A-small.out",ios::out);
if(!ou)
{
cout<<"ouput File error";
return 0;
}
in>>n;
cout<<n;
while(m<=n)
{
ou<<"Case #"<<m<<": ";
m++;
k=0;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
in>>a[i][j];

ar=a[0][0];
    if(ar=='X')
        if(((a[1][1]=='X')||(a[1][1]=='T'))&&((a[2][2]=='X')||(a[2][2]=='T'))&&((a[3][3]=='X')||(a[3][3]=='T')))
        {
        ou<<"X won\n";cout<<"1";
        continue;
        }
     if(ar=='O')
        if(((a[1][1]=='O')||(a[1][1]=='T'))&&((a[2][2]=='O')||(a[2][2]=='T'))&&((a[3][3]=='O')||(a[3][3]=='T')))
        {
        ou<<"O won\n";cout<<"2";
        continue;
        }
    if(ar=='T')
        if((a[1][1]==a[2][2])&&(a[2][2]==a[3][3])&&(a[3][3]!='.'))
        {
        ou<<a[1][1]<<" won\n";cout<<"3";
        continue;
        }

   ar=a[3][0];
    if(ar=='X')
        if(((a[2][1]=='X')||(a[2][1]=='T'))&&((a[1][2]=='X')||(a[1][2]=='T'))&&((a[0][3]=='X')||(a[0][3]=='T')))

        {
        ou<<"X won\n";cout<<"4";
        continue;
        }
    if(ar=='O')
        if(((a[2][1]=='O')||(a[2][1]=='T'))&&((a[1][2]=='O')||(a[1][2]=='T'))&&((a[0][3]=='O')||(a[0][3]=='T')))
        {
        ou<<"O won\n";cout<<"5";
        continue;
        }
    if(ar=='T')
        if((a[2][1]==a[1][2])&&(a[1][2]==a[0][3])&&(a[0][3]!='.'))
        {
        ou<<a[2][1]<<" won\n";cout<<"6";
        continue;
        }
if(k==0)
for(i=0;i<4;i++)
{
    ar=a[i][0];
    if(ar=='X')
        if(((a[i][1]=='X')||(a[i][1]=='T'))&&((a[i][2]=='X')||(a[i][2]=='T'))&&((a[i][3]=='X')||(a[i][3]=='T')))
        {
        ou<<"X won\n";k=1;cout<<"7";
        break;
        }
    if(ar=='O')
        if(((a[i][1]=='O')||(a[i][1]=='T'))&&((a[i][2]=='O')||(a[i][2]=='T'))&&((a[i][3]=='O')||(a[i][3]=='T')))
        {
        ou<<"O won\n";k=1;cout<<"8";
        break;
        }
    if(ar=='T')
        if((a[i][1]==a[i][2])&&(a[i][2]==a[i][3])&&(a[i][3]!='.'))
        {
        ou<<a[i][1]<<" won\n";k=1;cout<<"9";
        break;
        }
}
if(k==0)
for(i=0;i<4;i++)
{
    ar=a[0][i];
    if(ar=='X')
        if(((a[1][i]=='X')||(a[1][i]=='T'))&&((a[2][i]=='X')||(a[2][i]=='T'))&&((a[3][i]=='X')||(a[3][i]=='T')))
        {
        ou<<"X won\n";k=1;cout<<"A";
        break;
        }
    if(ar=='O')
        if(((a[1][i]=='O')||(a[1][i]=='T'))&&((a[2][i]=='O')||(a[2][i]=='T'))&&((a[3][i]=='O')||(a[3][i]=='T')))
        {
        ou<<"O won\n";k=1;cout<<"B";
        break;
        }
    if(ar=='T')
        if((a[1][i]==a[2][i])&&(a[2][i]==a[3][i])&&(a[3][i]!='.'))
        {
        ou<<a[i][1]<<" won\n";k=1;cout<<"C";
        break;
        }
}


if(k==0)
{
for(i=0;i<4;i++)
for(j=0;j<4;j++)
if(a[i][j]=='.')
{
    ar=a[i][j];
}
if(ar=='.')
{ou<<"Game has not completed\n";cout<<"D";}
else{
ou<<"Draw\n";cout<<"E";
}
}

}

in.close();
ou.close();
return 0;

}
