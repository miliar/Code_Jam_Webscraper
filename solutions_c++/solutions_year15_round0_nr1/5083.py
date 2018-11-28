#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{int T,t;
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 cin>>T;
 for(t=1;t<=T;t++)
 {int M,i,S=0,p=0,d; string x;
  cin>>M>>x;
  for(i=0;i<=M;i++)
  {if(x[i]=='0')continue;
   if(i>S)d=i-S; else d=0;
   S+=d+x[i]-'0'; p+=d;
  }
  cout<<"Case #"<<t<<": "<<p<<endl;
 }
 //   system("PAUSE");
    return EXIT_SUCCESS;
}
