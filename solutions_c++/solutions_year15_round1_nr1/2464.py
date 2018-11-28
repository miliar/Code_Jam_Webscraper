#include<iostream>
#include<fstream>
#include<cmath>
#define cout fout
#define cin fin
using namespace std;

int main()
{
 int t,n,m1,m2,*m;
 int ans,sec;
 
 ofstream fout("out.out");
 ifstream fin("A-large.in");
 cin>>t;
 
 for(int z=0;z<t;z++)
 {
  cin>>n;
  m=new int[n];
  ans=0;
  sec=0;
  m2=0;
  int best=0;
  for(int i=0;i<n;i++)
  {
   cin>>m1;
   m[i]=m1;
   if(m1<m2)
   {
    sec+=(m2-m1);
	if(best<(m2-m1))
	 best=m2-m1;
   }
   m2=m1;
  }
  for(int i=0;i<n-1;i++)
  {
   ans+=min(m[i],best);
  }
  cout<<"Case #"<<z+1<<": "<<sec<<' '<<ans<<endl;
 }
}


