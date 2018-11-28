#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;
int tabka[10];
int main()
{
    int T,z=0,c=0,liczba=0,suma=0,temp=0,liczba_pocz,iteratorek=0;
    int wyniki[100];
    char tab[200][100];
    cin>>T;
    if(T<1 || T>100)return 0;
    for(int i=1;i<=T;i++)
    {
        cin>>tab[i-1];
    }
    while(z<T)
    {
        if(iteratorek==0)liczba_pocz=atoi(tab[z]);
        if(liczba_pocz==0){wyniki[z]=0;z++;iteratorek=0;continue;}
        while(tab[z][c]!=NULL){
        if(tab[z][c]=='0'){tabka[0]=1;c++;continue;}
        if(tab[z][c]=='1'){tabka[1]=1;c++;continue;}
        if(tab[z][c]=='2'){tabka[2]=1;c++;continue;}
        if(tab[z][c]=='3'){tabka[3]=1;c++;continue;}
        if(tab[z][c]=='4'){tabka[4]=1;c++;continue;}
        if(tab[z][c]=='5'){tabka[5]=1;c++;continue;}
        if(tab[z][c]=='6'){tabka[6]=1;c++;continue;}
        if(tab[z][c]=='7'){tabka[7]=1;c++;continue;}
        if(tab[z][c]=='8'){tabka[8]=1;c++;continue;}
        if(tab[z][c]=='9'){tabka[9]=1;c++;continue;}
        cout<<"lol:"<<endl;
        }
        liczba=atoi(tab[z]);
        temp=liczba;
        liczba+=liczba_pocz;
        itoa(liczba,tab[z],10);
        iteratorek++;
        c=0;
        suma=0;
        for(int k=0;k<10;k++)
        {
            suma+=tabka[k];
        }
        if(suma==10){wyniki[z]=temp;z++;iteratorek=0;
        for(int k=0;k<10;k++)
        {
            tabka[k]=0;
        }
        continue;}
    }
    for(int m=1;m<=T;m++)
    {
        if(wyniki[m-1]==0){cout<<"Case #"<<m<<": INSOMNIA"<<endl;continue;}
        cout<<"Case #"<<m<<": "<<wyniki[m-1]<<endl;
    }
    return 0;
}
