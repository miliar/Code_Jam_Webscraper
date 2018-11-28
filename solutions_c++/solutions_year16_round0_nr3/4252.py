#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <cstdlib>
#include <bitset>
#include <cmath>
#include <unordered_set>
#include <gmpxx.h>

using namespace std;

//unordered_set<mpz_class> prime_list;

bool is_prime(mpz_class val, mpz_class &div){
  //auto it = prime_list.find(val);
  //if(it != prime_list.end()) return true;
  for(int i = 2; i < sqrt(val + 1); i++){
      if(val % i == 0){
        div = i;
        return false;
      }
  }
  //prime_list.insert(val);
  return true; 
}

/*string to_bit_string(long long x, int n){
  string str(n,'0');

  for(int i = 0; i < n; i++){
    ;
  }
}*/


int main(){




  int total_cases;
  cin >>total_cases;
  int total_candidates = 0;;
  int number_to_find;
  int n;
  cin >>n;
  cin >>number_to_find;

  long long max_val = pow(2,n);

  cout<<"Case #1:"<<endl;
  for(long long i = (1ll << (n-1)) + 1; i < max_val; i+= 2){

    if(total_candidates >= number_to_find) break;
    bitset<32> b(i);
    string str = b.to_string();
    str = str.substr(32-n,n);
    mpz_class temp(str);
    int not_prime_count = 0;
    mpz_class div_array[9] = 0;
    for(int j = 2; j <= 10; j++){
      mpz_class num(str,j);
      mpz_class divisor = 0;
      if(is_prime(num,divisor)) break;

      if(!is_prime(num,divisor)){
        not_prime_count++;
        div_array[j-2] = divisor;
      }

    }
    if(not_prime_count == 9){
      total_candidates++;
      cout<<str<<" ";
      for(auto x: div_array) cout<<x<<" ";
      cout<<endl;
    }


  }
   
   
  


  return 0;
}