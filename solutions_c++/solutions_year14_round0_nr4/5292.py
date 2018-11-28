#include<iostream>
using namespace std;

void asort(double *a,int n)
{
 double temp=0;
 for(int i=0;i<n;i++)
 for(int j=i+1;j<n;j++)
 if(a[i]>=a[j])
 {
  temp=a[i];
  a[i]=a[j];
  a[j]=temp;
 }
}

void dsort(double *a,int n)
{
 double temp=0;
 for(int i=0;i<n;i++)
 for(int j=i+1;j<n;j++)
 if(a[i]<=a[j])
 {
  temp=a[i];
  a[i]=a[j];
  a[j]=temp;
 }
}


void adjust(double *a,int pos,int n)
{
 for(int i=pos;i<n-1;i++)
 a[i]=a[i+1];
}

int main()
{
 int t,n,n1,n2,l=1;
 double naomi[1001],ken[1001],point1=0,point2=0,naomi1[1001],ken1[1001];
 cin>>t;
 while(t--)
 {
  cin>>n;
  n1=n2=n;
  point1=point2=0;
  
  for(int i=0;i<n;i++)
  {cin>>naomi[i];naomi1[i]=naomi[i];}
  
  for(int i=0;i<n;i++)
  {cin>>ken[i];ken1[i]=ken[i];}
  
  asort(naomi,n);
  asort(ken,n);
  dsort(naomi1,n);
  dsort(ken1,n);
  
  
  
  
  
  
  for(int i=0;i<n1;i++)
  {
   int flag=0,temp=0;
   for(int j=0;j<n2;j++)
   {
    if(naomi[j]>ken1[i])
    {
     flag=1;
     point1++;
     temp=j;
     break;
    }
   }
   
   if(flag==1)
   {adjust(naomi,temp,n2);n2--;}
   
   else{adjust(naomi,0,n2);n2--;}
  }
  
  n1=n2=n;
  
  for(int i=0;i<n1;i++)
  {
   int flag=0,temp=0;
   
   for(int j=0;j<n2;j++)
   {
    if(ken[j]>naomi1[i])
    {
     flag=1;
     point2++;
     temp=j;
     break;
    }
   }
   
   if(flag==1)
   {adjust(ken,temp,n2);n2--;}
   
   else {adjust(ken,0,n2);n2--;}
  }
  
  cout<<"Case #"<<l<<": "<<point1<<" "<<n-point2<<"\n";
  l++;
 }
}
