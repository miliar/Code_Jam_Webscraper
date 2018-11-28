#include<algorithm>
#include<string>
#include<iostream>
#include<cstdlib>
#include<vector>
#include <list>
#include <iterator>
using namespace std;

int main()
{
int T,i=1;
cin>>T;
while(T--)
{
  int N,y=0,z=0;
  cin>>N;
  vector<double> Na(N),K(N);
  for( int i=0;i<N;i++)cin>>Na[i]; 
  for( int i=0;i<N;i++)cin>>K[i];
  sort(Na.begin(),Na.end());sort(K.begin(),K.end());
 // for( int i=0;i<N;i++)cout<<"("<<Na[i]<<","<<K[i]<<") ";
 // cout<<"\n";
  int k,n;k=n=N-1;
  while(k>=0 && n>=0)
    {
      if(Na[n]>K[k])
        {
          z++;n--;
        }
      else 
       {
         n--;k--;
       }
    } 
   k=n=0;
   while(k<N && n<N)
    {
     if(Na[n]>K[k])
      {
        y++;k++;n++;
      }else {n++;}
     }
  cout<<"Case #"<<(i++)<<": "<<y<<' '<<z<<'\n';  
}
return 0;
}
