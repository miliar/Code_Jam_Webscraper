#include <iostream>

using namespace std;

char answer[4096];
int N, R, P, S;

char verify(int i,int d) {
  if (d==0) return answer[i];
  char a=verify(i,d-1), b=verify(i+(1<<(d-1)),d-1);
  if (a=='-' || b=='-' || a==b) return '-';
  if ((a=='P' && b=='R') || (b=='P' && a=='R')) return 'P';
  if ((a=='P' && b=='S') || (b=='P' && a=='S')) return 'S';
  return 'R';
};

bool solve(int r,int p,int s) {
  if (r==0 && p==0 && s==0) {
    return verify(0,N) != '-';    
  } else {
    int i=(1<<N)-p-r-s;
    if (p>0) { answer[i]='P'; if (solve(r,p-1,s)) return true; }
    if (r>0) { answer[i]='R'; if (solve(r-1,p,s)) return true; }
    if (s>0) { answer[i]='S'; if (solve(r,p,s-1)) return true; }
    return false;
  };
};

int main() {
  int t;
  cin >> t;
  for (int x=1; x<=t; x++) {
    cin >> N >> R >> P >> S;
    cout << "Case #" << x << ": ";
    if (! solve(R,P,S) ) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      for (int i=0; i<(1<<N); i++) cout << answer[i];
      cout << endl;
    };
  };
  return 0;
};
