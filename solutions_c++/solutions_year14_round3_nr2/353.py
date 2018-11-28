#include <iostream>
#include <vector>
#include <string>
#include <algorithm>



using namespace std;

const int MAXn = 12;
int jadval[MAXn];

bool good(string x)
{
  for(char tmp = 'a' ;tmp<='z'; tmp++)
    {
      bool b = 1;
      for(int i=0;i<x.size();i++)
	{
	  if(x[i]==tmp)
	    {
	      if(b==0)
		return 0;
	      b = 0;
	      while(i<x.size() && x[i] == tmp) i++;
	    }
	}
    }
  return 1;
} 


void make(string& x)
{
  string y= x;
  x= "";
  x+=y[0];
  for(int i=1;i<y.size();i++)
    {
      if(y[i]!=x[x.size()-1])
	x+=y[i];
    }
}


int main()
{
  ios::sync_with_stdio(false);
  int T;
  cin>>T;
  for(int I=1;I<=T;I++)
    {
      int tedad = 0;
      vector <string> myvec;
      int n;
      cin>>n;
      for(int i=0;i<n;i++)
	{
	  jadval[i] = i;
	  string x;
	  cin>>x;
	  make(x);
	  myvec.push_back(x);
	}

      do{
	//cerr<<"here"<<endl;
	string s;
	for(int i=0;i<n;i++)
	  s+=myvec[jadval[i]];
	//cerr<<s<<endl;
	if(good(s))
	  {
	    tedad++;
	    // tedad%=MOD;
	  }
      }while(next_permutation(jadval,jadval+n));
      cout<<"Case #"<<I<<": "<<tedad<<endl;
    }
  return 0;
}
