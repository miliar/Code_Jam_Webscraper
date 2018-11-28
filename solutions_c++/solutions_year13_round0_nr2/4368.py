#include<iostream>
#include<cstring>
using namespace std;
class S
{
  public:
  int data[100][100];
  int m,n;
  void getin()
  {
    cin>>m>>n;
     for(int i=0;i<m;i++)
      for(int j=0;j<n;j++)
        cin>>data[i][j];
  }
  bool juge()
  {
    bool f[100][100];
    
    for(int i=0;i<m;i++)
      for(int j=0;j<n;j++)
        f[i][j]=false;
    for(int i=0;i<m;i++)
     {
       int maxh=0;
       for(int j=0;j<n;j++)
         maxh=data[i][j]>maxh ? data[i][j]:maxh;
       for(int j=0;j<n;j++)
         if(data[i][j]==maxh)
           f[i][j]=true;
      }
       for(int j=0;j<n;j++)
     {
       int maxh=0;
       for(int i=0;i<m;i++)
         maxh=data[i][j]>maxh ? data[i][j]:maxh;
       for(int i=0;i<m;i++)
         if(data[i][j]==maxh)
           f[i][j]=true;
      }
       for(int i=0;i<m;i++)
         for(int j=0;j<n;j++)
           if(!f[i][j])
             return false;
       return true;
  }
};



int main()
{
  int t;
  S s;
 //freopen("in.txt","r",stdin);
  //freopen("b.out","w",stdout);
  cin>>t;
  for(int k=1;k<=t;k++)
  {
  s.getin();
  if(s.juge())
    cout<<"Case #"<<k<<": YES\n";
  else
     cout<<"Case #"<<k<<": NO\n";
  }
  return 0;
}
