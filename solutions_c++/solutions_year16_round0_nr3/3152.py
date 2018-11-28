#include <bits/stdc++.h>
#define lli long long int
#define s(x) scanf("%lld", &x)
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define MAXX 1000009

using namespace std;

bool visit[MAXX];
vector<lli> primes;
lli arr[20];
lli brr[20];
int crr[50];
lli drr[20];

void sieve()
{
	lli i,j,k;

	for (i = 2; i < MAXX; ++i)
		visit[i] = true;

//	primes.pb(2);

	for (i = 2; i < MAXX; ++i) {
		if (visit[i] == true) {
			primes.pb(i);
		
			for (j = 2*i; j < MAXX; j += i) {
				visit[j] = false;
			}
		}
	}		
}

lli poe(lli a, lli b)
{
	if (b == 0)
		return 1;
	else if (b %2 == 0) {
		lli ans = poe(a, b/2);
		ans *= ans;

		return ans;
	} else {
		lli ans = poe(a, b-1);
		ans *= a;

		return ans;
	}
}

int main()
{
	lli N,K,n,tcase,i,j,k,l,m,zz,yy,ans,temp,pos,sz;
	s(i);
	s(N);
	s(K);
	i = 0;

	printf("Case #1: \n");
	sieve();

	sz = 0;

	for (i = (1LL << (N-1)) + 1; i < (1LL << (N)); i += 2) {
		for (j = 2; j < 11; ++j) {
			arr[j] = 0;
			brr[j] = 0;
			crr[j] = 1;
		}

		for (j = 0; j < N; ++j) {
			if (i&(1LL << j)) {
				for (k = 2; k < 11; ++k) {
					arr[k] = arr[k] + poe(k, j);
				}
				crr[j] = 1;
			} else {
				crr[j] = 0;
			}			
		}
		
		zz = 0;

		for (j = 2; j < 11; ++j) {
			yy = 0;
			for (k = 0; k < primes.size(); ++k) {
				if (arr[j] % primes[k] == 0) {
					yy = 1;
					brr[j] = primes[k];
					break;
				}
			}

			if (yy == 0) {
				zz = 1;
				break;
			}	
		}

		if (zz == 0) {
			++sz;
			
			for (j = N-1; j >= 0; --j) {
				printf("%d", crr[j]);
			}
			printf(" ");
			
/*			for (j = 2; j < 11; ++j) {
				cout << arr[j] << " ";
			}
			cout << " ";
*/
			for (j = 2; j < 11; ++j) {
				printf("%lld ", brr[j]);
			}
			printf("\n");
		}

		if (sz == K)
			break;			
	}

	return 0;
}
