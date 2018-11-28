#include<iostream>
#include<fstream>
using namespace std;

int T,cards1[4][4],cards2[4][4];
int main()
{
freopen("A-small-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
cin>>T;
for(int k=0;k<T;k++)
{
  int row1,row2,count=0,output=-1;
  cin>>row1;row1--;
  for(int p=0;p<4;p++)
    for(int q=0;q<4;q++)
      cin>>cards1[p][q];
  cin>>row2;row2--;
  for(int p=0;p<4;p++)
    for(int q=0;q<4;q++)
      cin>>cards2[p][q];
  
  for(int i=0;i<4;i++)
   for(int j=0;j<4;j++)
    if(cards1[row1][i]==cards2[row2][j])
      {output=cards1[row1][i];count++;} 
      
  if(count==1) cout<<"Case #"<<k+1<<": "<<output<<endl;
  if(count>1) cout<<"Case #"<<k+1<<": Bad magician!"<<endl;
  if(output==-1) cout<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;
}
return 0;    
}
