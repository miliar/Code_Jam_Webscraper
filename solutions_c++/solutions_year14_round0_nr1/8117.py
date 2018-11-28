#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("Input.txt");
    ofstream fout ("Output.txt");
int a,b,c[4][4],d[4][4],kol,element,n;
kol=0;
element=0;
fin>>n;
for (int l=0;l<n;l++)
{
fin>>a;
for (int i=0;i<4;i++)
for (int j=0;j<4;j++)
fin>>c[i][j];
fin>>b;
for (int i=0;i<4;i++)
for (int j=0;j<4;j++)
fin>>d[i][j];
for (int i=0;i<4;i++)
{
for (int j=0;j<4;j++)
 if (c[a-1][i]==d[b-1][j])
{
kol++;
element=c[a-1][i];
}
}
if (kol>=2)
fout<<"Case #"<<l+1<<": Bad magician!"<<endl;
if (kol==1)
fout<<"Case #"<<l+1<<": "<<element<<endl;
if (kol==0)
fout<<"Case #"<<l+1<<": Volunteer cheated!"<<endl;
kol=0;
}
fin.close();
fout.close();
return 0;
}
