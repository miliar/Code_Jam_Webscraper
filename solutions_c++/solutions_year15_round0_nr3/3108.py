#include <iostream>
#include <string>
using namespace std;

signed int sign_lookup(char x, char y)
{
  signed int out = 1;

  if((x == '1') || (y == '1') || ((x == 'i') && (y == 'j')) || ((x == 'j') && (y == 'k')) || ((x == 'k') && (y == 'i')))
  {
    out = 1;
  }
  else
  {
    out = -1;
  }
  return out;
}

char char_lookup(char x, char y)
{
  char out;

  if(x == '1')
  {
    out = y;
  }
  else if(y == '1')
  {
    out = x;
  }
  else if (x == y)
  {
    out = '1';
  }
  else if(((x == 'i') && (y == 'j')) || ((x == 'j') && (y == 'i')))
  {
    out = 'k';
  }
  else if(((x == 'i') && (y == 'k')) || ((x == 'k') && (y == 'i')))
  {
    out = 'j';
  }
  else
  {
    out = 'i';
  }
  return out;
}

string process(int L, int X, string ijk_str)
{
  string out = "YES";
  char next_char = '1';
  signed int sign = 1;
  int i;
  int all_char_same = 1;
  int i_not_found = 1;
  int j_not_found = 1;
  int k_not_found = 1;

  if((L*X) < 3)
  {
    out = "NO";
  }
  else
  {
    if(L == 1)
    {
      return "NO";
    }
    else
    {
      for(i = 1; i < L; i++)
      {
	if(ijk_str.at(i) != ijk_str.at(i-1))
        {
	  all_char_same = 0;
	}
      }
      if(all_char_same == 1)
	return "NO";
    }
    for(i = 0; i < L; i++)
    {
      sign = sign * sign_lookup(next_char,ijk_str.at(i));
      next_char = char_lookup(next_char,ijk_str.at(i));
    }
    if((next_char == '1') && (sign == 1))
    {
	out = "NO";
    }
    else if (((X % 2) == 0) && (next_char == '1'))
    {
      out = "NO";
    }
    else if(next_char == '1')
    {
	goto YES;
    }
    else if ((X % 2) == 1)
    {
      out = "NO";
    }
    else if ((X % 4) == 0)
    {
      out = "NO";
    }
    else
    {
      YES:
      sign = 1;
      next_char = '1';
      out = "NO";
      for(i = 0; i < L*X; i++)
      {
        sign = sign * sign_lookup(next_char,ijk_str.at(i % L));
        next_char = char_lookup(next_char,ijk_str.at(i % L));
	if(i_not_found)
	{
	  if((sign == 1) && (next_char == 'i'))
	  {
	    i_not_found = 0;
	    next_char = '1';
	  }
	}
	else if(j_not_found)
	{
	  if((sign == 1) && (next_char == 'j'))
	  {
	    j_not_found = 0;
	    next_char = '1';
	  }
	}
	else if(k_not_found)
	{
	  if((sign == 1) && (next_char == 'k'))
	  {
	    k_not_found = 0;
	    next_char = '1';
	    out = "YES";
	    break;
	  }
	}
      }
    }
  }

  return out;
}
int main(void)
{
  int T;
  int L;
  int X;
  string ijk_str;
  int i;
  string *out;
  cin>>T;
  out = new string [T];
  for(i = 1; i <=T ; i++)
  {
    cin>>L;
    cin>>X;
    cin>>ijk_str;
    out[i-1] = process(L,X,ijk_str);
  }
  for(i = 1; i <=T ; i++)
  {
    cout<<"Case #"<<i<<": "<<out[i-1]<<endl;
  }
  return 0;
}
