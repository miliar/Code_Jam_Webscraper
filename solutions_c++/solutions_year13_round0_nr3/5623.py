/* Paras Narang */
#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <deque>
#include <bitset>
#include <cmath>
#include <set>
#include <sstream>

using namespace std;

#define oo 0x7F7F7F7F
#define LET(x,a)     __typeof(a) x(a)
#define EACH(it,v)   for(LET(it,v.begin());it!=v.end();++it)
#define REP(i,n)     for(__typeof(n) i(0); i<n; i++)
#define ALL(x)       (x).begin(), (x).end()
#define gint(t)      scanf("%d", &t);
#define pint(t)      printf("%d\n", t);
#define pb           push_back
#define mp           make_pair

typedef long long int   ll;
typedef unsigned long long int ull;
typedef unsigned int    uint;
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector<vi>      vii;
typedef vector<pii>     vpii;

int pal[1000], ctr = 0;
int is_palindrome(unsigned long orig)
{
  unsigned long reversed = 0, n = orig;

  while (n > 0)
  {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }

  return orig == reversed;
}

void preprocess(){
    for(int i = 1; i <= 1000; i++){
        if(is_palindrome(i)){
            int tmp = i * i;
            if(is_palindrome(tmp)){
                pal[ctr] = tmp;
                ctr++;
            }
        }
    }
}

int main(){
    preprocess();
    int T; gint(T);
    REP(ti, T){
        int a, b, res = 0; cin >> a >> b;
        REP(i, 1000){
            while(pal[i] < a) i++;
            if(pal[i] >= a && pal[i] <= b) res++;
            if(pal[i] > b) break;
        }
        printf("Case #%d: %d\n", ti+1, res);
    }
    return 0;
}
