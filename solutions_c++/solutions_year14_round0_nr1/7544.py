#include <iostream>

using namespace std;

int scan(int f[4],int s[4])
{
 int r1=0,r;
 for(int i=0;i<4;i++)
 {
  r=f[i];
  for(int j=0;j<4;j++)
  {
   if(r==s[j] && r1==0)
   {
    r1=r;
   }
   else if(r==s[j] && r1!=0)
   {
    return 17;
   }
  }
 }
 return r1;
}
int main()
{
 int t,a,b,f[4][4],s[4][4],r;
 cin>>t;
 for(int n=1;n<=t;n++)
 {
  cin>>a;
  for(int i=0;i<4;i++)
  {
   for(int j=0;j<4;j++)
   {
    cin>>f[i][j];
   }
  }
  cin>>b;
  for(int i=0;i<4;i++)
  {
   for(int j=0;j<4;j++)
   {
    cin>>s[i][j];
   }
  }
  r=scan(f[a-1],s[b-1]);
  if(r==0)
   cout<<"Case #"<<n<<": Volunteer cheated!\n";
  else if(r==17)
   cout<<"Case #"<<n<<": Bad magician!\n";
  else
   cout<<"Case #"<<n<<": "<<r<<"\n";
 }
 return 0;
}
