#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int N; 
    cin >> N;
    vector<string> S(N);
    map<string,int> words;
    vector< vector<int> > lines(N);
    int nextword = 1;
    string dummy_str;
    getline(cin,dummy_str);
    for (int i=0; i<N; i++) {
      getline(cin,S[i]);

      int p=0;
      while (p<S[i].length()) {
	if (S[i][p]<'a' || S[i][p]>'z') p++;
	else {
	  int q=p;
	  while (q<S[i].length() && S[i][q]>='a' && S[i][q]<='z') q++;
	  string w = S[i].substr(p,q-p);
	  if (words.find(w) == words.end()) words[w] = nextword++;
	  lines[i].push_back(words.find(w)->second);
	  p=q;
	};
      };
    };

    bool lang[2][nextword];

    int answer = nextword; 
    for (long long S=2; S < (1<<N); S+=4) {

      for (int i=0; i<2; i++)
	for (int j=0; j<nextword; j++)
	  lang[i][j] = false;

      for (long long i=0; i<N; i++) {
	long long L = (S >> i) & 1;
	for (int j=0; j<lines[i].size(); j++)
	  lang[L][lines[i][j]] = true;
      };

      int repeat = 0;
      for (int i=0; i<nextword; i++)
	if (lang[0][i] && lang[1][i]) repeat++;
      answer = min(answer, repeat);
    };

    cout << "Case #" << t << ": " << answer << endl;
  };
  return 0;
};
