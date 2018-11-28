#include <cmath>
#include <list>
#include <map>
#include <set>
#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

unsigned long long int arr[100][2];

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


int main()
{
unsigned long long int test;
ifstream myfile;
myfile.open("C-small-attempt0.in");
myfile >> test;
cout<<test;
unsigned long long int i=0,j=0,t,n=0,flag[100]={0};
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
return 0;
//getch();
}

