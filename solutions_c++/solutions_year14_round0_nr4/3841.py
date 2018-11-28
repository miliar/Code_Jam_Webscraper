#include<iostream>
#include<conio.h>
#include<fstream>
#include<algorithm>
 
using namespace std;

int main()
{
	ifstream fin("D-large.in");
	ofstream fout("jitu4.txt");
float temp_naomi[1000],naomi[1000],ken[1000];
float temp;
int t;
int i;
int j;
int count=0,m=0,n;
int a[100];
fin>>t;
while(t--)
{
fin>>n;

for(i=0;i<n;i++)
fin>>naomi[i];
if(n>1)
sort(naomi,naomi+n);
for(i=0;i<n;i++)
temp_naomi[i]=naomi[i];

for(i=0;i<n;i++)
fin>>ken[i];
if(n>1)
sort(ken,ken+n);

for(i=0;i<n;i++)
for(j=0;j<n;j++)
if(ken[i]<naomi[j])
{
count++;
naomi[j]=0;
break;
}
a[m]=count;
m++;
count=0;

for(i=0;i<n;i++)
for(j=0;j<n;j++)
if(temp_naomi[i]<ken[j])
{
count++;
ken[j]=0;
break;
}
a[m]=n-count;
m++;
count=0;


}
j=1;
for(i=0;i<m;i=i+2)
{
fout<<"Case #"<<j<<": ";
fout<<a[i]<<" "<<a[i+1]<<"\n";
j++;
}

return 0;
}
