#include <bits/stdc++.h>
using namespace std;


string reduccao(string cad)
{
  string nueva="";
  char act = cad[0];
  nueva+=act;
  for(int i = 1 ; i < cad.size() ; ++i)
    {
      if(act != cad[i])
	{
	  nueva+=cad[i];
	  act= cad[i];
	}
    }
  return nueva;
}


int main()
{
  int n; cin >> n;
  for(int i = 0 ; i < n ; ++i)
    {
      int cnt=0;
      string nai,cad,towork,cpy;  cin >> cad;
      towork = reduccao(cad);
      cpy = towork;
      if(cpy.size() == 1)
	{
	  if(cpy[0] == '+')
	    cout <<"Case #" << i+1 << ": "<< "0"<< "\n";
	  else
	    cout <<"Case #" << i+1 << ": "<< "1" << "\n";
	}
      else
	{
	  while(nai.size() != 1 or nai[0] != '+')
	    {
	      ++cnt;
	      nai = cpy[1];
	      for(int i = 2 ; i < cpy.size() ; ++i)
		nai += cpy[i];
	      cpy = nai;
	      // cout << nai << "\n";
	      if(nai.size() == 1 and nai[0] == '-')
	        {
		  ++cnt;
		  nai = "+";
		}
	    }      
	  cout <<"Case #" << i+1 << ": "<<  cnt << "\n";
	}
    }
  return 0;
}
