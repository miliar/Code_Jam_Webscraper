#include <iostream>
#include <fstream>
#include <ctime>
#include <string>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>

using namespace std;


void solve(void);
void _solve(int n);

int main(int argc, char* argv[]){
  solve();
  return 0;
}

#define LINESIZE 2000
ofstream of;

int j;

void solve(){

  ifstream fl;
  fl.open("f1.in");
  of.open("f1x.out");

  int t, n, i;
  fl >> t;

  for (i = 0; i < t; i++){
    fl >> n;
    fl >> j;
    of << "Case #" << (i+1) << ":" << endl;;
    _solve(n);
  }

  fl.close();
  of.close();
}

bool check_string(char* s, int sz){
  
  vector<long long> divs(9);
  long long nr, l, k, pwr;
  int base, i;
  bool found;
  for (base = 2; base < 11; base++){
    nr = 0;
    pwr = 1;
    found = false;
    for (i = (sz - 1); i >= 0; i--){
      nr = nr + ((long long)(s[i] - '0') * pwr);
      pwr = pwr * base;
    }
    l = (long long)sqrt(nr);
    for (k = 2; k <= l; k++)
      if ((nr % k) == 0){
	divs[base-2] = k;
	found = true;
	break;
      }
    if (found == false)
      return false;
  }

  of << s;
  for (i = 0; i < 9; i++)
    of << ' ' << divs[i];

  of << endl;
  return true;
}

void gen(char* s, int sz, int poz){

  bool ret;

  if (poz == (sz - 1)){
    ret = check_string(s,sz);
    if (ret == true)
      j = j - 1;
    return;
  }

  if (j <= 0)
    return;

  s[poz] = '0';
  gen(s,sz,poz+1);

  if (j <= 0)
    return;

  s[poz] = '1';
  gen(s,sz,poz+1);
  return;
}

void _solve(int n){
  char s[n+1];
  int poz = 1;
  s[0] = '1';
  s[n-1] = '1';
  s[n] = '\0';
  gen(s,n,poz);
}
