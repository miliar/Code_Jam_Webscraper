#include<iostream>

using namespace std;

int main(int argc, char **argv)
{
  int t;
  int digs[10];
  long long value, cValue, ans;

  cin>>t;

  for(int i = 1 ; i <= t ; i++)
  {
    cin>>value;

    if(value == 0)
    {
      cout<<"Case #"<<i<<": INSOMNIA\n";  
    }
    else
    {
      for(int p = 0; p <10 ; p++)
        digs[p] = 0;

      for( int c=1 ; 1 ; c++)
      {
        ans = cValue = value * (long long)(c);

        while(cValue != 0)
        {
          digs[(cValue%10)] = 1;
          cValue = cValue / (long long)(10);
        }

        int nComp = 0;
        for(int p = 0; p <10 ; p++)
          if(digs[p] == 0)
            nComp = 1;

        if( nComp == 0)
        {
          cout<<"Case #"<<i<<": "<<ans<<"\n";
          break;
        }
      }
    } // else
       
  }

  return 0;
}
