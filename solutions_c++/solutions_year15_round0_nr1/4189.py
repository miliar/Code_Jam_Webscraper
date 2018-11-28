#include<iostream>

using namespace std;


inline unsigned int toI(char c) {
  return (int)(c-'0');
}

int main() {
  unsigned int T;

  cin >> T;

  for (unsigned int t=1; t<=T; ++t) {
    unsigned int y=0;
    unsigned int Smax;
    string s;
    cin >> Smax >> s;
    unsigned int sum=toI(s[0]);
    for (unsigned int i=1; i<=Smax; ++i) {
      unsigned int nf=0;
      if (sum<i)
	nf=(i-sum);
      sum+=(toI(s[i])+nf);
      y+=nf;
    }
    cout << "Case #" << t << ": " << y << endl;
  }

  return 0;
}
