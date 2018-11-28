#include<iostream>
#include<fstream>
#include<string>

using namespace std;
int N, i, l, temp, signChange;
string panc;

int main()
{
ifstream fin;
ofstream fout;
fin.open("test.txt");
fout.open("output.txt");
fin>>N;
temp = 0;
getline(fin, panc);

while(temp<N)
{
getline(fin, panc);

l = panc.length();
signChange = 0;

if(l>1)
{
for(i=0; i<l-1; i++)
{
if(panc[i]!=panc[i+1])
  signChange++;
}
}

if(panc[l-1]=='-')
{
signChange++;
}

fout<<"Case #"<<temp+1<<": "<<signChange<<"\n";
temp++;
 }

fin.close();
fout.close();
return 0;
}
