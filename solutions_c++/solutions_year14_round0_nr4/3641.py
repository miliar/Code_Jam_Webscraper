#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <list>
#include <iostream>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;

int main()
{
  freopen("D-large.in","r",stdin);
  freopen("D-saida-large.out","w",stdout);
  int tt = 1;
  int T;
  scanf("%d", &T);
  while (T--) {
    int N;
    scanf("%d", &N);
    vector < double > naomi, ken;
    for (int i = 0; i < N; i++) {
      double vf;
      scanf("%lf", &vf);
      naomi.pb(vf);
    }
    for (int i = 0; i < N; i++) {
      double vf;
      scanf("%lf", &vf);
      ken.pb(vf);
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    int war, dec;
    war = dec = 0;
    int ini_ken = 0, fim_ken = N - 1;
    for (int i = N - 1; i >= 0; i--) {
      if (naomi[i] > ken[fim_ken]) {
	war++;
	ini_ken++;
      } else {
	fim_ken--;
      }
    }
    ini_ken = 0, fim_ken = N - 1;
    for (int i = 0; i < N; i++) {
      if (naomi[i] > ken[ini_ken]) {
	ini_ken++;
	dec++;
      } else if (naomi[i] > ken[fim_ken]) {
	fim_ken--;
	dec++;
      } else  {
	fim_ken--;
      }
    }
    printf("Case #%d: %d %d\n", tt++, dec, war);
  }
  return 0;
}
