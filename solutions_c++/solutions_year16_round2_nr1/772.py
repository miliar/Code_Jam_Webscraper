#include <iostream>
#include <cstring>
using namespace std;
int main() {
  int cases;
  int a[30];
  int o[30];
  cin>>cases;
  for (int z=1;z<=cases;z++) {
    string s;
    cin>>s;
    memset(a,0,sizeof(a));
    memset(o,0,sizeof(o));
    for (int i=0;i<s.size();i++) {
      a[s[i]-'A']++;
    }
    while(a['X'-'A']>0) {
      o[6]++;
      a['S'-'A']--;
      a['I'-'A']--;
      a['X'-'A']--;
    }
    while(a['Z'-'A']>0) {
      o[0]++;
      a['Z'-'A']--;
      a['E'-'A']--;
      a['R'-'A']--;
      a['O'-'A']--;
    }
    while(a['W'-'A']>0) {
      o[2]++;
      a['T'-'A']--;
      a['W'-'A']--;
      a['O'-'A']--;
    }
    while(a['U'-'A']>0) {
      o[4]++;
      a['F'-'A']--;
      a['O'-'A']--;
      a['U'-'A']--;
      a['R'-'A']--;
    }
    while(a['O'-'A']>0) {
      o[1]++;
      a['O'-'A']--;
      a['N'-'A']--;
      a['E'-'A']--;
    }
    while(a['G'-'A']>0) {
      o[8]++;
      a['E'-'A']--;
      a['I'-'A']--;
      a['G'-'A']--;
      a['H'-'A']--;
      a['T'-'A']--;
    }
    while(a['H'-'A']>0) {
      o[3]++;
      a['T'-'A']--;
      a['H'-'A']--;
      a['R'-'A']--;
      a['E'-'A']--;
      a['E'-'A']--;
    }
    while(a['F'-'A']>0) {
      o[5]++;
      a['F'-'A']--;
      a['I'-'A']--;
      a['V'-'A']--;
      a['E'-'A']--;
    }
    while(a['V'-'A']>0) {
      o[7]++;
      a['S'-'A']--;
      a['E'-'A']--;
      a['V'-'A']--;
      a['E'-'A']--;
      a['N'-'A']--;
    }
    o[9]=a['N'-'A']/2;
    cout<<"Case #"<<z<<": ";
    for (int i=0;i<=9;i++) {
      for (int j=1;j<=o[i];j++) {
        cout<<i;
      }
    }
    cout<<endl;
  }
  return 0;
}
