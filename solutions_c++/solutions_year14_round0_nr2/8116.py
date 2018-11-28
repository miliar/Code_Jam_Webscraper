#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;
int main()
{
ifstream fin("Input.txt");
ofstream fout("Output.txt");
double n,m,c,min,min2,k;
int l=1;
int a;
k=0;
fin>>a;
for (int z=0;z<a;z++)
{
l=1;
fin>>n>>m>>c;
min=c/2;
min2=min;
while (min==min2)
{
min=0;
for (int i=0;i<l;i++)
{
min=min+n/(2+k);
k=k+m;
}
min=min+c/(2+k);
l++;
k=0;
if (min<min2)
min2=min;
}
fout<<"Case #"<<z+1<<": "<<fixed<<setprecision(7)<<min2<<endl;
}
fin.close();
fout.close();
return 0;
}
