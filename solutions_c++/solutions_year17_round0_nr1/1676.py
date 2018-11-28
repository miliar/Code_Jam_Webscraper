#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream out;
ifstream in;

int casei=1;
#define OUTPUT(type)\
void output(type i) { out << "Case #" << casei << ": " << i << endl; casei++; }

OUTPUT(int);
OUTPUT(long long);
OUTPUT(const char*);
OUTPUT(string);

void worker();
int main()
{
  in.open("input");
  out.open("output");
  int cnt;
  in >> cnt;
  for (int i=0; i<cnt; i++) {
    worker();
  }
  in.close();
  out.close();
  return 0;
}







string s;
int k;
int sa[2000];

void worker()
{
  int r = 0;
  in >> s >> k;
  cout << s << endl;
  const char* p = s.c_str();
  int l = s.length();
  for (int i=0; i<l; i++) {
    if (*p == '-') sa[i]=1;
    else sa[i]=0;
    p++;
  }
  for (int i=0; i<l-k+1; i++) {
    if (sa[i] == 1) {
      sa[i] = 0;
      for (int j=0; j<k-1; j++)
        sa[i+j+1] = (sa[i+j+1]+1)%2;
      r++;
    }
  }
  for (int i=0; i<k; i++) {
    if (sa[l-i-1] == 1) {
      output("IMPOSSIBLE");
      return;
    }
  }
  output(r);
}
