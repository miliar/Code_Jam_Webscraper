#include <iostream>
#include <vector>
#include <deque>

#include <algorithm>
#include <string>
#include <iomanip>

#include <limits>

#include <cmath>

using namespace std;

typedef long long ll;

typedef std::pair<ll,ll> mypair;

typedef unsigned long long ull;

#include <sstream>

bool is_palindrome(ull n)
{
  stringstream ss;
  ss << n;
  string str = ss.str();
  
  int len = str.length();
  int half = len/2;
  
  for(int i=0; i<half; ++i)
  {
    if(str[i] != str[len-1-i])
      return false;
  
  }
  
  return true;

}

int main()
{
  
  //cout<<numeric_limits<ull>::max()<<endl;
  //Result: 18446744073709551615
  //18446,74407,37095,51615
  //20 digits
  
  int T=0;
  
  cin>>T;
  
  //const int number_of_digits = 3;//for small
  //const int max_root_length = number_of_digits/2 + 1;
  /*
  vector<vector<ull> > palindromes(max_root_length);
  vector<vector<ull> > fair_and_square(number_of_digits);
  
  for(int i=0; i<max_root_length; ++i)
  {
    int basis_length = int(ceil(double(i+1)/2.0));
    
    //Exp. time! NO GOOD!
  }
  */
   
  for(int i=0; i<T; ++i)
  {
    ull A, B;
    
    cin>>A>>B;
    
    ull count = 0;
    
    for(ull n=A; n<=B; ++n)
    {
      if(!is_palindrome(n)) continue;
      
      double root = sqrt(double(n));
      
      if(floor(root) != root) continue;
      
      if(is_palindrome(ull(floor(root))))
        ++count;
    }
    
    cout<<"Case #"<<i+1<<": "<<count<<endl;
    
  }
  
	return 0;
}
