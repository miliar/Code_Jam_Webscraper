#include <iostream>

using namespace std;

int main()
{
  int t;
  cin >> t;
  for(int j=1; j<=t; j++)
  {
    int smax, s[1001],i ;
    char s_str[1002];
    cin >> smax;
    cin >> s_str;
    for (i=0; i<=smax; i++)
      s[i] = s_str[i]-'0';
    int sum=s[0], num=0;
    for (i=1; i<=smax; i++)
    {
      if(sum < i)
      {
        num += i-sum;
        sum = i+s[i];
      }
      else
      {
        sum += s[i];
      }
    }
    cout << "Case #" << j << ": " << num << endl;
  }
  return 0;
}
