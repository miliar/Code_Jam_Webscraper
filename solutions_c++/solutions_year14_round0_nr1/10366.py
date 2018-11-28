#include<iostream>
#include<fstream>
using namespace std;

int main()
{
ifstream in;
in.open("A-small-in.txt");
ofstream out;
out.open("A-small-attempt3.out");

int test,cas=1,value;
in>>test;
int arr[4][4];
while(test--)
{
int hash[17]={0};
int count=0;
int choose;

for(int i=1;i<=2;i++)
{
  in>>choose;
  for(int j=0;j<4;j++)
  {
    for(int k=0;k<4;k++)
    {
      in>>arr[i][j];
      
      if(choose == (j+1))
      {
        hash[arr[i][j]]++;
      }
    }
  }

} //two questions asked


for(int i=1;i<=16;i++)
{
  if(hash[i]>=2)
  {
    count++;
    value=i;
  }
}

if(count==1)
{
  out<<"Case #"<<cas++<<": "<<value<<endl;
}
else if(count>1) //more than one common
{
  out<<"Case #"<<cas++<<": "<<"Bad magician!"<<endl;
}
else
  out<<"Case #"<<cas++<<": "<<"Volunteer cheated!"<<endl;
}//end of while test case



return 0;
}
