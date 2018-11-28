#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define ALL(x) x.begin(),x.end()

int main(int argc, char const *argv[])
{
	freopen("outs.txt","w",stdout);
	freopen("ins.txt","r",stdin);
	int t;
	scanf("%d",&t);
	for(int ct = 1 ;ct<=t;ct++){
		printf("Case #%d: ",ct);
		long long n;
		scanf("%lld",&n);
		if(n==0){
			cout << "INSOMNIA\n";
			continue;
		}
		ll arr[10] = {0};
		for(long long i = n ; ; i+=n){
			ll j = i;
			while(j){
				arr[j%10]++;
				j/=10;
			}
			int k;
			for(k = 0 ; k <= 9 ; k++)
				if(arr[k]) continue;
				else break;
			if(k == 10){
				printf("%lld\n",i);
				break;
			}
		}
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
