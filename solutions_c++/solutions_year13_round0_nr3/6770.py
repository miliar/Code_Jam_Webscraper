#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<long double> rngs;


bool is_palin(long double n)
{  
  int dbuf[200];
  
  int pos = 0;
  
  while(n >= 1)
  {
    dbuf[pos++] = fmod(n,10);
    n/=10;    
  }
  
  for(int i = 0 ; i < pos/2; ++i)
  {
    if(dbuf[i] != dbuf[pos-i-1])
      return false;
  }
  
  return true;  
}


int get_num_fair_and_square(long double beg,long double end)
{
  long double b = ceil(sqrt(beg));
  long double e = floor(sqrt(end));
  
  int nfnsq = 0;
  
//   cerr<< " b" <<b<<endl;
//   cerr<< " e" <<e<<endl;
  
  for(; b <=e ; ++b)
  {
    if(!is_palin(b))
    {
//       cerr<<b<<": b is not a palin"<<endl;
      continue;
    }
    
    if(!is_palin(b*b))
    {
//       cerr<<b*b<<": b*b is not a palin"<<endl;
      continue;
    }

    
    nfnsq++;
  }
  
  return nfnsq;
}

int main()
{
  int n;  
  cin >> n;
  
  rngs.resize(n*2);
  
  for(int i = 0 ; i < n*2 ; ++i)
    cin>>rngs[i];
  
  for(int i = 0 ; i < n; ++i)
  {
    cout<< "Case #"<<i+1<<": "<<get_num_fair_and_square(rngs[2*i],rngs[2*i+1])<<endl;    
  }
    
}