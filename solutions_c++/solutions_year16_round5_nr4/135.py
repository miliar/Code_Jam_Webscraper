#include <cstdio>
#include <cstring>

char goods[110][60];
char bad[60];

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int N, L; scanf("%d%d", &N, &L);

    for(int i = 0; i < N; i++) scanf("%s", goods[i]);
    scanf("%s", bad);

    bool val = true;
    for(int i = 0; i < N; i++) if(strcmp(goods[i], bad) == 0) val = false;

    printf("Case #%d: ", tt);

    if(!val) puts("IMPOSSIBLE");
    else{
      if(L == 1) puts("? 0");
      else if(L == 2) puts("? 10?1");
      else{
        for(int i = 0; i < L - 1; i++) printf("?");
        printf(" 10?");
        for(int i = 0; i < L - 2; i++) printf("%d", (i + 1) % 2);
        printf("\n");
      }
    }
  }
  return 0;
}

/*
#include <cstdio>
#include <cstring>
#include <set>
#include <string>
using namespace std;

char S1[110], S2[110];
int L1, L2;

char s[210];
char t[210];

set<string> st;

void play(int x, int y){
if(x == L1 && y == L2){
printf("%s : ", s);

bool v = false; int c = 0;
for(int i = 0; i < L1 + L2; i++){
if(s[i] == '?') t[c++] = '0' + v;
else if(s[i] == '0') v = false;
else v = true;
}

puts(t);
st.insert(t);
return ;
}

if(x != L1){ s[x + y] = S1[x]; play(x + 1, y); }
if(y != L2){ s[x + y] = S2[y]; play(x, y + 1); }
}

int main(){
scanf("%s%s", S1, S2);
L1 = strlen(S1); L2 = strlen(S2);

play(0, 0);

printf("%d\n", (int)st.size());
return 0;
}
 */
