#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int power(int p)
{
 if(p==1)
 {return 1;}
 int res=10;
 for(int i=1;i<p-1;i++)
 {
   res *= 10;
 }
 return res;  
}

int sum(int array[10])
{
 int suma=0;
 for(int i=0;i<10;i++)
 {
   suma+=array[i];
 }
 return suma;
}

int main(int argc, char** argv)
{

int T=0,p=0,d=0;
long long N=0,aux=0;
int decimals[10]={0,0,0,0,0,0,0,0,0,0};
ifstream file;
ofstream results;
file.open("A-large.in",ios::in);
results.open("A-large.out",ios::out);

file>>T;

for(int i=0;i<T;i++)
{

file>>N;

for(int j=1;j<10000000;j++)
{
 aux=N*j;
 int digits = floor(log10((double)aux))+1;
 
 for(int k=digits;k>0;k--)
 {
   p=power(k);
   d = aux/p;
   decimals[d]=d+1;
   aux=aux-d*p;

 }
 //decimals[aux]=aux+1;
 
 if(sum(decimals)==55)
 {
   results<<"Case"<<" #"<<i+1<<": "<<N*j<<endl;
   break;
 }  
}
 if(sum(decimals)!=55)
 {
 results<<"Case"<<" #"<<i+1<<": INSOMNIA"<<endl;
 }
 for(int l=0;l<10;l++)
 {decimals[l]=0;}
}

return 0;

}
