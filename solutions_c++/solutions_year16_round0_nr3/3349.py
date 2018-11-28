
#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void pv(vector<int> v){
  for(int i=0; i<v.size(); i++){ cout << v[i] << " "; }
}

void pv(vector<long> v){
  for(int i=0; i<v.size(); i++){ cout << v[i] << " "; }
  cout << endl;
}
void pvn(vector<long> v){
  for(int i=0; i<v.size(); i++){ cout << v[i]; }
  cout << " ";
}

void pv(vector<char> v){
  for(int i=0; i<v.size(); i++){ cout << v[i] << " "; }
  cout << endl;
}

long isPrime( long num ){
  if(num <= 1){ return false; }
  if(num == 2){ return true; }
  for(long i=2; i<=floor(sqrt(num)); i++){
    if( num % i == 0 ){
      //cout << num << " is not prime" << endl;
      return i;
    }
  }
  //cout << num << " is prime" << endl;
  return -1;
}

/*
vector<long> numbers( vector<long> v ){

  for(long i=2; i<=10; i++){

    long sum = 0;
    for(long j=0; i<v.size(); j++){
      sum += v[j] * pow(i,j);
    }
    v.push_back( isPrime(sum) );

  }
  return v;

}*/

long build = 0;
vector<long> increment(vector<long> &v){
  build += 1;
  long cbuild = build;
  int index = 1;
  while( cbuild > 0 ){
    long t = cbuild & 1;
    v[index] = t;
    cbuild = cbuild >> 1;
    index += 1;
  }
  return v;
}

int main(){
  long N, J;
  cin >> N >> J;
  cout << "Case #1:" << endl;
  vector<long> v(N,0);
  v[0] = 1; v[N-1] = 1;

  long found = 0;
  while( found < J){

      bool skip = false;
      vector<long> bn;
      vector<long> dn;
      for(long i=2; i<=10; i++){

        long sum = 0;
        for(long j=0; j<v.size(); j++){
          sum += v[j] * pow(i,j);
        }
        bn.push_back( sum );
        long tt = isPrime(sum);
        dn.push_back( tt );
        if(tt == -1){
          skip = true;
          break;
        }

      }
/*
      cout << "bn: ";
      pv(bn);
      cout << "dn: ";
      pv(dn);
*/
      //cout << "before inc: ";
      //pv(v);

      if(skip){
        increment(v);
        continue;

      }else{
        vector<long> tv = v;
        reverse(tv.begin(), tv.end());
        pvn( tv );
        pv(dn);
        found += 1;
        increment(v);

      }
      //cout << "after inc: ";
      //pv(v);

    }

  return 0;
}

/*
6 3
*/
