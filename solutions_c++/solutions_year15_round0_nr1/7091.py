#include <stdio.h>
#include <iostream>

using namespace std;
int main()
{
  int n,k,vet[10000];
  char word[10000];

  cin >> n;

  for(int i=0;i<n;i++)
  {
     cin >> k;
     cout << "Case #" <<i+1 <<": ";
     getchar();
     for(int j=0;j<=k;j++)
     {
        char c=getchar();
        vet[j] = c-'0';
     }

     int x,cont,aux;
    x=cont=aux=0;
     cont = vet[0];
    // cout << "cont = " << cont << "\n";
     for(int i=1;i<=k;i++){
        //cout << i << " < " << cont<< " vet[i] " << vet[i] <<"\n";
   	if(i > cont && vet[i]>0) {x = i-cont ; aux+=x;}// cout << "if = " << i << " - " <<cont<< " = " <<i-cont << "\t";}
        cont += x+vet[i];
        x=0;

     }

    cout  <<aux <<  "\n" ;
   // cout << "\n*******\n\n\n";

  }
  return 0;
}
