// Author: Harhro94 [Harutyunyan Hrayr]
#pragma comment(linker, "/STACK:66777216")
#define _CRT_SECURE_NO_WARNINGS
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <bitset>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include <vector>
using namespace std;

typedef long long LL;
typedef long double LD;
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()

const int N = 10;
int n, m, pos[N];
string st[N];

int M[100];

struct node
{
   node* nxt[26];

   node()
   {
      memset(nxt, 0, sizeof nxt);
   }
} *root;
typedef node* pnode;
int total;

void add(string &s)
{
   if (!root)
   {
      root = new node();
      ++total;
   }
   pnode T = root;
   for (int i = 0; i < sz(s); ++i)
   {
      int d = s[i] - 'A';
      if (T->nxt[d] == 0)
      {
         T->nxt[d] = new node;
         ++total;
      }
      T = T->nxt[d];
   }
}

void init(pnode T)
{
   if (!T) return;
   for (int i = 0; i < 26; ++i)
      init(T->nxt[i]);
   delete T;
}

void rec(int p)
{
   if (p == m)
   {
      vector<int> cnt(n, 0);
      for (int i = 0; i < m; ++i)
         cnt[pos[i]]++;
      for (int i = 0; i < n; ++i)
         if (cnt[i] == 0) return;

      int cur = 0;
      for (int i = 0; i < n; ++i)
      {
         total = 0;
         init(root);
         root = NULL;
         for (int j = 0; j < m; ++j)
            if (pos[j] == i) add(st[j]);
         cur += total;
      }
      M[cur]++;
      return;
   }
   for (int i = 0; i < n; ++i)
   {
      pos[p] = i;
      rec(p + 1);
   }
}

int main()
{
#ifdef harhro94
   //testGen();
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
#else
#define task "angle"
   //freopen(task".in", "r", stdin);
   //freopen(task".out", "w", stdout);
#endif

   int T;
   scanf("%d", &T);
   for (int test = 1; test <= T; ++test)
   {
      cerr << test << endl;
      printf("Case #%d: ", test);

      cin >> m >> n;
      memset(M, 0, sizeof M);
      for (int i = 0; i < m; ++i) cin >> st[i];
      rec(0);
      int pos;
      for (int i = 0; i < 100; ++i)
         if (M[i]) pos = i;
      cout << pos << " " << M[pos] << endl;
   }

#ifdef harhro94
   cerr << fixed << setprecision(3) << "\nExecution time = " << clock() / 1000.0 << "s\n";
#endif
   return 0;
}