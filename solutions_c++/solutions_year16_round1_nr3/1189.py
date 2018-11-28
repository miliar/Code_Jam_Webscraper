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

int N;
int a[10];
bool visited[10];
int ans;
int c[10];

void solve (int i, int n) {
	
	if (i == n) {
		bool fin = false;
		for_up (j, 0, n) {
			if (c[(j-1+n)%n]!=a[c[j]] && c[(j+1)%n]!=a[c[j]]) {
				fin = true;
				break;
			}
		}
		if (!fin) {
			ans = n;
		}
	}
	else {
		for_up (j, 0, N) {
			if (!visited[j]) {
				visited[j] = true;
				c[i] = j;
				solve(i+1, n);
				visited[j] = false;
			}
		}
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
	
    int T;
    scan(T);

    for_up (t, 1, T+1) {
		scan(N);
		
		for_up (i, 0, N) {
			scan(a[i]);
			a[i]--;
		}
		
		if (N == 1) {
			printf("Case #%d: %d\n", t, 1);
		}
		
		else {
			memset(visited, false, sizeof(visited));
			ans = 0;
			for_up (i, 1, N+1) {
				solve(0, i);
			}
			
			printf("Case #%d: %d\n", t, ans);
		}
	}
	
	fclose(stdin);
	fclose(stdout);

	return 0;
}

