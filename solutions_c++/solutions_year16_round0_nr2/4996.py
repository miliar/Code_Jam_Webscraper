#include <bits/stdc++.h>
using namespace std;

#define file "file"
#define mp make_pair
#define pb push_back
#define xx real()
#define yy imag()
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef complex<double> point;

#define DEBUG 0
#define dout if(DEBUG) cout

const int MAXN = 1e4 + 5;

char s[MAXN];
char s2[MAXN];
int cnt[MAXN], top;

void solve(){
    scanf("%s", s);
    int n = strlen(s);
    top = 0;
    int cur = 1;
    for(int i = 1; i < n; i++){
        if(s[i] != s[i - 1]){
            s2[top] = s[i - 1];
            cnt[top] = cur;
            top++;
            cur = 1;
        }
        else{
            cur++;
        }
    }
    s2[top] = s[n - 1];
    cnt[top] = cur;
    top++;
    int ans = (s2[top - 1] == '+' ? top - 1 : top);
    printf("%d\n", ans);
}

int main()
{
	#ifdef NASTYA
    assert(freopen("input.txt","r",stdin));
    assert(freopen("output.txt","w",stdout));
    #else
    //assert(freopen(file".in","r",stdin)); assert(freopen(file".out","w",stdout));
    #endif
	int t = 1;
	cin >> t;
	int cs = 1;
	while(t--){
        printf("Case #%d: ", cs++);
		solve();
	}
	return 0;
}
