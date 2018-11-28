#include<iostream>
using namespace std;
int main()
{ 
  int T,N;
  float a[100],b[100],a2[100],b2[100],tmp;
  int z,i,j,k,war,nwar,flag;

  cin>>T;
  for(z=0;z<T;z++)
  {
     cin>>N;
     for(i=0;i<N;i++)
     cin>>a[i];
     for(i=0;i<N;i++)
     cin>>b[i];
     war=0; nwar=0;
     tmp=a[0];
     for(j=0;j<N;j++)
     for(i=0;i<N-1;i++)
     if(a[i]>a[i+1])
     {
       tmp=a[i];
       a[i]=a[i+1];
       a[i+1]=tmp;
     }
     tmp=b[0];
     for(j=0;j<N;j++)
     for(i=0;i<N-1;i++)
     if(b[i]>b[i+1])
     {
       tmp=b[i];
       b[i]=b[i+1];
       b[i+1]=tmp;
     }
     for(i=0;i<N;i++)
     {
      a2[i]=a[i];
      b2[i]=b[i];
     }

   for(i=0;i<N;i++)
   { flag=2;
    for(j=0;j<N;j++)
     if(b2[j]>a2[i])
     {
	b2[j]=0;
	a2[i]=0;
	flag=1;
	break;
     }
     else
     flag=0;
    if(flag==0)
    for(j=0;j<N;j++)
    {
      if(b2[j]!=0)
      {
	b2[j]=0;
	a2[i]=0;
	war+=1;
	break;
      }
    }
   }

   for(i=0;i<N;i++)
   {  flag=2;
      for(j=0;j<N;j++)
	if(b[i]<a[j])
	{
	  a[j]=0;
	  b[i]=0;
	  flag=1;
	  nwar+=1;
	  break;
	}
	else
	flag=0;
	if(flag==0)
	for(j=0;j<N;j++)
	if(a[j]!=0&&b[i]>a[j])
	{
	  b[i]=0;
	  a[j]=0;
	  break;
	}
   }

   /*
  cout<<"\n";
  for(i=0;i<N;i++)
  cout<<a[i]<<"  ";  cout<<"\n";
  for(i=0;i<N;i++)
  cout<<b[i]<<"  ";
  cout<<"\n\n";
  for(i=0;i<N;i++)
  cout<<a2[i]<<"  ";  cout<<"\n";
  for(i=0;i<N;i++)
  cout<<b2[i]<<"  ";   */
  cout<<"Case #"<<z+1<<": "<<nwar<<" "<<war<<"\n";
  }
}

