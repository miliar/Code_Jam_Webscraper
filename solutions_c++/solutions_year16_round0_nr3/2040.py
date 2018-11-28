#include <iostream>
#include <array>
#include <iomanip>
#include <bitset>
#include <cmath>

typedef unsigned __int128 uli;
typedef unsigned int ui;

using namespace std;

bitset<65536> non_prime(0);

uli index_to_num(uli index){
  return index * 2 + 3;
}

uli num_to_index(uli num){
  return (num - 3) / 2;
}

void init_prime(){
  ui max = index_to_num(non_prime.size());
  ui sqmax = ceil(sqrt(max));
  for(ui i = 3; i <= sqmax;){
    for(ui j = i * 3; j < max; j += i * 2){
      non_prime[num_to_index(j)] = 1;
    }
    for(i += 2; non_prime[num_to_index(i)] == 1; i += 2);
  }
}

uli find_divisor(uli n){
  if((n % 2) == 0){
    return 2;
  }
  for(ui i = 0; i < non_prime.size(); i++){
    if(non_prime[i] == 0){
      if(n % index_to_num(i) == 0){
        return index_to_num(i);
      }
    }
  }
  return 0;
}

uli uli_pow(uli a, uli b){
  uli c = 1;
  while(b--){
    c *= a;
  }
  return c;
}

uli expand(ui base, uli n){
  uli num = 0;
  ui digit = 1;
  do{
    if(n % 2){
      num += uli_pow(base, digit);
    }
    digit++;
  }while(n /= 2);
  return num;
}

string bin(uli n){
  string s;
  do{
    s = to_string((ui)(n % 2)) + s;
  }while(n /= 2);
  return s;
}

int main(){
  init_prime();
  ui t;
  cin >> t;
  for(ui i = 0; i < t; i++){
    ui n, j;
    cin >> n >> j;
    ui count = 0;
    cout << "Case #" << i + 1 << ":" << endl;
    for(ui k = 0; k < (ui)(1 << (n - 2)); k++){
      array<unsigned long long int, 9> proofs;
      for(ui base = 2; base <= 10; base++){
        uli num = 1 + expand(base, k) + uli_pow(base, n - 1);
        uli div = find_divisor(num);
        if(!div){
          goto next_jam;
        }
        proofs[base - 2] = div;
      }
      cout << "1" << setfill('0') << setw(n - 2) << bin(k) << "1";
      for(auto k : proofs){
        cout << " " << k;
      }
      cout << endl;
      count++;
      if(count >= j){
        return 0;
      }
    next_jam:;
    }
  }
  return 1;
}
