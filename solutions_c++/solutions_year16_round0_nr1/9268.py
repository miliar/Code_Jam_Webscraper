#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
void check(int y,int z[])
    {   int temp=y%10;
        int left=y/10;
        z[temp]=1;
           if(left==0)
           return;
        check(left,z);
    }
int main()
{
    int casesnum,N;
    int z[10];
    ifstream input;
    ofstream output;
	input.open("A-large.in");
	output.open("A-large.out");
    input>>casesnum;
    for(int i=1;i<=casesnum;i++)
   {    input>>N;
           if(N==0)
               {
                   output<<"Case #"<<i<<": INSOMNIA"<<endl;
                   continue;
               }
           int x=0;
           bool notyet=false;
           bool allones=true;
           for(int k=0;k<10;k++)
            {
                z[k]=0;
            }
            for(int j=1;!notyet;j++)
            {   allones=true;
                 x=j*N;
                 check(x,z);
                 for(int k=0;k<10;k++)
                    {
                        if(z[k]!=1)
                            {allones=false;
                            break;
                            }
                    }
                 if(allones)
                 notyet=true;
            }
           output<<"Case #"<<i<<": "<<x<<endl;
    }
  return 0;
}
