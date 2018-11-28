/*pranjuldb*/
#include <bits/stdc++.h>
#define pri(a) printf("%d",a)
#define prl(a) printf("%lld",a)
#define prd(a) printf("%lf",a)
#define nl printf("\n")
#define sp printf(" ")
#define prs(str) printf("%s", str)
#define pb push_back
#define mem(a,b) memset(a, b, sizeof(a))
#define vi vector < int >
#define vl vector < long long int >
#define pll pair<long long, long long>
#define pii pair < int , int >
#define ll long long
#define rep(i,j,k) for(i = j; i < k; i++)
#define nrep(i,j,k) for(i = j; i >= k; i--)
#define scs(str) scanf("%s", str)
#define sci(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define scd(a) scanf("%lf", &a)
#define fr first
#define se second
#define mp make_pair

using namespace std;

int arr[10001];

int bsearch(int d, int m, int mid)
{
    int idx = 0;
	int flag[1001];
	int i;
	rep(i, 0, d) {
		if(arr[i] > mid) {
			flag[idx] = arr[i] - mid;
			idx++;
		}
	}
    rep(i, 0, idx) {
		if(flag[i] > 0 && m <= 0) {
			return 0;
		}
		if(flag[i] <= mid) {
			m--;
		} else {
			flag[i] -= mid;
			m--;
			i--;
		}
	}
	return 1;
}

int solve()
{
        int anss = 19999999;
		int d, i;
		sci(d);
		rep(i, 0, d) sci(arr[i]);
		rep(i, 0, 1001) {
			int low = 1;
			int high = 1000;
			while(low < high) {
				int mid = low + (high-low)/2;
				int val = bsearch(d, i, mid);
				if(val == 1) {
					high = mid;
				}else {
					low =  mid+1;
				}
			}
			if(anss > i + low ) {
				anss = i + low;
			}
		}
		return anss;
}

int main()
{
	//freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
	int cases, tt, i;
    sci(cases);
	rep(tt, 1, cases + 1) {

		printf("Case #%d: %d\n", tt, solve());
	}
	return 0;
}
