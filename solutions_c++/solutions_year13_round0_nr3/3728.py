#include <iostream>
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
const int MAXLEN = 4;
using namespace std;

void add(vector<long long>& tab, int curr, int len, int left)
{
  if(left < 0)
    {return;}
  if(len == 0)
    {
      int temp = curr;
      int len = 0;
      while(temp!=0)
	{
	  temp /= 10;
	  ++len;
	}
      temp = curr;
      int div = 1;
      for(int i = 0; i < len; ++i)
	{
	  temp *= 10;
	  temp += (curr/div)%10;
	  div*=10;
	}
      tab.push_back(temp);
      temp = curr;
      div =10;
      for(int i = 0; i < len-1; ++i)
        {
          temp *= 10;
          temp += (curr/div)%10;
          div*=10;
        }
      tab.push_back(temp);
      return;
    }
  for(int i = 0; i < 4; ++i)
    {
      add(tab, curr*10+i, len-1, left-i*i);
    }
}

void buildTab(vector<long long>& tab)
{
  for(int i = 0; i < 4; ++i)
    {
      int curr = i;
      add(tab, curr, MAXLEN-1, 9);
    }
  sort(tab.begin(), tab.end());
}

long long biSearch(const vector<long long>& tab, long long a)
{
  int min = 0, max =tab.size()-1;
  while(min < max)
    {
      int mid = (min+max)/2;
      if(tab[mid] < a)
	{min = mid+1;}
      else if(tab[mid] > a)
	{max = mid;}
      else if(tab[mid] == a)
	{return mid;}
    }
  if(min!=max)
    {cerr << "ERROR" << endl;}
  return min-1;
}

int main()
{
  int T;
  cin >> T;
  vector<long long> tab;
  buildTab(tab);
  for(int i = 0; i < T; ++i)
    {
      long long a, b;
      cin >> a >> b;
      long long s = biSearch(tab, sqrt(b));
      s -= biSearch(tab, sqrt(a-1));
      cout << "Case #" << i+1 << ": " << s << endl;
    }
}
