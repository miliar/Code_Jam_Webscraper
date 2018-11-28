#include <iostream>
#include <string>

using namespace std;

int process(int SMAX, string AUD)
{
  int out = 0;
  int sum = AUD.at(0) - 48;
  int i;
  int Si;

  for(i = 1; i <= SMAX; i++)
  {
    Si = AUD.at(i) - 48;
//    cout<<AUD.at(i)<<" "<<Si<<endl;
    if(sum < i)
    {
      out = out + (i - sum);
      sum = i;
    }
    sum = sum + Si;
  }
  return out;
}

int main(void)
{
  int T;
  int SMAX;
  string AUD;
  int i;
  int *out;

  cin>>T;
  out = new int [T];
  for(i = 1; i <= T; i++)
  {
    cin>>SMAX;
    cin>>AUD;
    out[i-1] = process(SMAX,AUD); 
  }
  for(i = 1; i <= T; i++)
  {
    cout<<"Case #"<<i<<": "<<out[i-1]<<endl;
  }
  return 0;
}
