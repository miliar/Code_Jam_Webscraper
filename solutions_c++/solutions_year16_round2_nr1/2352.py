#include <bits/stdc++.h>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef map<string, int>   msi;

vi V(10, 0);
vi A(255, 0);

void f(string s, char c) {
  for(int i=0; i<s.length(); i++)
    if(s[i] != c) {
      A[s[i]] -= A[c];
    }
  A[c] = 0;
}

int main() {
  int t, tc = 0; scanf("%d", &t);

  while(t--) {
    string s; cin >> s;
    A.assign(255, 0);
    for(int i=0; i<s.length(); i++) A[s[i]]++;

    V.assign(10, 0);

    V[0] += A['Z']; f("ZERO", 'Z');
    V[2] += A['W']; f("TWO", 'W');
    V[4] += A['U']; f("FOUR", 'U');
    V[6] += A['X']; f("SIX", 'X');
    V[8] += A['G']; f("EIGHT", 'G');

    /////////////////////
    
    V[1] += A['O']; f("ONE", 'O');
    V[3] += A['H']; f("THREE", 'H');
    V[5] += A['F']; f("FIVE", 'F');
    V[7] += A['S']; f("SEVEN", 'S');

    /////////////////////
    
    V[9] += A['I']; f("NINE", 'I');

    printf("Case #%d: ", ++tc);
    
    for(int i=0; i<V.size(); i++)
      for(int j=0; j<V[i]; j++)
	cout << i;

    cout << endl;
  }

  return 0;
}

