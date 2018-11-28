#include<bits/stdc++.h>
using namespace std;

typedef long long int lli;

#define MOD 1000000007

#define scan(x) scanf("%d", &x)
#define print(x) printf("%d\n", x)

#define scan_lli(x) scanf("%lld", &x)
#define print_lli(x) printf("%lld\n", x)

#define scanc(x) scanf("%c", &x)
#define printc(x) printf("%c", x)

#define scans(x) scanf("%s", x)
#define prints(x) fscanf(out, "%s\n", x)

#define for_up(v, s, e) for (int v=s; v<e; v++)
#define for_down(v, s, e) for (int v=s; v>=e; v--)

#define vi vector<int>
#define pii pair<int, int>
#define vpii vector< pair<int, int> >

#define pb push_back
#define mp make_pair

#define fs first
#define sc second

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
	
    int T;
    scan(T);

    for_up (t, 1, T+1) {
    	int n;
    	scan(n);
    	
    	int cnt[2501];
    	memset(cnt, 0, sizeof(cnt));
    	
    	for_up (i, 0, 2*n-1) {
    		for_up (j, 0, n) {
    			int a;
    			scan(a);
    			
    			cnt[a]++;
    		}
    	}
    	
    	vi ans;
    	for_up (i, 1, 2501) {
    		if (cnt[i] & 1) {
    			ans.pb(i);
    		}
    	}
    	
		printf("Case #%d: ", t);
		for_up (i, 0, ans.size()) {
			printf("%d ", ans[i]);
		}
		printf("\n");
	}
	
	fclose(stdin);
	fclose(stdout);

	return 0;
}

