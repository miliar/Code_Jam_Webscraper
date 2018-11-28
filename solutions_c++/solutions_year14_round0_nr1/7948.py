#include<iostream>
#include<fstream>
using namespace std;
ifstream fin;
ofstream fout;
class magic
{
	 int arrange1[4][4],arrange2[4][4],row1,row2;
  public:
	 void getdata();
	 void calc(int);
};
void magic::getdata()
{
  fin>>row1;
  for(int j=0;j<4;j++)
  {
    for(int k=0;k<4;k++)
    {
      fin>>arrange1[j][k];
    }
  }
  fin>>row2;
  for(int j=0;j<4;j++)
  {
    for(int k=0;k<4;k++)
    {
      fin>>arrange2[j][k];
    }
  }
}
void magic::calc(int i)
{
  int count=0,guess=0;
  for(int j=0;j<4;j++)
  {
    for(int k=0;k<4;k++)
    {
      if(arrange1[row1-1][j]==arrange2[row2-1][k])
      {
	guess=arrange1[row1-1][j];
	count+=1;
      }
    }
  }
  fout<<endl<<"Case #"<<i+1<<": ";
  if(count==0)
    fout<<"Volunteer cheated!";
  else if(count==1)
    fout<<guess;
  else
    fout<<"Bad magician!";
}
int main()
{
  int n;
  magic m[100];
  fin.open("A-small-attempt1.in");
  fin>>n;
  for(int i=0;i<n;i++)
  {
    m[i].getdata();
  }
  fin.close();
  fout.open("A-smallo.in");
  for(int
      i=0;i<n;i++)
  {
    m[i].calc(i);
  }
  return(1);
}
