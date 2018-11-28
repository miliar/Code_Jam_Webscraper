#include <fstream>
#include <string>
#include <iostream>
#include <cassert>
#include <sstream>
using namespace std;

ifstream in;
ofstream out;

long long to_long(string x) {
  stringstream sstr(x);
  long long r;
  sstr >> r;
  return r;
}

string to_string(long long n) {
  stringstream out;
  out << n;
  return out.str();
}

string multiply(string a, string b) {
  long long x = to_long(a);
  long long y = to_long(b);
  return to_string(x*y);
}

bool palindrome(string x) {
  int l=x.length();
  int i;
  for (i=0;i*2<l && x[i]==x[l-1-i];++i);
  return i*2 >= l;
}

int count(string A, string B) {
  long long x = to_long(A);
  long long y = to_long(B);
  long long i;
  int count=0;
  for (i=0;i*i <= y;++i) {
    if (i*i<x) continue;
    string s = to_string(i);
    if (!palindrome(s)) continue;
    if (!palindrome(to_string(i*i))) continue;
    cout<<i<<" "<<i*i<<endl;
    count ++;
  }
  return count;
}

string A,B;

int main(int argc, char *argv[]) {
  assert(argc==3 || argc==4);
  string name=string(argv[1])+"-"+argv[2];
  if (argc==4)
    name += string("-")+argv[3];
  in.open((name+".in").c_str());
  assert(in);
  out.open((name+".out").c_str());
  assert(out);

  int T;
  in >> T;
  for (int t=1;t<=T;++t) {
    in >> A >> B;
    out<<"Case #"<<t<<": "<<count(A,B)<<endl;
  }
  return 0;
}
