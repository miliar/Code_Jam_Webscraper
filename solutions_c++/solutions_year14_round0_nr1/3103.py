#include<iostream>
using namespace std;
int main(){
int n,c,i,j,k,a,b,ar[4][4],br[4][4],num;
cin>>n;
for(i=0;i<n;i++)
{
cin>>a;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
cin>>ar[j][k];
cin>>b;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
cin>>br[j][k];
c=0;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
if(ar[a-1][j]==br[b-1][k])
{
c++;
num=ar[a-1][j];
}
if(c==1)
cout<<"Case #"<<i+1<<": "<<num<<endl;
else if(c==0)
cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
else
cout<<"Case #"<<i+1<<": Bad magician!\n";
}
}

