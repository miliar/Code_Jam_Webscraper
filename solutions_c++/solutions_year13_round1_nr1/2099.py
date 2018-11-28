#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<fstream>
//#define pi 3.14159
using namespace std;

const long double pi = 2.0*acos(0.0);

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("inp.txt");
    fout.open("oup.txt");
int t,j;
long long c,r,b,d;
fin>>t;
for(int i=1;i<=t;i++) {
fin>>r>>b;
c=0;
d=0;
for(j=0;j<b;j=j+2)
{
c=c+(((r+j+1)*(r+j+1)-(r+j)*(r+j)));
if(c>b)
break;
else
d++;
}
fout<<"Case #"<<i<<":"<<" "<<d<<"\n";
//t--;
}
return 0;
}
