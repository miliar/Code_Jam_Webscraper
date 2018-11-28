#include <cstdio>
#include <cstring>

using namespace std;

char s[105];

int main() {
   int T;
   scanf("%d", &T);
   for (int t = 1; t <= T; t++) {
      scanf(" %s", &s);
      int cnt = 1;
      for (int i = 1; i < strlen(s); i++)
         cnt+=s[i-1]!=s[i];
      printf("Case #%d: %d\n", t, cnt - (s[0]=='-')*!(cnt%2) - (s[0]=='+')*(cnt%2) );
   }
	return 0;
}

