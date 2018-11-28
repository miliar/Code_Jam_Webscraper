#include <iostream>
#include <fstream>
using namespace std;

string flip(int i, string s){
    string w = s;
    for(int j = 0; j < i; ++j)
        if(s[j] == '+')
            w[j] = '-';
        else
            w[j] = '+';
    return w;
}

bool done(string s){
    for(int i = 0; i < s.size(); ++i)
        if(s[i] == '-')
            return false;
    return true;
}



int f(int n, int j, string s){
    if(done(s))
        return n;
    if(j == s.size()+1) return 1000000000;
    int mn = 10000000000, m, m1, m2;
    //ss = s.size();
    //for(int i = 1; i <= ss; ++i){
//        m = f(n+1, flip(i, s));
//        if(m < mn){
//            mn = m;
//        }
//    }
    m1 = f(n+1, j+1, flip(j, s));
    m2 = f(n,   j+1, s);
    return m1>m2?m2:m1;
}

int main() {
  long long t, n;
  string s;
  ifstream fin {"B-small-attempt0.in"};
  ofstream fout {"b-small.out"};
  fin >> t;
  for (int i = 1; i <= t; ++i) {
    fin >> s;

    fout << "Case #" << i << ": " << f(0, 0, s) << endl;
  }
}
