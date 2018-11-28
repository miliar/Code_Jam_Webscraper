#include<iostream>
#include<fstream>

using namespace std;

int mat1[4][4],mat2[4][4];
int r1,r2,ch;
int row_check()

{
  int flag=0;
  int ch;
  for(int i=0;i<4;i++)
  {
   for(int j=0;j<4;j++)
   {
    if(mat1[r1-1][i]==mat2[r2-1][j])
    {
     ch=mat1[r1-1][i];
     flag++;
    }
   }
  }

  if(flag==0)
    return 21;
  else
    if(flag==1)
     return ch;
      else
        return 20;

}

int main()
{
 ifstream fin("A-small-attempt1.in");
 ofstream fout("output.txt");
 int n;
 fin>>n;
 for(int i=1;i<=n;i++)
 {
  fin>>r1;
  for(int j=0;j<4;j++)
    for(int k=0;k<4;k++)
      fin>>mat1[j][k];
  fin>>r2;
  for(int j=0;j<4;j++)
    for(int k=0;k<4;k++)
      fin>>mat2[j][k];

  ch=row_check();
  fout<<"Case #"<<i<<": ";
  if(ch==20)
  {
   fout<<"Bad magician!";
  }
  else
    if(ch==21)
  {
   fout<<"Volunteer cheated!";
  }
  else
    fout<<ch;


  fout<<endl;
 }

return 0;
}
