#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <iomanip>
#include <fstream>
#include <stdlib.h> 
#include  <iterator>
#include <stdexcept>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

template<typename T> T from_str(std::string key)
{
      std::stringstream ss(key);
      T convertedValue;
      if ( ss >> convertedValue ) return convertedValue;
      else throw std::runtime_error("conversion failed");
}

std::pair<char,int> ms(char a, char b)
  {
    
    if(a == 'i')
      {
	if(b == 'i')
	  return std::pair<char,int>('1',-1);
	else if(b == 'j')
	  return std::pair<char,int>('k',1);
	else if(b == 'k')
	  return std::pair<char,int>('j',-1);

      }
    else if(a == 'j')
      {
	if(b == 'i')
	  return std::pair<char,int>('k',-1);
	else if(b == 'j')
	  return std::pair<char,int>('1',-1);
	else if(b == 'k')
	  return std::pair<char,int>('i',1);

      }
    else if(a == 'k')
      {
	if(b == 'i')
	  return std::pair<char,int>('j',1);
	else if(b == 'j')
	  return std::pair<char,int>('i',-1);
	else if(b == 'k')
	  return std::pair<char,int>('1',-1);
      }
    else
      {
	cout << a << "bug" << endl;
      }

    return std::pair<char,int>('0',0);
  }

int signe(const std::string& a)
{
  uint sign = 1;
  char b;
  std::string x(a);
  std::pair<char,int> meu;
  while(x.size() > 1)
    {
      meu = ms(x[0],x[1]);
      b = meu.first;
      sign *= meu.second;
      x = (b == '1' ? x.substr(2) :  b + x.substr(2));
    }

  return sign;

}


char m(char a, char b)
  {
    
    if(a == 'i')
      {
	if(b == 'i')
	  return '1';
	else if(b == 'j')
	  return 'k';
	else if(b == 'k')
	  return 'j';

      }
    else if(a == 'j')
      {
	if(b == 'i')
	  return 'k';
	else if(b == 'j')
	  return '1';
	else if(b == 'k')
	  return 'i';

      }
    else if(a == 'k')
      {
	if(b == 'i')
	  return 'j';
	else if(b == 'j')
	  return 'i';
	else if(b == 'k')
	  return '1';
      }
    else
      {
	cout << a << "bug" << endl;
      }

    return '0';
  }

std::string simplify(const std::string& a)
{
  char b;
  std::string x(a);
  while(x.size() > 1)
    {
      b = m(x[0],x[1]);
      x = (b == '1' ? x.substr(2) :  b + x.substr(2));
    }
  return x;
}


  int ta,tb;

std::string resultat(std::string line, uint L, uint X)
{



  std::string linetemp = std::string();
  if(X < 10)
    {
      for(unsigned int kk = 0; kk < X ; kk++)
  	linetemp += line;
      line = linetemp;
      X = 1;
    }


  std::string part1 = line + (X > 1 ? line : "");
  char a = part1[0];
  ta = -1;
  if(a != 'i')
    {
      for(unsigned int ll = 1; ll < part1.size(); ++ll)
	{
	  a = m(a, part1[ll]);
	  if(a == '1')
	    {
	      ll += 1;
	      a = part1[ll];
	    }
	  if(a == 'i')
	    {
	      ta = ll;
	      break;
	    }
	}
    }
  else 
    ta = 0;

  if(ta == -1)
    return "NO";

  std::string left = part1.substr(ta+1);
  std::string part2 = left + (X > 1 ? line : "") + (X > 1 ? line : "");

  
  char b = part2[0];
  tb = -1;
  if(b != 'j')
    {
      for(unsigned int ll = 1; ll < part2.size(); ++ll)
	{
	  b = m(b, part2[ll]);

	  if(b == '1')
	    {
	      ll += 1;
	      b = part2[ll];
	    }
	  if(b == 'j')
	    {
	      tb = ll;
	      break;
	    }
	}
    }
  else 
    tb = 0;

  if(tb == -1)
    return "NO";

   left = part2.substr(tb+1);
     
   std::string part3 = left + (X > 1 ? line : "") + (X > 1 ? line : "");
   std::string the_end("");
   if(X==1)
     the_end = simplify(part3);
   else if(simplify(line) == "")
     the_end = simplify(part3);
   else
     {
       if(X%2 == 0)
	 the_end = simplify(part3);
       else
	 the_end = simplify(part3 + line);
     }
   //   cout << the_end << endl;
  if(the_end != "k")
    return "NO";

  else
    {
      if(X == 1 and signe(line) == -1)
	return "YES";
      else if(simplify(line) != ""  and X%2 == 0 and X%4 != 0) 
	return "YES";
      else if(simplify(line) == "" and signe(line) == -1 and X%2 != 0 ) 
	return "YES";
      else
	return "NO";
    }
    

}



int main()
{
  string line,  result;;
  ifstream input ("C-small-attempt6.in");
  ofstream output ("C-small-attempt6.out");
  unsigned int nb_test,L,X;

  if (input.is_open())
    {
      input >> nb_test;
      for(unsigned int kk=1; kk <= nb_test; ++kk)
	{

	  input >> L >> X >> line;
	  // //test
	  // std::string full("");
	  // for(unsigned int k =0; k < X; k++)
	  //   full += line;

	  result = resultat(line,L,X);
	  if(output.is_open())
	    {
	      cout << "Case #" << kk << ": " << result << endl;
	      output << "Case #" << kk << ": " << result << endl;
	      // if(true)
	      // 	{
	      // 	  cout <<" t " <<  ta << " " << tb << endl;
	      // 	  std::string val1 = full.substr(0,ta+1), val2 = full.substr(ta+1, tb+1), val3 = full.substr(ta+tb+2); 
	      // 	  cout << simplify(val1) << " ";
	      // 	  cout << simplify(val2) << " ";
	      // 	  cout << simplify(val3) << endl;
	      // 	}

	    }
	}
      input.close();
      output.close();
    }
}

