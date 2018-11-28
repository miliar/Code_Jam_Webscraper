#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
using namespace std;

typedef pair<int, int> P;
#define INF (1LL << 30)
typedef long long Int;

int n, k;
int ans[1080];
int mi[1080];
int ma[1080];
int pos[1080];
int sum[1080];

int solve(){
  cin >> n >> k;
  fill(ans, ans + n, 0);
  fill(mi, mi + n, 0);
  fill(ma, ma + n, 0);
  for(int i = 0;i < n - k + 1;i++){
    cin >> sum[i];
    if(i == 0)continue;
    ans[i + k - 1] = ans[i - 1] + sum[i] - sum[i-1];
    mi[i % k] = min(mi[i % k], ans[i + k - 1]);
    ma[i % k] = max(ma[i % k], ans[i + k - 1]);
  }
  int tmp = 0;
  vector<P> nums;
  for(int i = 0;i < k;i++){
    pos[i] = -mi[i];
    tmp += pos[i];
    nums.push_back(P(ma[i] - mi[i], i));
  }
  tmp = sum[0] - tmp;
  tmp %= k;
  if(tmp < 0)tmp += k;
  sort(nums.begin(), nums.end());
  int pp = 0, cnt = 0;
  int lim = pos[nums[k-1].second] + ma[nums[k-1].second];
  for(int i = 0;i < tmp;i++){
    int now = nums[pp].second;
    if(pos[now] + ma[now] < lim || cnt == 0)pos[now]++, cnt++;
    else pp++, cnt = 0;
  }
  int mma = -INF, mmi = INF;
  for(int i = 0;i < k;i++){
    mma = max(mma, pos[i] + ma[i]);
    mmi = min(mmi, pos[i] + mi[i]);
  }
  cout << mma - mmi << endl;
  return 0;
}

int main(){
  Int T;
  cin >> T;
  for(Int t = 1;t <= T;t++){
    cout << "Case #" << t << ": ";
    solve();
  }
  return 0;
}
