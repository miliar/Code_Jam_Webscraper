#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
int main()
{
    long long n,i,t,j,k=0;
    ofstream fout ("A-large (1).out");
    ifstream fin ("A-large (1).in");
fin>>t;
while(t>0)
{
          ++k;
          fout<<"Case #"<<k<<": ";
char s[2500];
long long ar[26]={0},a[10]={0};
fin>>s;
n=strlen(s);
for(i=0;i<n;++i)
++ar[s[i]-65];
a[0]=ar[25];
ar[4]=ar[4]-ar[25];
ar[17]=ar[17]-ar[25];
ar[14]=ar[14]-ar[25];
a[2]=ar[22];
ar[19]=ar[19]-ar[22];
ar[14]=ar[14]-ar[22];
a[4]=ar[20];
ar[5]=ar[5]-ar[20];
ar[14]=ar[14]-ar[20];
ar[17]=ar[17]-ar[20];
a[6]=ar[23];
ar[18]=ar[18]-ar[23];
ar[8]=ar[8]-ar[23];
a[8]=ar[6];
ar[4]=ar[4]-ar[6];
ar[8]=ar[8]-ar[6];
ar[7]=ar[7]-ar[6];
ar[19]=ar[19]-ar[6];
a[3]=ar[17];
ar[19]=ar[19]-ar[17];
ar[7]=ar[7]-ar[17];
ar[4]=ar[4]-2*ar[17];
a[5]=ar[5];
ar[8]=ar[8]-ar[5];
ar[21]=ar[21]-ar[5];
ar[4]=ar[4]-ar[5];
a[7]=ar[21];
ar[18]=ar[18]-ar[21];
ar[4]=ar[4]-2*ar[21];
ar[13]=ar[13]-ar[21];
a[1]=ar[14];
ar[13]=ar[13]-ar[14];
a[9]=ar[13]/2;
for(i=0;i<10;++i)
for(j=0;j<a[i];++j)
fout<<i;
fout<<endl;
--t;
}
return 0;
}
