#include<iostream>
#include<unordered_set>

using namespace std;

int main()
{
  long long t, N;
  cin>>t;
  for(long long i=1; i<=t; i++)
  {
    long long observed = 0;
    long long original, curr;
    unordered_set<int> obs;
    cin>>original;
    curr = original;
    if(original == 0)
    {
      cout<<"Case #"<<i<<": INSOMNIA"<<endl;
      continue;
    }
    while(observed < 10)
    {
      long long x = curr;
      while(x > 0)
      {
        long long digit = x%10;
        if(obs.find(digit) == obs.end())
        {
          observed++;
          obs.insert(digit);
        }
        x = x/10;
      }
      if(observed == 10)
        break;
      curr += original;
    }
    cout<<"Case #"<<i<<": "<<curr<<endl;
  }
  return 0;
}
