#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<algorithm>
#include<vector>
#include<queue>
#include<list>
#include<string>
#include<set>
#include<map>
#include<iomanip>
#include<sstream>
#include<functional>
#include<climits>
#define eps 1e-9
const int mod = 1000000007;
using namespace std;

int t, L;
long long x;
char mp[205][205];
bool sign[205][205];
int main() {
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("problem3Small.txt", "w", stdout);
  mp['1']['1'] = '1';
  sign['1']['1'] = 1;
  mp['1']['i'] = 'i';
  sign['1']['i'] = 1;
  mp['1']['j'] = 'j';
  sign['1']['j'] = 1;
  mp['1']['k'] = 'k';
  sign['1']['k'] = 1;

  mp['i']['1'] = 'i';
  sign['i']['1'] = 1;
  mp['i']['i'] = '1';
  sign['i']['i'] = 0;
  mp['i']['j'] = 'k';
  sign['i']['j'] = 1;
  mp['i']['k'] = 'j';
  sign['i']['k'] = 0;

  mp['j']['1'] = 'j';
  sign['j']['1'] = 1;
  mp['j']['i'] = 'k';
  sign['j']['i'] = 0;
  mp['j']['j'] = '1';
  sign['j']['j'] = 0;
  mp['j']['k'] = 'i';
  sign['j']['k'] = 1;

  mp['k']['1'] = 'k';
  sign['k']['1'] = 1;
  mp['k']['i'] = 'j';
  sign['k']['i'] = 1;
  mp['k']['j'] = 'i';
  sign['k']['j'] = 0;
  mp['k']['k'] = '1';
  sign['k']['k'] = 0;

  scanf("%d", &t);
  for (int test = 1; test <= t; ++test) {
    char buff[10005];
    string s, ss;
    scanf("%d %lld", &L, &x);
    scanf("%s", buff);
    s = string(buff);
    if (x % 4 == 0) {
	printf("Case #%d: NO\n", test);
	continue;
    }
    for (int i = 0; i < x % 4; ++i) ss += s;
    bool b = true;
    char c = '1';
    for (int i = 0; i < ss.size(); ++i) {
	b = (b ^ sign[c][ss[i]]) ^ 1;
	c = mp[c][ss[i]];
    }
    if (b || c != '1') {
	printf("Case #%d: NO\n", test);
	continue;
    }
    //slow
    bool found = false;
    string str;
    for (int i = 0; i < x; ++i) str.append(s);
    char findi = '1';
    bool bi = 1;
    for (int i = 0; i < str.size(); ++i) {
	if (found) break;
	bi = (bi ^ sign[findi][str[i]]) ^ 1;
	findi = mp[findi][str[i]];
	if (bi && findi == 'i') {
	  char findj = '1';
	  bool bj = 1;
	  for (int j = i + 1; j < str.size(); ++j) {
	    bj = (bj ^ sign[findj][str[j]]) ^ 1;
	    findj = mp[findj][str[j]];
	    if (bj && findj == 'j') {
		char findk = '1';
		bool bk = 1;
		for (int k = j + 1; k < str.size(); ++k) {
		  bk = (bk ^ sign[findk][str[k]]) ^ 1;
		  findk = mp[findk][str[k]];
		}
		if (bk && findk == 'k') {
		  printf("Case #%d: YES\n", test);
		  found = true;
		  break;
		}
	    }
	  }
	}
    }
    if (found) continue;
    printf("Case #%d: NO\n", test);
  }
  return 0;
}

/*
for (int i = 0; i < L; ++i) {
bool b = q.second;
q = mp[q.first][s[i]];
if (!b) q.second ^= 1;
}
ss = s + s + s + s + s;
pair<char, bool> pat[5];
pat[0] = { '1', 1 };
pat[1] = q;
for (int i = 2; i <= 4; ++i) {
bool b = pat[i - 1].second;
pat[i] = mp[pat[i - 1].first][pat[i - 1].first];
if (!b) pat[i].second ^= 1;
}
vector<pair<char, bool> > pref(min(5 *1LL* L, x*L)), suff(min(5 * 1LL * L, x* L));
vector<pair<int, long long> > is, ks;
pref[0] = { '1', 1 };
for (int i = 0; i < 5 * L - 2; ++i) {
bool b = pref[i].second;
pref[i] = mp[pref[i].first][ss[i]];
if (!b) pref[i].second ^= 1;
if (pref[i].second && pref[i].first == 'i') {
is.push_back({ i % L, i / L });
}
}
suff[5 * L - 1] = { '1', 1 };
for (int i = 5 * L - 1; i >= 1; --i) {
bool b = suff[i].second;
suff[i] = mp[ss[i]][suff[i].first];
if (!b) suff[i].second ^= 1;
if (suff[i].second && suff[i].first == 'k') {
ks.push_back({ i%L, x - (4 - i / L) });
}
}
bool found = false;
for (int i = 0; i < is.size(); ++i) {
if (found) break;
for (int j = 0; j < ks.size(); ++j) {
if (is[i].second < ks[j].second) {
int p = ks[j].second - is[i].second - 1;
p %= 5;
pair<char, bool> cur = pat[p];
pair<char, bool> left = suff[is[i].first];
pair<char, bool> right = pref[ks[j].first];
bool b = cur.second;
cur = mp[left.first][cur.first];
if (!b) cur.second ^= 1;
if (!left.second) cur.second ^= 1;
b = cur.second;
cur = mp[cur.first][right.first];
if (!cur.second) cur.second ^= 1;
if (!right.second) cur.second ^= 1;
if (cur.second && cur.first == 'j') {
printf("Case %d: YES\n", test);
found = true;
break;
}
}
}
}
if (found) continue;
printf("Case %d: NO\n", test);
*/