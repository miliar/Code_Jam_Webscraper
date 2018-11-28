#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define ALL(x) x.begin(),x.end()
long long powers[15][20];

void comp_pow()
{
	for(int i = 2 ; i <=10 ; i++){
		powers[i][0] = 1;
		for(int j = 1 ; j <= 17 ; j++){
			powers[i][j] = powers[i][j-1]*i;
		}
	}
}


ll isPrime(ll n)
{
	if(n%2 == 0)
	{
		if(n==2)
			return 0;
		else
			return 2;
	}
	ll kk = sqrt(n);
	for(int i = 3 ; i <= kk ; i+=2)
		if(n%i == 0)
			return i;
	return 0;
}




void bitmask(int n, int lenftw)
{
	int counter = 0;
	ll ansm[12] = {0};
	for(ll i = 0 ; i < powers[2][n-2] ; i++){
		string s = "1000000000000001";
		ll numcur[12] = {0};
		for(int j = 0 ; j <= n-3;j++){
			if(powers[2][j] & i){
				s[n-2 - j] = '1';
				for(int k = 2 ; k <= 10 ; k++){
					numcur[k] += powers[k][j+1];
				}
			}
		}
		int ctr = 0;
		for(int k = 2 ; k <= 10 ; k++){
			numcur[k] += 1 + powers[k][n-1];
			ll kpp;
			if(kpp = isPrime(numcur[k]))
				ansm[ctr++] = kpp;
			else break;
		}
		if(ctr == 9){
			counter++;
			cout << s <<" ";
			for(int cc = 0 ; cc < 9 ; cc++)
				printf("%lld ",ansm[cc]);
			printf("\n");
			if(counter == lenftw)
				break;
		}
	}
}




int main(int argc, char const *argv[])
{
	freopen("outs2.txt","w",stdout);
	freopen("ins.txt","r",stdin);
	int t;
	scanf("%d",&t);
	comp_pow();
	for(int ct = 1 ;ct<=t;ct++){
		printf("Case #%d:\n" , ct);
		int n,j;
		scanf("%d %d",&n,&j);
		bitmask(n,j);
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
