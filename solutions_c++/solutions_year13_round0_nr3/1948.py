#include <fstream>
#include <math.h>
#include <vector>
using namespace std;

inline bool p(long long pre)
{
  long long result=0;
  int q;
  long long current=pre;
  while (current>0)
  {
    q=current%10;
    current=current/10;
    result=result*10+q;
  }
  if (pre==result)
    return true;
  return false;
}

int main()
{
  ifstream fin("C-large-1.in");
  ofstream fout("C-large-attempt1.out");
  vector<int> arr;
  int n,num;
  fin>>n;
  long long a,b;
  double low,up;

  for (long long i=1;i<100000000;i++)
  {
    if (!p(i))
      continue;
    else if (p(i*i))
      arr.push_back(i);
    else continue;
  }
  
  for (long long i=0;i<n;i++)
  {
    num=0;
    fin>>a>>b;
    low=sqrt(a);
    up=sqrt(b);

    for (int j=0;j<arr.size();j++)
      if ((arr[j]<=up)&&(arr[j]>=low))
        num++;
    fout<<"Case #"<<i+1<<": "<<num<<endl;
  }
  return 0;
}
