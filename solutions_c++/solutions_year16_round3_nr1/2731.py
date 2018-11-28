#include<bits/stdc++.h>
using namespace std;

typedef long long int lli;

#define MOD 1000000007

#define scan(x) scanf("%d", &x)
#define scan2(x, y) scanf("%d %d", &x, &y)
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
	//freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	
    int T;
    scan(T);

    for_up (t, 1, T+1) {
		int n;
		scan(n);
		
		int total = 0;
		set< pair<int, char> > s;
		for_up (i, 0, n) {
			int a;
			scan(a);
			
			if (a > 0) {
				s.insert(mp(a, i+'A'));
			}
			total += a;
		}
		
		printf("Case #%d: ", t);
		while (s.size() > 0) {
			printf("%c", s.rbegin()->sc);
			if (total % 2 == 1) {
				printf(" ");
			}
			total--;
			pair<int, char> p = *(s.rbegin());
			s.erase(p);
			if (p.fs > 1) {
				s.insert(mp(p.fs-1, p.sc));
			}
		}
		printf("\n");
	}
	
	fclose(stdin);
	fclose(stdout);

	return 0;
}

