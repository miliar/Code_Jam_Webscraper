#include <bits/stdc++.h>
using namespace std;

char SS[2000 + 10];
char rs[2000 + 10];
int ii = 0;
multiset<char> st;
vector<pair<char,char>> vp;
map<char,string> mp;
int cc = 0;

bool has(char c) {
   return st.find(c) != st.end();
}

void rem(char c) {
   for(char c0 : mp[c]) {
      st.erase(st.find(c0));
   }
}

void ff() {
   if(st.size() == 0) return;
   for(auto p : vp) {
      if(has(p.first)) {
         rem(p.second);
         rs[ii++] = p.second;
         ff();
         return;
      }
   }
   rem('9');
   rs[ii++] = '9';
   ff();
}

void f() {
   ii = 0;
   memset(rs, 0, sizeof(rs));
   st.clear();
   for(int i = 0; SS[i]; i++) {
      st.insert(SS[i]);
   }
   cc = st.size();
   ff();
   sort(rs, rs + ii);
}

void init() {
   vp.emplace_back('Z', '0');
   vp.emplace_back('W', '2');
   vp.emplace_back('U', '4');
   vp.emplace_back('X', '6');
   vp.emplace_back('G', '8');
   vp.emplace_back('O', '1');
   vp.emplace_back('H', '3');
   vp.emplace_back('F', '5');
   vp.emplace_back('S', '7');
   mp['0'] = "ZERO";
   mp['1'] = "ONE";
   mp['2'] = "TWO";
   mp['3'] = "THREE";
   mp['4'] = "FOUR";
   mp['5'] = "FIVE";
   mp['6'] = "SIX";
   mp['7'] = "SEVEN";
   mp['8'] = "EIGHT";
   mp['9'] = "NINE";
}

int main() {
   freopen("inp.txt", "r", stdin);
   freopen("out.txt", "w", stdout);
   init();
   int T; scanf("%d", &T);
   for(int cs = 1; cs <= T; cs++) {
      scanf("%s", SS);
      f();
      printf("Case #%d: %s\n", cs, rs);
   }
}