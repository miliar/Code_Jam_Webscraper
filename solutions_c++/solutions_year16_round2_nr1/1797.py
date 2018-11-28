#include <iostream>
#include <string>
using namespace std;

int main() {
  int cas, T;
  int arr[26];
  int res[10];
  string s;
  cin>>T;

  for (cas=1; cas<=T; ++cas) {
    for (int i=0; i<26; ++i) arr[i]=0;
    for (int i=0; i<10; ++i) res[i]=0;
    cin>>s;
    for (int i=0; i<s.size(); ++i) ++arr[s[i]-'A'];

    res[0] = arr['Z'-'A'];
    arr['Z'-'A'] -= res[0];
    arr['E'-'A'] -= res[0];
    arr['R'-'A'] -= res[0];
    arr['O'-'A'] -= res[0];
    
    res[6] = arr['X'-'A'];
    arr['S'-'A'] -= res[6];
    arr['I'-'A'] -= res[6];
    arr['X'-'A'] -= res[6];

    res[7] = arr['S'-'A'];
    arr['S'-'A'] -= res[7];
    arr['E'-'A'] -= res[7];
    arr['V'-'A'] -= res[7];
    arr['E'-'A'] -= res[7];
    arr['N'-'A'] -= res[7];

    res[5] = arr['V'-'A'];
    arr['F'-'A'] -= res[5];
    arr['I'-'A'] -= res[5];
    arr['V'-'A'] -= res[5];
    arr['E'-'A'] -= res[5];

    res[4] = arr['F'-'A'];
    arr['F'-'A'] -= res[4];
    arr['O'-'A'] -= res[4];
    arr['U'-'A'] -= res[4];
    arr['R'-'A'] -= res[4];

    res[8] = arr['G'-'A'];
    arr['E'-'A'] -= res[8];
    arr['I'-'A'] -= res[8];
    arr['G'-'A'] -= res[8];
    arr['H'-'A'] -= res[8];
    arr['T'-'A'] -= res[8];

    res[2] = arr['W'-'A'];
    arr['T'-'A'] -= res[2];
    arr['W'-'A'] -= res[2];
    arr['O'-'A'] -= res[2];

    res[9] = arr['I'-'A'];
    arr['N'-'A'] -= res[9];
    arr['I'-'A'] -= res[9];
    arr['N'-'A'] -= res[9];
    arr['E'-'A'] -= res[9];

    res[1] = arr['O'-'A'];
    arr['O'-'A'] -= res[1];
    arr['N'-'A'] -= res[1];
    arr['E'-'A'] -= res[1];

    res[3] = arr['T'-'A'];
    arr['T'-'A'] -= res[3];
    arr['H'-'A'] -= res[3];
    arr['R'-'A'] -= res[3];
    arr['E'-'A'] -= res[3];
    arr['E'-'A'] -= res[3];

    for (int i=0; i<26; ++i) if (arr[i]) cout<<"error\n";
    cout<<"Case #"<<cas<<": ";
    for (int i=0; i<10; ++i)
      for (int j=0; j<res[i]; ++j)
        cout<<i;
    cout<<endl;
  }

  return 0;
}
