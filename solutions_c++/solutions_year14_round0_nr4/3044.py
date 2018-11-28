//in the name of GOD
#include<fstream.h>
#include<stdio.h>
#include<stdlib.h>
void bubsort(double *a,double n);
void rbubsort(double *a,double n);
void main()
{
double cases,n,naomi[2000],ken[2000],done=0,i,j,war,dwar;
fstream ifile("d1l.in",ios::in);
fstream ofile("d1l.out",ios::out);

ifile>>cases;
while(done<cases)
{
 ifile>>n;
 for(i=0;i<n;i++)
 {
 ifile>>naomi[i];
 }
 for(i=0;i<n;i++)
 {
 ifile>>ken[i];
 }
 bubsort(naomi,n);
 bubsort(ken,n);


 {
  i=0;
  war=0;
  for(j=0;j<n;)
  {
  if(ken[j]>naomi[i])
  {
  war=war+1;
  i++;
  j++;
  }
  else
  {
  j++;
  }
  }
  war=n-war;

 }

 {
 rbubsort(ken,n);
 rbubsort(naomi,n);
 i=0;
 dwar=0;
 for(j=0;j<n;)
 {
 if(naomi[i]>ken[j])
 {
 i++;
 j++;
 dwar=dwar+1;
 }
 else
 {
 j++;
 }
 }

 }

 done++;
 ofile<<"Case #"<<done<<": "<<dwar<<" "<<war<<"\n";
}
}

void bubsort(double *a,double n)
{
double temp,i,j;
for(i=0;i<n;i++)
{
for(j=0;j<n-i-1;j++)
{
if(a[j]>a[j+1])
{
temp=a[j];
a[j]=a[j+1];
a[j+1]=temp;
}
}
}
}
void rbubsort(double *a,double n)
{
double temp,i,j;
for(i=0;i<n;i++)
{
for(j=0;j<n-i-1;j++)
{
if(a[j]<a[j+1])
{
temp=a[j];
a[j]=a[j+1];
a[j+1]=temp;
}
}
}
}