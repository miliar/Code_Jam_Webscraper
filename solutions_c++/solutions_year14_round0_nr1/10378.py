#include <iostream>
using namespace std;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
int t;
cin>>t;
for(int testcase=1;testcase<=t;testcase++)
{
  int row1;
  
  cin>>row1;
  row1=row1-1;
  int a[4][4],b[4][4];
  //int nouseinput;
  for(int i=0;i<4;i++)
  for(int j=0;j<4;j++)
  cin>>a[i][j];   
  //cin>>nouseinput;
 
  int row2;
  cin>>row2;
  row2=row2-1;
  //int nouseinput;
  for(int i=0;i<4;i++)
  for(int j=0;j<4;j++)
  cin>>b[i][j]; 
  
  int count=0,firstmatch=-1;
  for(int i=0;i<4;i++)
  {
          for(int j=0;j<4;j++)
  { //cout<<a[row1][i]<<" "<<b[row2][j]<<"\n";
     if(a[row1][i]==b[row2][j])
     { if(count==0)
        firstmatch=a[row1][i];
                               count++;   
     }
  }
}
  if(count==0)
  cout<<"Case #"<<testcase<<": Volunteer cheated!\n";
  else if(count==1)
  cout<<"Case #"<<testcase<<": "<<firstmatch<<"\n";
  else
  cout<<"Case #"<<testcase<<": Bad magician!\n";
}

getchar();
return(0);
} 


