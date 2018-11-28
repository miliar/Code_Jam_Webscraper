#include<stdio.h>
#include <fstream>
#include<iostream>
using namespace std;

int main()
{

  ifstream in ("q.txt");
  ofstream myfile ("outcheck.txt");
  if (in.is_open()&&myfile.is_open())
  {
    int t;
    in>>t;

    for(int c=0;c<t;c++)
    {
        int smax;
        in>>smax;
        string str;
        in>>str;
        unsigned long long int sum=(int)(str[0]-'0'),ans=0;
        int size=smax+1;

        for(int i=0;i<size;i++)
            myfile<<(int)(str[i]-'0');
        myfile<<"\n size : "<<size;

       /*
        for(int i=1;i<size;i++)
        {
            if((int)(str[i]-'0')>0)
            {
            //	cout<<"\n>0\n";
                if(i<=sum)
                {
                    sum+=(int)(str[i]-'0');
                }
                else
                {
                    ans+=i-sum;
                    sum=(int)(str[i]-'0')+i;
                }
            }
        //cout<<"\nvars : "<<ans<<" , "<<sum;

        }
*/
       // myfile<<"Case #"<<c+1<<": "<<ans<<"\n";
    }

  }
    return 0;
}
