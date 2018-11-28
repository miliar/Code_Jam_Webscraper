#include<iostream>
#include<string>
#include<cmath>

using namespace std;

long long baseC(string num, int base)
{
    long long ans = 0;
    for(int i = num.length()-1, c = 0 ; i >= 0 ; i--, c++)
    {
      if(num[i] == '1')
        ans = ans + pow(base,c);
    }

    return ans;
}

string rBaseC(long long num)
{
  string ans="1000000000000001";

  for(int i = 15 ; i >=0 ; i--)
  {
    ans[i] = char(num%2+'0');
    num = num/2;
  }

  return ans;

}

long long checkJC(long long num)
{
  long long sq = sqrt(num);

  for(long long i = 2 ; i < sq+1 ; i++)
  {
    if ( (num % i) == 0 )
      return i;
  } 
 
  return 0;
}

int main(int argc, char **argv)
{
  int t,n,j;
  string num = "1000000000000001";
  long long list[10];

  cin>>t;

  for(int i = 1 ; i <= t ; i++)
  {
    cin>>n>>j;

    cout<<"Case #"<<i<<":\n";

    long long num = 32767;
    int count = 0;
    while(count < j)
    {
      num += 2;
      string sNum = rBaseC( num );

      int nJC = 0;   
      for(int bc = 2; bc <=10 ; bc++)
      {
        long long dm = checkJC( baseC(sNum,bc) );
        if ( dm > 0 )
          list[bc-2] = dm;
        else
        {
          nJC = 1;
          break;
        }
      }

      if( ! nJC )
      {
        count++;
        cout<<sNum;
        for(int p = 0 ; p < 9 ; p++)
          cout<<" "<<list[p];
        cout<<"\n";
      }
    }

  }

  return 0;
}

