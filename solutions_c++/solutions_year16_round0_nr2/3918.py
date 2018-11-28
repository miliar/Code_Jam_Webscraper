#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>

using std::ifstream;
using std::ofstream;
using std::vector;
using std::string;
using std::set;
using std::endl;

bool f[10] = {0};

int main() {
  ifstream fin("c_in.txt");
  ofstream fout("c_out.txt");
  int T = 0;
  fin >> T;
  for (int i = 0; i<T; i++) {
    string str; int ans = 0;
    
    fin >> str;
    vector<char> buffer;
    buffer.push_back('.');
    for (int j =0; j<str.size(); j++)
      if (str[j]!=buffer.back())
	buffer.push_back(str[j]);
    ans = buffer.size()-1;
    if (buffer.back()=='+') ans--;
    fout << "CASE #"<<i+1<<": "<<ans<<endl;
  }
  return 0;
}
