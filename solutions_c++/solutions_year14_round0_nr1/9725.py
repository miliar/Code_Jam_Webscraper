#include <iostream>
#include<fstream>
using namespace std;

ifstream f("magician.in");
ofstream g("magician.out");

int t,a[6][6],b[6][6];

int main()
{   int i,j,l1,l2,t,k,c,d;
f>>t;
for(k=1;k<=t;++k){
                  f>>l1;
                  for(i=1;i<=4;++i)
                  for(j=1;j<=4;++j)
                  f>>a[i][j];
                  f>>l2;
                  for(i=1;i<=4;++i)
                  for(j=1;j<=4;++j)
                  f>>b[i][j];
                  c=0;
                  for(i=1;i<=4;++i)
                  for(j=1;j<=4;++j)
                  if(a[l1][i]==b[l2][j])
                  {++c; d=a[l1][i];}
                  if(c>1)
                  g<<"Case #"<<k<<": Bad magician!\n";
                  if(c==0)
                  g<<"Case #"<<k<<": Volunteer cheated!\n";
                  if(c==1)
                  g<<"Case #"<<k<<": "<<d<<"\n";
}

    system("pause");
    return 0;
}
