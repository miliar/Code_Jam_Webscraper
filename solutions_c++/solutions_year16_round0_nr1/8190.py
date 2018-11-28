#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<cmath>
#include<vector>
using namespace std;
#define PB push_back
#define PPB pop_back
#define MP make_pair
#define LL long long
#define fs first
#define sc second
#define pii pair<int,int>
#define pll pair<LL,LL>
#define ppii pair<int, pii>
#define BIG 2000000000

int tc,bil,cnt,temp;
bool cek[10];

void parse(int x) {
  while (x>0) {
    if (!cek[x%10]) --cnt;
    cek[x%10] = true;
    x /= 10;
  }
}

int main() {
  scanf("%d",&tc);
  for (int z=1;z<=tc;++z) {
    scanf("%d",&bil);
    cnt = 10;
    memset(cek,0,sizeof(cek));
    for (int i=1;i<=100;++i) {
      temp = bil * i;
      parse(temp);
      if (cnt == 0) break;
    }
    if (cnt == 0) {
      printf("Case #%d: %d\n",z,temp);
    } else {
      printf("Case #%d: INSOMNIA\n",z);
    }
  }
	return 0;
}
