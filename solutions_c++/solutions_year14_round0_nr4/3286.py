using namespace std;
#include<iostream>
#include<stdio.h>

double A[1001];
double B[1001];
int n;

void sort(double A[])
{
  int i,j;
  for(i=1; i<n; i++)
  {
    double key=A[i];
    for(j=i-1; j>=0 && A[j]>key; j--)
      A[j+1]=A[j];

    A[j+1]=key;
  }
}

int main()
{
freopen ("D-large.in","r",stdin);
freopen ("D-large.out","w",stdout);

long t;
cin>>t;
for(long k=1;k<=t;k++)
{
  cin >>n;
  for(int i=0;i<n;i++)
    cin >>A[i];
  for(int i=0; i<n;i++)
    cin >>B[i];

  sort(A);  sort(B);

  int l1,l2;
  int r1,r2;
  int dec,war;
  dec=war=0;

  l1=l2=0; r1=r2=n-1;
  while(r1>=l1)
  {
    if(A[l1]<B[l2])
    {   l1++;r2--;}
    else 
    { dec++;l1++;l2++;}
  }

  
  l1=l2=0; r1=r2=n-1;
  while(r1>=l1)
  {
    if(A[r1]>B[r2])
    { war++;r1--;}
    else
    { r1--;  r2--;}
  }

  printf("Case #%d: %d %d\n",k,dec,war);

}
}

