#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <memory.h>
#include <ctime>
#include <assert.h>
#include <stack>
//#include <cstdLL>
#include <bitset>
#include <iomanip> // for std::setprecision()

using namespace std;

//typedef LL_fast64_t Li;
//typedef LL_fast32_t ll;
//typedef LL_fast8_t ii;
typedef long long LL;
typedef long l;

#define arjun main()
#define FOR(i,x,y) for(LL i = (x) ; i <= (y) ; ++i)
//typedef makepair mpr;

#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);
#define mpr(x,y) make_pair(x,y);

//const ll arrsz=2*10e9+1;

namespace patch
{
    template < typename T > std::string to_string( const T& n )
    {
        std::ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

//usage use a>=b>=0;
//Ifa≥b,then a mod b <a/2.
/**
 *If d divides both a and b, and d = ax + by for some integers x and y, then necessarily
 *d = gcd(a, b).
**/
LL findgcd(LL a,LL b) {
  if(b==0) return a;
  return findgcd(b,a%b);
}

/**
 * find the min of two numbers!
 */

LL minm (LL a, LL b) {
  return !(b<a)?a:b;     // or: return !comp(b,a)?a:b; for version (2)
}

/**
 * If p is prime, then for every 1 ≤ a < p,
 * pow(a,p−1) ≡ 1 (mod p). ---> (pow(a,p−1)-1)%p ==0
 */

bool primetest(LL a)
{
  for (size_t i = 2; i <= sqrt(a); i++) {
    if(a%i == 0) return true;
  }
  return false;
}

/**
 * program for sorting an array in descending order
 * end here is the number of elements not the index
 */

LL* sort_descending(LL* array,LL start,LL end){
    sort(array+start,array+end+1,std::greater<LL>());
    return array;
}

/**
 *function similar to inbuilt max,finds maximum of two numbers
 */

LL maxm (LL a, LL b) {
    return !(b>a)?a:b;     // or: return !comp(b,a)?a:b; for version (2)
}

/**
 *function that calculates nCk using the property (n-1)C(k-1) + (n-1)Ck ,using dp
 */
LL nCk_dp_array[60][60] = {{0}};
LL nCk_dp_for_non_fixed_n_k (LL n, LL k) {
    nCk_dp_array[0][0] = 1;
    for (size_t i = 0; i <= n; i++) {
      for (size_t j = 0; j <=i; j++) {
        if (j == 0 || j==i) {
          nCk_dp_array[i][j] = 1;
        }
        else
        {
          nCk_dp_array[i][j] = nCk_dp_array[i-1][j-1]+nCk_dp_array[i-1][j];
        }
      }
    }
    return nCk_dp_array[n][k];
}

LL modular_exponential(LL base,LL exponent, LL modulus)
{
    LL result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

LL flip(string s,int j,LL count)
{
  if(j == 0)
  {
    if(s[j] == '-') return count+1;
    else return count;
  }
  if(s[j]=='+') return flip(s,j-1,count);
  else
  {
    LL r = 0;
    bool flag = false;
    while(s[r] == '+' && r<j)
    {
      s[r]='-';
      r++;
      flag = true;
    }
    if(flag)
      count++;
    std::string s2 = s.substr(0,j+1);
    //std::cout << s2<<" "<<s<<" 1 "<<j << std::endl;
    std::string s3 = "";
    int len_s2 = j;
    while(len_s2>=0)
    {
      if(s2[len_s2] == '+')
      {
        s3+='-';
      }
      else s3+='+';
      len_s2--;
    }
    count++;
    //std::cout << s3<<" "<<s<<" 2 "<<j << std::endl;
    s3+=s.substr(j+1);
    //std::cout << s3<<" "<<s<<" 3 "<<j << std::endl;
    return flip(s3,j-1,count);
  }
}

int arjun
{
  LL t;
  string s;
  cin>>t;
  LL count = 1;
  while(t!=0)
  {
    cin>>s;
    std::cout << "Case #"<<count<<": "<<flip(s,s.length()-1,0) << std::endl;
    t--;
    count++;
  }
  return 0;
}
