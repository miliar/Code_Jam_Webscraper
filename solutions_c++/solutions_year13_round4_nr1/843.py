#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1000 + 1;
const int MODU = 1000002013;
int N, M, s[MAXN], t[MAXN], num[MAXN];
pair<int, int> seg[MAXN + MAXN];
long long height[MAXN + MAXN];
int htot;
int top;

int modAdd(int ans, long long s, long long num) {
  int tmp = s;
  //printf ("%d %d\n", tmp, (int) num);

  s = s % MODU;
  s = s * num;
  s = s % MODU;
  if (s < 0) s += MODU;
  return (ans + s) % MODU;
}

int Scan (int p, long long sum, int ans)
{
  int ret = ans;
  long long h = sum, tmp;
  for (int i = p + 1; i < top; i++) {
    if (seg[i].second > 0) {
      if (sum - seg[i].second <= h) {
        tmp = (long long)(2 * N + 1 - (seg[i].first - seg[p].first)) * (seg[i].first - seg[p].first) / 2;
        printf ("extract %d %d\n", seg[i].first, seg[i].second);
        ret = modAdd (ret, -tmp, h); 
      }
    }
    sum -= seg[i].second;
    if (sum < h) h = sum;
    if (sum == 0) return ret;
  }
}

int Solve()
{
  int ans = 0;
  long long tmp;
  for (int i = 0; i < M; i++) {
    tmp = (long long)(2 * N + 1 - (t[i] - s[i])) * (t[i] - s[i]) / 2; 
    ans = modAdd (ans, tmp, num[i]);
    seg[i * 2] = make_pair(s[i], -num[i]);
    seg[i * 2 + 1] = make_pair(t[i], num[i]);
  }

  sort (seg, seg + M + M);
  top = 1;
  for (int i = 1; i < M + M; i++) {
    if (seg[i].first != seg[top - 1].first) {
      seg[top ++] = seg[i];
    } else {
      seg[top - 1].second += seg[i].second;
    }
  }
  //printf ("%d\n", top);
  //for (int i = 0; i < top; i++) printf ("%d %d\n", seg[i].first, seg[i].second);
  int bak = top;
  top = 0;
  for (int i = 0; i < bak; i++) {
    if (seg[i].second != 0) seg[top ++] = seg[i];
  }
  seg[top] = make_pair (0, 1000000000);
  //printf ("%d\n", top);
  //for (int i = 0; i < top; i++) printf ("%d %d\n", seg[i].first, seg[i].second);


  long long sum = 0;
  htot = 0;
  for (int i = 0; i < top; i++) {
    sum -= seg[i].second;
    height[i] = sum;
  }
  sort (height, height + top);
  htot = unique (height, height + top) - height; 
  //printf ("htot %d\n", htot);
  //for (int i = 0; i < htot; i++) printf ("%d ", (int)height[i]);
  //printf ("\n");

  for (int h = 1; h < htot; h++) {
    sum = 0;
    int left = -1;
    for (int i = 0; i < top; i++) {
      sum -= seg[i].second;
      if (seg[i].second < 0) {
        if (sum >= height[h] && left == -1) left = seg[i].first;
      } else {
        if (sum < height[h] && left > -1) {
          tmp = (long long)(2 * N + 1 - (seg[i].first - left)) * (seg[i].first - left) / 2;
          //printf ("extract %d %d\n", left, seg[i].first);
          ans = modAdd (ans, -tmp, height[h] - height[h - 1]); 
          left = -1;
        }
      }
    }
  }

  return ans;
}

int main ()
{
  freopen ("in.txt", "r", stdin);
  freopen ("ou.txt", "w", stdout);

  int T;
  scanf ("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf ("Case #%d: ", i);
    scanf ("%d%d", &N, &M);
    for (int j = 0; j < M; j++) {
      scanf ("%d%d%d", s + j, t + j, num + j);
    }
    printf ("%d\n", Solve());
  }
}

