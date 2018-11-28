#include<iostream>
#include<fstream>
using namespace std;
int main()
{
ifstream fin("C-small-attempt0.in");
ofstream fout("output.txt");
int t,i,a,b,p=0,count;
int ar[]={1,4,9,121,484};
fin>>t;
while(t--)
{
count=0;
fin>>a>>b;
for(i=0;i<5;i++)
if((a<=ar[i])&&(ar[i]<=b))
count++;
p++;
fout<<"Case #"<<p<<": "<<count<<endl;

}
return 0;
}
