#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include <functional>
#include<numeric>
using namespace std;



int sum(const vector<pair<int, char> > &values)
{
  int su = 0;
  for(int i=0; i < values.size();i++)
    {
      su += values[i].first; 
    }
  return su;
}

bool has_majority(vector<pair<int, char> > values)
{
  long long total = sum(values);
  for(int idx = 0; idx < values.size();idx++)
    {
      if(2 * values[idx].first > total)
        return true;
    }
  return false;
}

int main()
{
  int T;
  cin>>T;
  for(int t = 0; t < T; t++)
    {
      int n;
      cin>>n;
      vector<pair<int, char> > values;
      for(int i=0; i < n; i++)
        {
          int temp;
          cin>>temp;
          values.push_back(make_pair(temp, 'A' + i));
        }
      cout<<"Case #"<<t + 1<<": ";
      sort(values.begin(), values.end(), greater<pair<int, char> >());
      long long total = sum(values);
      while(total > 0)
        {
          sort(values.begin(), values.end(), greater<pair<int, char> >());

          //Check first values
          values[0].first -= 2;
          if(!has_majority(values))
            {
              cout<<values[0].second<<values[0].second<<" ";
              total = sum(values);
              continue;
            }

          values[0].first += 2;

          // first two elements
          values[0].first -= 1;
          values[1].first -= 1;
          if(!has_majority(values))
            {
              cout<<values[0].second<<values[1].second<<" ";
              total = sum(values);
              continue;
            }
          values[0].first += 1;
          values[1].first += 1;

          //first elements
          values[0].first -= 1;
          if(!has_majority(values))
            {
              cout<<values[0].second<<" ";
              total = sum(values);
              continue;
            }
          else
            {
              cout<<"error"<<endl;
            }
        }
      cout<<endl;
    }
}
