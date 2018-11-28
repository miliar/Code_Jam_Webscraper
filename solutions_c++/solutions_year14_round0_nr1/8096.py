//#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
ifstream cin("A-small-attempt0.in");
ofstream cout("A-small-attempt0.out");
int a[4][4];
int b[4][4];
int main()
{
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++)
    {
            vector<int> v;
          int x1,x2;
          cin>>x1;
          for(int i=0;i<4;i++)
          for(int j=0;j<4;j++)
          cin>>a[i][j];
          cin>>x2;
          for(int i=0;i<4;i++)
          for(int j=0;j<4;j++)
          cin>>b[i][j];
          x1--;
          x2--;
          for(int i=1;i<17;i++)
          {
                  bool c=false;
                  for(int j=0;j<4;j++)
                  if(a[x1][j]==i)
                  c=true;
                  for(int j=0;j<4;j++)
                  if(b[x2][j]==i&&c)
                  v.push_back(i);
          }  
          cout<<"Case #"<<ii+1<<": ";
          if(v.size()==1)
          cout<<v[0]<<endl;
          if(v.size()==0)
          cout<<"Volunteer cheated!"<<endl;
          if(v.size()>1)
          cout<<"Bad magician!"<<endl;
    }
    //system("pause");
}
