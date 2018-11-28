using namespace std;
#include<iostream>
#include<stdio.h>
long A[4][4];
long B[4][4];

int a,b;

int main()
{
freopen ("input.txt","r",stdin);
freopen ("output.txt","w",stdout);

long t;
cin>>t;
for(long k=1;k<=t;k++)
{
  cin >>a;a--;
  for(int i=0;i<4;i++)
   for(int j=0; j<4;j++)
    cin >>A[i][j];

  cin >>b;b--;
  for(int i=0;i<4;i++)
   for(int j=0; j<4;j++)
    cin >>B[i][j];

  int H[17]={0};
  int equals=0;
  int eql;


  for(int i=0;i<4;i++)
  {  H[A[a][i]]++;    H[B[b][i]]++; }

  for(int i=1;i<=16;i++)
    if(H[i]>1)
    {  equals++; eql=i;}


  if(equals==0)
    cout <<"Case #"<<k<<": Volunteer cheated!"<<endl;
  else if(equals==1)
    cout <<"Case #"<<k<<": "<<eql<<endl;
  else
    cout <<"Case #"<<k<<": Bad magician!"<<endl;

}
}

