#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main() {

  ifstream fin;
  ofstream fout;
  fin.open("A-large.in");
  fout.open("A-large-practice.out");

  int t;
  fin>>t;

  for(int i=0;i<t;i++) {
    int smax;
    fin>>smax;

    string s;
    fin>>s;

    vector<int> S(s.size());

    for(int k=0;k<s.size();k++)
      S[k] = s[k]-'0';

    int ans = 0;
    int standing = 0;
    for(int k=0;k<s.size();k++) {
      if(standing < k && S[k] != 0){
        ans += k-standing;
        standing = k+S[k];
      }

      else
          standing += S[k];

    }
    fout<<"case #"<<i+1<<": "<<ans<<"\n";
  }

  return 0;
}
