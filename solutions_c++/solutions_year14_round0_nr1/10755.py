#include<iostream>
#include <fstream>
using namespace std;
int main()
{
    ofstream myfile;
  myfile.open ("first.txt");
    int t,x,y,a[4][4],b[4][4],ans,count,k,i,j;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        count=0;
        cin>>x;
        for(i=0;i<4;i++)
         for(j=0;j<4;j++)
          cin>>a[i][j];
        cin>>y;
        for(i=0;i<4;i++)
         for(j=0;j<4;j++)
          cin>>b[i][j];
        for(i=0;i<4;i++)
         for(j=0;j<4;j++)
          if(a[x-1][i]==b[y-1][j])
          {
              count++;
              ans=a[x-1][i];
          }
        if(count==1)
        myfile<<"Case #"<<k<<":"<<ans<<endl;
        else
         if(count==0)
          myfile<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        else
         myfile<<"Case #"<<k<<": Bad magician!"<<endl;
    }
    myfile.close();
    return 0;
}
