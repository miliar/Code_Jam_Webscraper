#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>



#define forn(i,n) for(int i = 0; i < n; i++)
#define forn1(i,n) for(int i = 1; i <= n; i++)
#define forall(it, vec) for(vector<int>::iterator it = vec.begin(); it != vec.end(); it++)
#define ON(mask,i) (mask | (1L << (i)))
#define OFF(mask,i) (mask &  (-1 ^ (1L<<(i))) )
#define TOGGLE(mask,i) (mask ^ (1L << (i)))
#define isON(mask, i) (mask & (1L<<(i)))
#define mp make_pair
using namespace std;
typedef pair<int, int> pii;

int main(){
	int T, N;
  string s;
  cin >> T;
  forn1(t, T){
    int ans = 0, sum = 0;
    
    cin >> N >> s;
    
    forn(i, s.size()){
      if(sum + ans < i)
        ans = i - sum;
      sum += s[i] - '0';
    }
    printf("Case #%d: %d\n", t, ans);
  }
	return 0;
}
