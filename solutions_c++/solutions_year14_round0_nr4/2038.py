#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#define LL long long
#define MP make_pair
#define PB push_back
#define ff first
#define ss second
#define DEBUG(x) cerr<<#x<<" "<<(x)<<endl;

using namespace std;
int wynik, wynik2, n;
void rozwaz(vector<double> v1, vector<double> v2)
{
  int m = v1.size();
  if(m == 0)
    return;
  
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  
  for(int i=m-1; i>=0; i--)
  {
    if(v1[i] < v2[i])
    {
      swap(v2[i], v2.back());
      v2.pop_back();
      swap(v1[0], v1.back());
      v1.pop_back();
      rozwaz(v1, v2);
      return;
    }
  }
  wynik += m;  
}
void zwykle(vector<double> v1, vector<double> v2)
{
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  int in = 0;
  int ret = v1.size();
  for(int i=0; i<=v1.size()-1; i++)
  {
    while(in < v2.size() && v2[in] < v1[i])
      in++;
    if(in < v2.size())
    {
      ret--;
      in++;
    }
  }
  wynik2 += ret;
}

int main()
{
  int t;
  scanf("%d", &t);
  for(int z=1; z<=t; z++)
  {
    wynik = wynik2 = 0;
    printf("Case #%d: ", z);
    scanf("%d", &n);
    vector<double>v1, v2;
    v1.clear();
    v2.clear();
    double x;
    for(int i=1; i<=n; i++)
    {
      scanf("%lf", &x);
      v1.PB(x);
    }
    for(int i=1; i<=n; i++)
    {
      scanf("%lf", &x);
      v2.PB(x);
    }
    zwykle(v1, v2);
    rozwaz(v1, v2);
    printf("%d %d\n", wynik, wynik2);
  }
  
  return 0;
}