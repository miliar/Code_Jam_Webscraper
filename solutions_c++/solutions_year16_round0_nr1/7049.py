#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;

bool n[10];

void setfalse(){
    for(int i=0;i<10;i++)
    {
       n[i]=false;
    }
}
bool allset()
{   int m=0;
    for(int i=0;i<10;i++)
    {
        if(n[i]==true){
        m++;
        }
    }

    if(m==10){
        return true;

    }
}

void add(int num)
{   int ld;  //last digit
    while(num!=0){
        ld =num%10;
        num = num/10;
    if(n[ld]==false){
        n[ld]=true;
    }}}



int csheep(int N){
    setfalse();
    int M;
    int i=1;
    while(!allset())
    {
        M=N*i;
        i++;
        add(M);
    }
    return M;
}

int main(){
    int TC; //Number of input or T.T
    int N;

ifstream istr("A-large.in");
ofstream ostr("A-large.out");

istr>>TC;

for(int i=1;i<=TC;i++)
{
    istr>>N;
    if(N!=0){
    ostr<<"Case #"<<i<<": "<<csheep(N)<<endl;
    }
    else
    {
        ostr<<"Case #"<<i<<": INSOMNIA"<<endl;
    }


}

system("pause");
return 0;
}
