#include <iostream>
#include <string>

using namespace std;

int main()
{
 int t,l,x,fi,fk,f1,p;
 int a[8][8]={{1,2,3,4,5,6,7,8},{2,5,4,7,6,1,8,3},{3,8,5,2,7,4,1,6},{4,3,6,5,8,7,2,1},{5,6,7,8,1,2,3,4},{6,1,8,3,2,5,4,7},{7,4,1,6,3,8,5,2},{8,7,2,1,4,3,6,5}};
 string s;
 cin>>t;
 for(int k=1;k<=t;k++)
 {
  cin>>l>>x;
  cin>>s;
  fi=0;fk=0;f1=0;
  p=1;
  for(int i=0;i<l*x;i++)
  {
   p=a[p-1][s[i%(l)]-'i'+1];
   if(p==2)
    fi=1;
   if(fi==1 && p==4)
    fk=1;
  }
  if(fi==1 && fk==1 && p==5)
  {
   cout<<"Case #"<<k<<": YES\n";
  }
  else
  {
   cout<<"Case #"<<k<<": NO\n";
  }
 }
 return 0;
} 
 
