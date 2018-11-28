#include <bits/stdc++.h>
#define MAXN int(1e8+2*1e7)
using namespace std;
typedef unsigned long long ull;
bool crib[MAXN];
ull dame[11];
string k;
int n,j;
ull number;

void sieve()
{
  memset(crib,0,sizeof crib);
  crib[1] = 1;
  for(int  i = 2 ; i <= MAXN ; ++i)
    {
      if(!crib[i])
	for(int j = 2*i  ; j <= MAXN ; j+=i )
	  crib[j] = 1;
    }
  // for(int  i = 0 ; i < 1000 ; ++i)
  //   if(!crib[i])
  //     cout << i << "\n";
}

bool itsprime(ull number,ull index)
{
  for(int i = 2 ; i*i <= number ; ++i)
    {
      if(!crib[i])
	{
	  if(number % i == 0)
	    {
	      dame[index]=i;
	      return 0;
	    }
	}
    }
  return 1;    
}

inline ull goestobase(ull num , ull base)
{
  ull mine=0,go = 1;
  for(int i = n ; i >= 0; --i)
    {
      ull part = num % 10;
      mine += part*go;
      num /= 10;
      go*=base;
    }
  return mine;
}


int main()
{
  sieve();
  int t; cin >> t;
  while(t--)
    {
      cout << "Case #1:\n";
      k = "";
      cin >> n >> j;
      for(int i = 0 ; i < n ; ++i)
	k += '0';
      k[0] = '1';    k[n-1] = '1';
      // cout << k << "\n";
      int cnt = 0;
      for(int i = 0 ; i < (1<<(n-2)); ++i)
      	{
	  if(cnt >= j)
	    break;
	  number = stoull(k);
	  bool sipo = 1;
	  for(int i = 2 ; i <= 10 ; ++i)
	    {
	      ull nuevo = goestobase(number,i);
	      // cout << nuevo << "\n";
	      if(itsprime(nuevo,i))
	      	sipo = 0;
	    }
	  if(sipo)
	    {
	      cout << number << " ";
	      for(int i = 2 ; i < 11 ; ++i)
		cout << dame[i] << " " ;
	      cout << "\n";
	      ++cnt;
	    }
      	  bool notset=1;
      	  int nones = n-2;
      	  while(notset)
      	    {
      	      if(k[nones] == '1')
      	  	k[nones]='0';
      	      else
      	  	{
      	  	  k[nones]='1';
      	  	  notset=0;
      	  	}
      	      --nones;
      	    }
	  // cout << number << "\n";
	  // cout << "comienza:\n";
	}
      // ull number=1;
      // for(int i = 0 ; i < n-1; ++i)
      // 	number*=10;
      // number +=1;
      
      
    }
  return 0;
}
