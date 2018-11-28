#include <iostream>
#include <fstream>
using namespace std;


int main ()
{
 //ios::sync_with_stdio(false);
 freopen("A-large.in","r",stdin);   
 freopen("A-large.txt","w",stdout);
 
 int T, n;
 bool digits[10];
 
 cin>>T;
 for (int t=1;t<=T;++t)
 {

  cin>>n;

  int upper = n*100;
  for (int j=0;j<10;++j)
      digits[j]=false;
  bool all = false;    
  int i = 0;
  int counter = 0;
  

  
  while((!all) and counter<100)
  {
      i+=n;
      int smaller = i;
      //cout<<i<<" ";
      int num = i;
      while (smaller>0)
      {
       smaller = smaller/10;

       //cout<<smaller<<" "<<num<<"\n";
       digits[num-smaller*10] = true;
       num = smaller;
      }
  
      all = true;
      for (int j=0;j<10;++j)
      {
       if (!digits[j])
          all = false;
      }
      
      counter++;
 }
 if (all)
    cout<<"Case #"<<t<<": "<<i<<"\n";
 else
     cout<<"Case #"<<t<<": INSOMNIA\n";
 }
}
