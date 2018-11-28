#include<iostream>
#include<fstream>
#include<iomanip>
#include<algorithm>
using namespace std;
int main()
{
  int arr[]={1,4,9,121,484};

  ifstream infile;
  ofstream outfile;


  infile.open("C-small-attempt4.in");
  outfile.open("output.out");

  int n;
  int a;
  int b;
  int i,j,nn;
  int cnt=0;
  infile>>n;
  for(nn=0;nn<n;nn++)
  {
      infile>>a>>b;

      for(j=a;j<=b;j++)
      {
          for(i=0;i<5;i++)
          {
              if(arr[i]==j)
                cnt++;

          }

          }

 outfile<<"Case #"<<nn+1<<":"<<" "<<cnt<<endl;
          cnt=0;


      }

  }


