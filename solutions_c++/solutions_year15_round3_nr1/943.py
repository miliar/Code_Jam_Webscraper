#include<conio.h>
#include<iostream>
using namespace std;

int main () {
    int cases,row,col,size, minChances;
    scanf("%d",&cases);
    for(int tCase=1; tCase<=cases; tCase++)
    {
            scanf("%d %d %d",&row,&col,&size);
            minChances=(col==size?row-1+col:col%size==0?(row*(col/size)+(size-1)):(row*(col/size)+size));
            cout<<"Case #"<<tCase<<": "<<minChances<<endl;
    }
    //getch();
    
}
