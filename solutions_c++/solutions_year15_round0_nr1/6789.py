#include <iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream in;
      in.open("F:\\study\\Projects\\acm\\standing ovation\\A-small-attempt1.in");
         ofstream out;
         out.open("F:\\study\\Projects\\acm\\standing ovation\\out.out");
    int T,maxs,sum,fr,c;string s;
    in>>T;
    for(int k=1;k<=T;k++)
    {
  sum=0;
  fr=0;
  in>>maxs;
  in>>s;
  for(int z=0;z<s.size();z++)
  {
      if(s[z]!=0)
      {
          if(z>sum)
           {
               c=z-sum;
               fr+=c;
               sum+=int (s[z])-48+c;
           }
           else
            sum+=int (s[z])-48;

      }

  }


            out<<"Case #"<<k<<": "<<fr<<endl;



    }
in.close();
out.close();

    return 0;
}
