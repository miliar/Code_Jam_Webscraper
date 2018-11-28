#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
int main()
{

 ofstream fout ("test.out");
 ifstream fin ("A-small-attempt0.in");
 int t;fin>>t;
 for (int ii=0;ii<t;ii++){
 //int cas=0;
 int a1,a2;
 int grid1[4][4];
 int grid2[4][4];
 fin>>a1;
 for  (int i=0;i<4;i++)
  for (int j=0;j<4;j++)
    fin>>grid1[i][j];

 fin>>a2;
 for  (int i=0;i<4;i++)
  for (int j=0;j<4;j++)
    fin>>grid2[i][j];


 int ctr=0,val;
 for (int i=0;i<4;i++){

  for (int j=0;j<4;j++){
    if (grid1[a1-1][i]==grid2[a2-1][j]){
      ++ctr;
      val=grid1[a1-1][i];
       }
   }

 }



 //++cas;

   if (ctr==0)
     fout<<"Case #"<<ii+1<<": "<<"Volunteer cheated!"<<"\n";
   else{
   if (ctr==1)
    fout<<"Case #"<<ii+1<<": "<<val<<"\n";
   else
    fout<<"Case #"<<ii+1<<": "<<"Bad magician!"<<"\n";
   }

 }



 return 0;
}
