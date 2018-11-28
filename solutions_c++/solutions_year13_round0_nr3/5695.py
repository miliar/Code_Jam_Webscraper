#include <iostream>
#include <fstream>
#include <stdlib.h>   
#include <math.h>
using namespace std;
long long int rev(long long int num)
{
        long long int i; 
        i = 0;
        while (num>0)
        {
                i = i * 10 + (num%10);
                num = num / 10;
        }
        return i;
}
int main ()
{
  long long int a,b,tc,sa,sb,i,j,res=0,t,casec=1;
  ifstream myfile ("input.in");
  ofstream outp ("output.out");
  myfile>>tc;  
  while ( myfile.good() )
  {  
  myfile>>a;
  myfile>>b;
  if(myfile.eof())
      break;
 //cout<<a<<endl;
 //cout<<b<<endl;
  for(i=a;i<=b;++i)
  {
      if(i==1 || i==4 || i==9 || i ==121 || i==484)
      {
          
          //cout<<i<<endl;
          ++res;
      }
  }
  outp<<"Case #"<<casec<<": "<<res<<endl;
  ++casec;
  res=0;
  }
  /*
  sa=sqrt(a);
  sb=sqrt(b);
  for(i=sa;i<=sb;++i)
  {
      if(i==rev(i))
      {
          t=i*i;
          //cout<<i<<endl<<rev(i)<<endl;
          //cout<<"********** squares"<<endl;
          if(t==rev(t))
          {
              if(a>=10 && b<=120) 
                  continue;
              cout<<"t="<<t<<endl<<"rev(t)="<<rev(t)<<endl;
              cout<<"********** actual"<<endl;
              ++res;
          }
      }
  }
  outp<<"Case #"<<casec<<": "<<res<<endl;
  ++casec;
  res=0;
  //char buffer[]="924874187174872";
  //string tekst=buffer;
  //lli = atoll(buffer);
  //lli = sqrt (lli);
  //cout<<sb;
  //cout<<endl<<rev(sb)<<endl;
}
 */ 
  myfile.close();
  outp.close();
  return 0;
}

