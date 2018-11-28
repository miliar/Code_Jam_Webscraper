#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <assert.h>
#include <queue>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <bitset>

using namespace std;

bool debug=false;

#define DEBUG if (debug) cout

//ostream& operator<<(ostream& o, const Omino& oo) {
//  for (int y=0; y<oo[0].size(); ++y) {
//    for (int x=0; x<oo.size(); ++x) {
//      o << oo[x][y] << " ";
//    }
//    o << endl;
//  }
//
//  return o;
//}

int N, J;

vector<bool> pc;

string int2string(long int i) 
{
  stringstream s;
  s << i;

  return s.str();
}

string int2string_base2(long int i)
{
  string s = std::bitset<64>(i).to_string();

  string num;

  for (int i = 64-N; i<64; ++i) {
    num.push_back(s[i]);
  }
  
  return num;
}

long int string2int(const string& s, int base=10)
{
  if (base == 10) {
    long int i;
    stringstream ss(s);
    ss >> i;
    
    assert(int2string(i) == s);

    return i;
  }

  return strtol(s.c_str(), NULL, base);
}

long int getDivisor(long int num)
{
  //  static map<long int, long int> cache;
  //  auto it = cache.find(num);
  //  if (it != cache.end()) return it->second;

  int sq=sqrt(num)+1;
  for (long int div = 2; div <= sq; ++div) {
    if ((num%div) == 0) { /*cache[num]*/ = div; return div; }
  }

  //  cache[num] = -1;
  return -1;
}

bool isJamCoin(vector<int>& e, const string& num)
{
  for (int b=2; b<=10; ++b) {
    long int n = string2int(num, b);

    long int div = getDivisor(n);
    if (div == -1) return false;

    e.push_back(div);
  }

  assert(e.size() == 9);
  return true;
}


bool solve_(string num)
{
  int cont=0;
  while (cont < J) {
    vector<int> examples;
    if (isJamCoin(examples, num)) {
      cont++;
      cout << num;
      for (int n: examples)
        cout << " " << n;
      cout << endl;
    }

    num = int2string_base2(string2int(num, 2)+1);
    num[N-1] = '1';
  }
}


long int solve()
{
  string firstNum(N, '0');
  firstNum[0] = '1';
  firstNum[N-1] = '1';

  solve_(firstNum);

  return 0;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    i >> N;
    i >> J;

    cout << "Case #" << c+1 << ":" << endl;
    long int a = solve();
  }

  return true;
}



int main(int argv, char* argc[])
{
  if (argv < 2) {
    cout << "Usage " << argc[0] << " <inputFile>" << endl;
    exit(1);
  }

  ifstream filei(argc[1]);

  readFile(filei);

  return 0;
}
