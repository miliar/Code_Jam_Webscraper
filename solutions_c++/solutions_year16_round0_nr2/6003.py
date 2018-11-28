#include<iostream>
#include<string>

using namespace std;

int main(int argc, char **argv)
{
  int t;
  string input;

  cin>>t;

  for(int i = 1 ; i <= t ; i++)
  {
    cin>>input;

    int fc = input.length() - 1;

    for( int c = 0 ; 1 ; c++)
    {
      for( fc ; fc >= 0 ; fc-- )
        if(input[fc] == '-')
          break;

      if(fc == -1 )
      {
        cout<<"Case #"<<i<<": "<<c<<"\n";
        break;
      } 

      if(input[0] == '+')
      {
        for(int p = 0; p <= fc ; p++)
        {
          if(input[p] == '+')
            input[p] = '-';
          else
            break;
        }
      }
      else
      {
        for(int p = 0; p <= (fc/2) ; p++)
        {
          char c1,c2;
          if(input[p] == '+')
            c1 = '-';
          else
            c1 = '+';

          if(input[fc-p] == '+')
            c2 = '-';
          else
            c2 = '+';
       
          input[p] = c2;
          input[fc-p] = c1;
        }
      }
    }
  }

  return 0;
}

