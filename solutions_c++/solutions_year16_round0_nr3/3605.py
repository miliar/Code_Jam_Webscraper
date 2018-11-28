#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#define MAX_N 100000000
#define N 16
#define J 50
using namespace std;

vector<bool> primeTable;

string to_bin_string(unsigned long long m)
{
  string s;
  while(m) {
    s = to_string(m%2) + s;
    m /= 2;
  }

  while(s.length() < N)
    s = "0" + s;

  return s;
}

bool isPrime(unsigned long long n, int &divisor)
{

  if(n > primeTable.size() - 1) {
    for(int i = 2; i < primeTable.size(); i++) {
      if(primeTable[i] && (n%i == 0) ) {
        divisor = i;
        return false;
      }
    }
    return true;
  }

  bool ret = primeTable[n];
  if(!ret) {
    for(unsigned long long i = 2; i < n; i++)
      if(n%i == 0) {
        divisor = i;
        break;
      }
  }
  return ret;
}

unsigned long long intprt(unsigned long long m, int base)
{
  unsigned long long val = 0, bt = 1;
  while(m) {
    val += m%2 ? bt : 0;
    m = m>>1;
    bt *= base;
  }

  cout<<"intprt val="<<val<<endl;
  return val;
}

void foo(ofstream& fout){
  //int N = 16, J = 50;
  int count = 0, m = 0b1000000000000001;
  vector<string> result;

  while(count < J) {
    
    bool success = true;
    string oneLine = to_bin_string(m) + " ";
    for(int base = 2; base <= 10; base++) {
      int divisor = 0;
      if(!isPrime(intprt(m, base), divisor) && divisor != 0) {
        cout<<"count = "<<count<<", m="<<m<<"|"<<"passed base:"<<base<<", div:"<<divisor<<endl;
        oneLine += to_string(divisor);
        if(base != 10)
          oneLine += " ";
        cout<<oneLine<<endl;
      } else {
        cout<<"count = "<<count<<", m="<<m<<"|"<<"failed base:"<<base<<endl;
        success = false;
        break;
      }

    }

    if(success) {
      fout<<oneLine<<endl;
      result.push_back(oneLine);
      count++;
    }
    m += 2;
  }

  cout<<"result:::"<<endl;
  for(int i = 0; i < result.size(); i++)
    cout<<i<<" "<<result[i]<<endl;
}

void getPrime(){
  for(unsigned long long i=0;i<MAX_N;i++)
    primeTable.push_back(true);
  primeTable[0]=false;
  primeTable[1]=false;
  
  for(unsigned long long i=2;i<MAX_N;i++){
    if(primeTable[i])
    for(unsigned long long j=i;i*j<MAX_N;j++){
      primeTable[i*j]=false;
    }
    else continue;
  }
}

int main(){
  getPrime();
//  for(int i = 0; i < primeTable.size(); i++)
//    cout<<primeTable[i]<<" ";

  ofstream fout;
  //ifstream fin;
  //fin.open("A-small-attempt0.in");
  fout.open("Cs.out");
  
  cout<<"open success\n";
  
  int T = 0;
  //fin>>T;
  
  cout<<"input size success\n";

  fout<<"Case #1:"<<endl;
  foo(fout);

}