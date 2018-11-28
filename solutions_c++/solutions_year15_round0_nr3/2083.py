#include <queue>
#include <cstdio>
using namespace std;

int main() {
  int T, D, P;
  scanf(" %d", &T); 
  for (int t=1; t<=T; t++) {
    fprintf(stderr, "Case #%d\n", t);
    int X, L;
    scanf(" %d %d", &L, &X);
    char a[10001];
    scanf(" %s", a);

    bool sgn = false;
    char pos = '1', next_cut = 'i';
    for (int x=0; x<X; x++) {
      for (int l=0; l<L; l++) {
        
	if (pos == '1') {
          pos = a[l];
        } else if (pos == a[l]) {
          pos = '1';
          sgn = !sgn;
        } else if (pos == 'i') {
          if (a[l] == 'j') {
            pos = 'k';
          } else {
            pos = 'j';
            sgn = !sgn;
          }
        } else if (pos == 'j') {
          if (a[l] == 'k') {
            pos = 'i';
          } else {
            pos = 'k';
            sgn = !sgn;
          }
        } else { 
          if (a[l] == 'i') {
            pos = 'j';
          } else {
            pos = 'i';
            sgn = !sgn;
          }
        }

	if (sgn == false && pos == next_cut) {
          next_cut++;
          pos = '1';
        }
      }
    }

    if (sgn == false && pos == '1' && next_cut == 'l') {
      printf("Case #%d: YES\n", t);
    } else {
      printf("Case #%d: NO\n", t); 
    }
  }
}
