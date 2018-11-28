#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    long int t,arr[10],x,i,j,a,c;
    in>>t;
    for(i=1;i<=t;i++)
    {
        in>>x;
        if(x==0)
        {
            out<<"Case #"<<i<<": INSOMNIA\n";
            continue;
        }
        for(j=0;j<10;j++)
        {
            arr[j]=0;
        }
        c=1;
        while(1)
        {
          a=c*x;
          while(a>0)
          {
              arr[a%10]++;
              a=a/10;

          }
          for(j=0;j<10;j++)
          {
              if(arr[j]==0)
              {
                  break;
              }

          }
          if(j==10)
          {
              out<<"Case #"<<i<<": "<<c*x<<"\n";
              break;
          }
          c++;


        }

    }

    return 0;
}
