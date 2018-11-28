#include <vector.h>
#include <list.h>
#include <map.h>
#include <set.h>
#include <iostream.h>
#include <iomanip.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <fstream.h>
#include <conio.h>

int arr[100][2]={0};

int palin(float n)
{
int res,i=0,t;
t=n;
while(t>0)
  {
  i*=10;
  i+=(t%10);
  t/=10;
  }
if(i==n)
 return 1;
else
 return 0;
}


void main()
{
int test;
ifstream myfile;
myfile.open("example.txt");
myfile >> test;
cout<<test;
int i=0,j=0,t,n=0,flag[100]={0};
float check;
for(i=0;i<test;i++)
  {
    for(j=0;j<2;j++)
      {
      myfile >> arr[i][j];
      }
  }
cout<<"\n";
for(i=0;i<test;i++)
  {
    for(j=0;j<2;j++)
      {
      cout<< arr[i][j]<<" ";
      }
    cout<<"\n";
  }
for(i=0;i<test;i++)
  {
  for(j=arr[i][0];j<=arr[i][1];j++)
    {
     if(palin(j)==1)
       {
       check=sqrt(j);
       if(palin(check)==1)
          flag[i]++;
       }
    }

  }
for(i=0;i<test;i++)
cout<<flag[i]<<" ";
ofstream yourfile("ouptut.txt");
for(i=0;i<test;i++)
 {
 yourfile << "Case #"<<i+1<<": "<<flag[i]<<"\n";
 }
yourfile << endl;
//getch();
}

