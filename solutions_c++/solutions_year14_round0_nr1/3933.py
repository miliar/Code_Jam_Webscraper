#include<stdio.h>
#include<fstream>
using namespace std;
int a[4][4],b[4][4],r1,r2;
int dowork()
{
int i,j,ct=0,p;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
if(a[r1-1][i]==b[r2-1][j])
{
ct++;
p=a[r1-1][i];
}

if(ct==0)
return 0;
if(ct==1)
return p;
if(ct>1)
return -1;
}


int main()
{
    fstream A("input.in",ios::in);
    fstream B("output.in",ios::out);
int t,i=1,j,k,y;
A>>t;
while(i<=t)
{
A>>r1;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
A>>a[j][k];
A>>r2;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
A>>b[j][k];

B<<"Case #"<<i<<": ";
i++;
y=dowork();
if(y==-1)
B<<"Bad magician!\n";
else if(y==0)
B<<"Volunteer cheated!\n";
else
B<<y<<endl;
}
A.close();
B.close();
return 0;
}
