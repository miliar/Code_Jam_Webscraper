#include<iostream>
#include <fstream>

using namespace std;

int main()
{
ifstream in ("../Downloads/B-large.in");
ofstream myOutputFile;
myOutputFile.open ("bo.txt");

int c;
in>>c;

for(int k=1;k<=c;k++)
{
int m,n;
in>>m>>n;

int a[m+1][n+1];

for(int i=0;i<m;i++)
{
a[i][n]=0;
for(int j=0;j<n;j++)
  {
  in>>a[i][j];
  
  if(a[i][n]<a[i][j])
    a[i][n]=a[i][j];
  }
}

for(int j=0;j<n;j++)
{
a[m][j]=0;
for(int i=0;i<m;i++)
  if(a[i][j]>a[m][j])
    a[m][j]=a[i][j];
}

int ans=1;
bool out = false;
for(int i=0;i<=m&&!out;i++)
for(int j=0;j<=n&&!out;j++)
  if(a[i][j]<a[i][n] && a[i][j]<a[m][j])
   {  
   ans=0;
   out=true;
   break;
   }


if(ans==1)
  myOutputFile<<"Case #"<<k<<": YES"<<endl;
else  
  myOutputFile<<"Case #"<<k<<": NO"<<endl;
  
}  
}