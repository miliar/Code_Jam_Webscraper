#include<fstream>
#include<iostream>
using namespace std;
int main()
{
ifstream fin;
fin.open("input.in",ios::in);
ofstream fout("output",ios::out);
int T;
int br;
float r,t;
fin>>T;
cout<<"The value of T is "<<T;
float tempr;
for(int d=0;d<T;d++)
{
 br=0;
 fin>>r>>t;
 tempr=r;
 do
 {
 t=t-( ( (tempr+1)*(tempr+1) ) - ( (tempr)*(tempr) ) );
 br++;
 tempr+=2;
 }while(t>=0);
 br-=1;
 fout<<"Case #"<<d+1<<": "<<br<<"\n";
}

return 0;
}
