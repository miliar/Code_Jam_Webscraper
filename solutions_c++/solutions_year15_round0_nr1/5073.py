#define  _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h> 
using namespace std;
 
#define INPUT "C:\\Users\\Mahmoud Sayed\\Desktop\\New folder\\in.txt"
#define OUTPUT "C:\\Users\\Mahmoud Sayed\\Desktop\\New folder\\out.txt"
#define SZ(A) (int)A.size()
#define fr first 
#define pb push_back
#define sc second
#define mp make_pair
#define unordered_map _map
#define unordered_set _set
#define priority_queue pr_q
 
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<int> vi;
const int MAX = 100001; 
int  main() {
#ifndef ONLINE_JUDGE
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);
#endif
  int cs = 1, t, n; 
  scanf("%d", &t); 
  char st[1010]; 
  while(t--) {
    scanf("%d %s", &n, st); 
    int cur = (st[0]-'0'); 
    int needed = 0; 
    for(int i = 1; i <= n; i++) {
      if(cur < i) needed += (i - cur), cur = i;  
      cur += (st[i]-'0'); 
    }
    printf("Case #%d: %d\n", cs++, needed);
  }
}