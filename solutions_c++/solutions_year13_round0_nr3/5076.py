#include <cstdio>
#include <string>
#include <iostream>
#include <map>
using namespace std;
char str[101];
int  numero;
int A,B;

map<int,int> squared;



bool palindromo (string ca){
    
    int LI=0;
    int LS=ca.size()-1;
    while (LS>=LI){
        
        if (ca[LI]==ca[LS]){
            LI++;
            LS--;
        }else
        return false;
        
    }
    return true;
    
}


bool square (int numero){
    int saving=squared[numero];
    char rockstar [101];
    if (saving!=0  ){
        sprintf(rockstar,"%d",saving);
        return palindromo(rockstar);
    }else
    return false;
    
    
}

int main(){
    int t;
    scanf("%d",&t);
for (int s=0;s<1005;++s){
    squared[s*s]=s;    
}
    for (int o=0;o<t;++o){
    printf("Case #%d: ",o+1);
    
    cin>>A>>B;
int cont=0;
int stroke=A;
    while (stroke<=B){
    numero=stroke;
    sprintf(str,"%d",numero);
    if (square(numero) && palindromo(str)){
    cont++;
    }
      stroke++;
    }
    printf("%d\n",cont);
    
    }
    
    return 0;
    
    
    
}