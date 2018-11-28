#include<conio.h>
#include<fstream.h>
int a[100][100];
int b[100][100];
void lawnmover(int &res,int r,int c)
{
 for(int u=0;u<100;u++)
 {
  for(int v=0;v<100;v++)
   b[u][v]=0;
 }
 int x=0,y=0;
 res=1;
 for(int i=0;i<r;i++)
 {
  for(int j=0;j<c;j++)
  {
   x=0,y=0;
   {
    for(int k=0;k<r;k++)
    {
     if(a[k][j]>a[i][j])
      x=1;
    }
    if(x==0)
    {
     for(k=0;k<r;k++)
     {
      if(b[k][j]==0||b[k][j]>a[i][j])
       b[k][j]=a[i][j];
     }
    }
    for(k=0;k<c;k++)
    {
     if(a[i][k]>a[i][j])
      y=1;
    }
    if(y==0)
    {
     for(k=0;k<c;k++)
     {
      if(b[i][k]==0 || b[i][k]>a[i][j])
       b[i][k]=a[i][j];
     }
    }
    else if(x==1 && y==1)
    {
     res=2;
     goto ab;
    }
   }
  }
 }
 for(i=0;i<r;i++)
 {
  for(int j=0;j<c;j++)
  {
   if(b[i][j]!=a[i][j])
   {
    res=2;
    goto ab;
   }
  }
 }
 ab:
}

void main()
{
 clrscr();
 ifstream Ifile("BLARGE.IN",ios::in);
 ofstream Ofile("RESULT2L.TXT",ios::out);
 int T,M,N,l=0,i=0,j=0;
 Ifile>>T;
 cout<<T;
 int *result;
 result=new int[T];
 while(Ifile)
 {
  if(i==0 && j==0)
   Ifile>>N>>M;
  Ifile>>a[i][j];
  if(i==(N-1) && j==(M-1))
  {
   lawnmover(result[l],N,M);
   i=0;
   j=-1;
   l+=1;
  }
  j+=1;
  if(j==M)
  {
   i+=1;
   j=0;
  }
 }
 Ifile.close();
 for(i=0;i<T;i++)
 {
  Ofile<<"\nCase #"<<i+1<<": ";
  cout<<"\nCase #"<<i+1<<": ";
  if(result[i]==1)
  {
   Ofile<<"YES";
   cout<<"YES";
  }
  else if(result[i]==2)
  {
   Ofile<<"NO";
   cout<<"NO";
  }
 }
 Ofile.close();
 delete [] result;
}