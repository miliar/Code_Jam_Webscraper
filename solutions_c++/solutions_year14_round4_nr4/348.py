#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int number;
int T,N,M;
vector<string> S;

int last[4], best_so_far;

int lcp(int i,int j) {
  int k=0;
  while (k<S[i].length() && k<S[j].length() && S[i][k]==S[j][k]) k++;
  return k;
};

void try_solution(int i,int size) {
  if (i==M)  {
    for (int j=0; j<N; j++)
      if (last[j]<0) 
	return;
    if (size>best_so_far) { best_so_far=size; number=0; }
    if (size==best_so_far) number++;
  } else {
    for (int j=0; j<N; j++) {
      // try trie j
      int prev_last = last[j];
      last[j]=i;
      try_solution(i+1, size + (prev_last<0 ? 
				S[i].length()+1 :
				S[i].length()-lcp(prev_last,i)
				));
      last[j] = prev_last;
    };
  };
};

int main () {
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> M >> N;
    S = vector<string>(M,"");
    for (int i=0; i<M; i++) cin >> S[i]; 
    sort(S.begin(),S.end());
    best_so_far=number=0;
    for (int j=0; j<N; j++) last[j]=-1;
    try_solution(0,0);
    cout << "Case #" << t << ": " << best_so_far << " " << number << endl;
  };
};
