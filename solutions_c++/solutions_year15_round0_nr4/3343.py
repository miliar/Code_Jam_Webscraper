#include <bits/stdc++.h>

using namespace std;

typedef long long          ll;
typedef vector<int>        vi;
typedef pair<int, int>     ii;
typedef vector<ii>         vii;
typedef set<int>           si;
typedef set<ii>            sii;
typedef map<string, int>   msi;

int main() {
  int t, tc=0; scanf("%d", &t);

  sii A;
  A.insert(ii(1, 1));
  // A.insert(ii(1, 2));
  // A.insert(ii(2, 1));
  A.insert(ii(1, 3));
  A.insert(ii(3, 1));
  A.insert(ii(3, 3));
  // A.insert(ii(1, 4));
  // A.insert(ii(4, 1));

  sii B;
  B.insert(ii(2, 3));
  B.insert(ii(3, 2));
  B.insert(ii(3, 3));
  B.insert(ii(3, 4));
  B.insert(ii(4, 3));

  sii C;
  C.insert(ii(3, 4));
  C.insert(ii(4, 3));
  C.insert(ii(4, 4));
  
  while(t--) {
    int x, r, c;
    scanf("%d %d %d", &x, &r, &c);
    
    if(x == 1) {
      printf("Case #%d: GABRIEL\n", ++tc);
    } else if(x == 2) {
      if(A.count(ii(r, c)) == 0)
	printf("Case #%d: GABRIEL\n", ++tc);
      else
	printf("Case #%d: RICHARD\n", ++tc);
    } else if(x == 3) {
      if(B.count(ii(r, c)) == 0)
	printf("Case #%d: RICHARD\n", ++tc);
      else
	printf("Case #%d: GABRIEL\n", ++tc);
    } else if(x == 4) {
      if(C.count(ii(r, c)) == 0)
	printf("Case #%d: RICHARD\n", ++tc);
      else
	printf("Case #%d: GABRIEL\n", ++tc);
    }
  }

  return 0;
}
