#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <limits>
#include <utility>
#include <iomanip>
#include <cassert>

#define endl '\n'
using namespace std;
typedef unsigned long long ll;

int n,j,jc=0;
vector<vector<ll>> results;

ll base_change(ll dec,int base){
  ll multi = 1,mask = 1,result = 0;
  for(int i=0;i<n;i++){
    if(dec & mask)
      result += multi;
    mask <<= 1;
    multi *= base;
  }
  return result;
}

bool is_prime(ll num){
  for(int i=2;i*i <= num;i++)
    if(num % i == 0) return false;
  return true;
}

ll get_proper_divisor(ll num){
  for(int i=2;i*i <= num;i++)
    if(num % i == 0) return i;
  assert(false);
}

void check_number(ll num){

  for(int i=0;i<results.size();i++)
    if(results[i][0] == num)
      return;

  vector<ll> cand(10); // cand[0] == num
  int base;
  for(base=2;base <=10;base++){
    ll cur = base_change(num,base);
    if(is_prime(cur)) break;
    cand[base-1] = get_proper_divisor(cur);
  }
  if(base == 11){
    jc++;
    cand[0] = num;
    results.push_back(cand);
  }
}

void search(ll num,int pos){
  if(jc == j) return;
  if(pos == n-1) return;

  check_number(num);
  if(jc == j) return;
  check_number(num | (1 << pos));

  search(num,pos+1);
  search(num | (1 << pos),pos+1);
}

int main(){

  int t;
  cin >> t;
  for(int tc = 1;tc <= t;tc++){
    cin >> n >> j;
    ll num = (1 << (n-1)) | 1;
    search(num,1);
    cout << "Case #" << tc << ":\n";
    for(int i=0;i<j;i++){
      vector<ll> cur = results[i];
      for(int k=0;k<cur.size();k++){
        cout << (k == 0 ? base_change(cur[k],10) : cur[k]) << " \n"[k == cur.size()-1];
      }
    }
  }
  return 0;
}
