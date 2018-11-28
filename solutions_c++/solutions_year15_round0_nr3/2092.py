#include <bits/stdc++.h>
using namespace std;

int T, L, X, a[10005];
bool ans;
char s[10005], ori[10005];
int rr[10005][2];

int mt[4][4][2] = {
  {{+1,0}, {+1,1}, {+1,2}, {+1,3}},
  {{+1,1}, {-1,0}, {+1,3}, {-1,2}},
  {{+1,2}, {-1,3}, {-1,0}, {+1,1}},
  {{+1,3}, {+1,2}, {-1,1}, {-1,0}}
};

int mul(int lo, int hi){
  if(lo > hi) return 0;
  int sin = rr[hi][0], val = rr[hi][1];
  if(lo > 0){
    sin *= -1 * mt[rr[lo - 1][1]][val][0];
    val = mt[rr[lo - 1][1]][val][1];
  }
  if(sin == -1) val += 4;
  return val;
}

int main(){

  scanf("%d", &T);
  for(int ct = 1; ct <= T; ct ++){
    scanf("%d %d", &L, &X);
    scanf(" %s", ori);

    s[0] = 0;
    for(int i = 0; i < X; i ++)
      strcat(s, ori);

    int len = strlen(s);

    for(int i = 0; i < len; i ++)
      if(s[i] == 'i')
        a[i] = 1;
      else if(s[i] == 'j')
        a[i] = 2;
      else
        a[i] = 3;
    

    int sin = 1, val = 0;
    for(int i = 0; i < len; i ++){
      sin = sin * mt[val][a[i]][0];
      val = mt[val][a[i]][1];
      rr[i][0] = sin;
      rr[i][1] = val;
    }

    ans = false;
    for(int i = 0; i < len; i ++)
      for(int j = i + 1; j < len; j ++)
        if(mul(0, i) == 1 && mul(i + 1, j) == 2 && mul(j + 1, len - 1) == 3)
          ans = true;


    printf("Case #%d: ", ct);
    if(ans) printf("YES\n");
    else printf("NO\n");
  }
  
  return 0;
}
