#include <bits/stdc++.h>

using namespace std;

using LL = long long;
using ULL = unsigned long long;
#define vi vector<int>
#define vs vector<string>
#define vl vector<LL>
#define pb push_back
#define endl "\n"


int cnt[26];

bool check(const string& s) {
   int cnt1[26];
   memset(cnt1, 0, sizeof(cnt1));
   for (auto it : s) {
      cnt1[it - 'A'] ++;
   }

   for (int i=0;i<26;i++) {
      if (cnt1[i] > cnt[i])
         return false;
   }
   for (int i=0;i<26;i++) {
      cnt[i] -= cnt1[i];
   }

   return true;
}

string nums[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
string solve() {
   string s;
   cin >> s;
   size_t sz = s.size();
   memset(cnt, 0, sizeof(cnt));
   for (size_t i = 0;i<sz;i++) {
      cnt[s[i] - 'A'] ++;
   }
   vi m = { 0,2,6,7,8,5,3,4,9,1};
   assert(m.size() == 10);

   vi v;
   for(int i=0;i<10;i++) {
      while (check(nums[m[i]]))
         v.pb(m[i]);
   }


   sort(v.begin(), v.end());
   string ret(v.size(), '0');
   //cout << ret << endl;
   for (size_t i=0;i<v.size();i++) {
      ret[i] = '0' + v[i];
   }
   //cout << ret.size() << v.size() << endl;
   assert(ret.size() == v.size());

   for (int i=0;i<26;i++) {
      assert(cnt[i] == 0);
   }
   return ret;
}

int main()
{
	ios_base::sync_with_stdio(false);
   ULL T = 0;
   cin >> T;
   for (ULL i = 1; i <= T; ++i) {
      cout << "Case #" << i << ": " << solve() << endl;
   }

	return 0;
}
