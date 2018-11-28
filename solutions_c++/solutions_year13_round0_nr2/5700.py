#include<iostream>
#include<fstream>
using namespace std;
int a[10][10],m,n;
int check(int i,int j,int num)
{
 int k,flag1=0,flag2=0,flag3=0,flag4=0;
 for(k=0;k<m;k++)
 {
  if(a[i][k]>num)
  {
   flag1=1;break;
  }
 }
 for(i=0;i<n;i++)
 {
  if(a[i][j]>num)
  {
   flag2=1;break;
  }
 } 
  if(flag1==1&&flag2==1)
   return 0;
  else return 1;
}


int main()
{
 int i,j,k,count,flag=0;
 
 cout<<"Enter the input file name : ";
 char file[10];
 cin>>file;
 ifstream infile;
 infile.open(file);
 ofstream ofile;
 ofile.open("lawnoutput.txt");
 infile>>count;
 
  for(i=0;i<count;i++)
  {
   next:if(i>=count)
          break;
   //cout<<"Enter the value of n & m : ";
   infile>>n>>m;
   //cout<<"Enter the matrix design : "<<endl;
   for(j=0;j<n;j++)
    for(k=0;k<m;k++)
     infile>>a[j][k];
   for(j=0;j<n;j++)
   {
    for(k=0;k<m;k++)
    {
     flag=check(j,k,a[j][k]);
     if(flag==0)
     {
      ofile<<"Case #"<<i+1<<": NO"<<endl;
      i++;
      goto next;
     }
    }//end of for of k
   }//end of for of j
   ofile<<"Case #"<<i+1<<": YES"<<endl;
  }//end of for of i
 
}







