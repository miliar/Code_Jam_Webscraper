//"Lawnmower" by Shintero
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

short N, a, b, i;

bool oblicz(short a, short b)
{
short TAB[a][b];
short k, l, x, m;
bool wiersz, kolumna;
for(k=0; k<a; k++)
   for(l=0; l<b; l++)
      cin >> TAB[k][l];
//Przypadek brzegowy
if(a==1 || b==1)
   return true;
   
for(k=0; k<a; k++)
   {for(l=0; l<b; l++)
      {x=TAB[k][l];
      wiersz=true; kolumna=true;
      for(m=0; m<b; m++)
         if(TAB[k][m]>x)
            wiersz=false;
      for(m=0; m<a; m++)
         if(TAB[m][l]>x)
            kolumna=false;
      if(wiersz==false && kolumna==false)
         return false;}
   }
return true;
}

int main()
{
ios_base::sync_with_stdio(0);
cin >> N;
for(i=1; i<=N; i++)
   {cin >> a >> b;
   if(oblicz(a, b)==true)
      cout << "Case #" << i <<": YES" << endl; 
   else
      cout << "Case #" << i <<": NO" << endl; 
   } 
return 0;   
}
