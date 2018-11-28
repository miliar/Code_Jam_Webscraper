#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int t;
int n;
int main()
{
  cin >> t;
  for(int i= 0; i < t; i++)
  {
    cin >> n;
    string s;
    cin >> s;
    int result = 0;
    int cursum = 0;
    for(int j = 0; j < n + 1; j++)
    {
      if(cursum < j && s[j] != '0')
      {
        result += j-cursum;
        cursum = j;
      }
      cursum += s[j]-'0';
    }
    printf("Case #%d: %d\n", i+1, result); 
  }
}
