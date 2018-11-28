#include<bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define sl(n) scanf("%lld",&n);
#define ss(n) scanf("%s",n);
#define fr(i, n) for(i = 0; i < n; i++)
#define ms(i, n) memset(i, n, sizeof(i))
typedef long long LL; 
using namespace std;
int main () {
	//freopen ("input.in","r",stdin);
	//freopen ("output.txt","w",stdout);
	int t, n, used[1003], i, j, co, k, nao1, nao2, u, l;
	double a[1003], b[1003];
	si(t);
	u = t;
	while (t--) {
		ms(used, 0);
		si(n);
		fr(i, n) {
			scanf("%lf", &a[i]);
		}
		fr(i, n) {
			scanf("%lf", &b[i]);
		}
		sort(a, a + n);
		sort(b, b + n);
		//fr(i, n) printf("%.5lf ", a[i]);
		//cout<<endl;
		//fr(i, n) printf("%.5lf ", b[i]);
		//cout<<endl;
		i = 0;
		j = 0;
		k = 0;
		l = 0;
		nao1 = 0;
		while (i < n && j < n) {
			if(a[i] > b[j]) {
				i++;j++;
				nao1++;
			} else {
				i++;
			}
		}
		i = 0;
		j = 0;
		k = 0;
		l = 0;
		nao2 = 0;
		while (i < n && j < n) {
			if(a[i] < b[j]) {
				i++;j++;
			} else {
				nao2++;
				j++;
			}
		}
		printf("Case #%d: ", u - t);
		printf("%d %d\n", nao1, nao2);
	}
	return 0;
}

