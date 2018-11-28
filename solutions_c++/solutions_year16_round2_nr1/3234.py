#include <cstdio>
#include <cstring>

int T, tt;
char str[3000];
int chr[30];
int res[20];
char cls[] = "RONHFIVSTE";

char digits[10][8] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int adj[26][10] = {
  {},// A
  {},// B
  {},// C
  {},// D
  {6, 0,1,3,5,7,9},// E
  {2, 4,5},// F
  {},// G
  {2, 3,8},// H
  {4, 5,6,8,9},// I
  {},// J
  {},// K
  {},// L
  {},// M
  {3, 1,7,9},// N
  {4, 0,1,2,4},// O
  {},// P
  {},// Q
  {3, 0,3,4},// R
  {2, 6,7},// S
  {3, 2,3,8},// T
  {},// U
  {2, 5,7},// V
  {},// W
  {},// X
  {},// Y
  {},// Z
};
void init() {
  for(int i = 0; i < 30; i++) {
    chr[i] = 0;
    res[i] = 0;
  }
}

void remove(int num, int t) {
  for(char *c = digits[num]; *c != '\0'; c++)
    chr[*c - 'A'] -= t;
}

void add(int num, int t) {
  for(char *c = digits[num]; *c != '\0'; c++)
    chr[*c - 'A'] += t;
}

bool check(int num) {
  for(int i = 0; digits[num][i] != '\0'; i++) {
    char d = digits[num][i];
    if(chr[d-'A'] == 0)
      return false;
  }
  return true;
}

void show() {
  int i;
  for(i = 0; i < 'Z'-'A'; i++)
    if(chr[i] > 0)
      printf("(%c %d) ", 'A' + i, chr[i]);
  printf("\n");
}
bool dfs(int i, int j) {
  if(cls[i] == '\0')
    return true;

  int a = cls[i] - 'A';
  if(chr[a] > 0) {
    for(int k = j; k < adj[a][0]; k++)
      if(check(adj[a][k+1])) {
        remove(adj[a][k+1], 1);
        res[adj[a][k+1]]++;
        bool found = dfs(i, k);
        if(found)
          return true;
        add(a, 1);
        res[adj[a][k+1]]--;
      }
  }
  else {
    return dfs(i+1, 0);
  }
  return false;
}

void solve() {
  init();
  scanf("%s", str);
  for(int i = 0; str[i] != '\0'; i++)
    chr[str[i]-'A']++;
  res[0] += chr['Z'-'A'];
  remove(0, chr['Z'-'A']);
  res[2] += chr['W'-'A'];
  remove(2, chr['W'-'A']);
  res[4] += chr['U'-'A'];
  remove(4, chr['U'-'A']);
  res[6] += chr['X'-'A'];
  remove(6, chr['X'-'A']);
  res[8] += chr['G'-'A'];
  remove(8, chr['G'-'A']);
  dfs(0, 0);
  for(int i = 0; i < 10; i++)
    for(int j = 0; j < res[i]; j++)
      printf("%d", i);
  printf("\n");
}

int main() {
  scanf("%d", &T);
  for(tt = 1; tt <= T; tt++) {
    printf("Case #%d: ", tt);
    solve();
  }
  return 0;
}
