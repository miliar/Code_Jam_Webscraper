//Google Code Jam
//Preamble

#include <stdio.h>
#include <memory.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>

#define fo(a,b,c) for( a = ( b ); a < ( c ); a++)
#define fr(a,b) fo( a, 0, ( b ))
#define fi(a) fr(i, ( a ))
#define fj(a) fr(j, ( a ))
#define fk(a) fr(k, ( a ))
#define pb push_back
 
using namespace std;

string line;
stringstream ss;
ifstream input;
ofstream output;

int ir()
{
  int a;
  getline(input,line);
  ss << line;
  ss >> a;
  ss.clear();
  return a;
}

double dr()
{
  double a;
  getline(input,line);
  ss << line;
  ss >> a;
  ss.clear();
  return a;
}

long long llr()
{
  long long a;
  getline(input,line);
  ss << line;
  ss >> a;
  ss.clear();
  return a;
}

string sr()
{
  string a;
  getline(input,line);
  ss << line;
  ss >> a;
  ss.clear();
  return a;
}

void pi(int t, int a)
{
  cout << "Case #" << t+1 << ": " << a << endl;
}

void pd(int t, double a)
{
  cout << "Case #" << t+1 << ": " << a << endl;
}

void ps(int t, string a)
{
  cout << "Case #" << t+1 << ": " << a << endl;
}

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

bool istrue(string s, int nval)
{
  int k = 0;
  int n = 0;
  for(int i = 0;i < s.length();i++)
    {
      if(s[i] != 'a' && s[i] != 'e' && s[i] != 'i' && s[i] != 'o' && s[i] != 'u')
	{
	  k++;
	  if(k >= n)
	    n = k;
	}
      else
	k = 0;
    }
  if(n >= nval)
    return true;
  else
    return false;
}
	  

int main(int arc, char** argv)
{
  input.open(argv[1]);
  output.open(argv[2]);

  int T;
  int t,i,j,k;
  string name,subs;
  int nval,nstr,n;

   if(input.is_open())
    {
      T = ir();
      fr(t,T)
	{
	  getline(input,line);
	  ss << line;
	  ss >> name;
	  ss >> nval;
	  ss.clear();
	  nstr = 0;
	  for(i = 0; i < (name.length() - nval + 1); i++)
	    {
	      for(j = nval; j < (name.length() - i + 1); j++)
		{		  
		  subs = name.substr(i,j);
		  if(istrue(subs,nval))
		    nstr++;
		}
	    }
	  output << "Case #" << t+1 << ": " << nstr << endl;
	}
      input.close();
      output.close();
    }
  
  else
    cout << "Unable to open file" << endl;
  
  return 0;
}
