#include <bits/stdc++.h>
using namespace std;

int n;
int ok[15];

int main() {
	freopen("input.inp","r",stdin);
	freopen("output.out","w",stdout);
	int test;
	cin>>test;
	for(int dem=1;dem<=test;dem++) {
		printf("Case #%i: ",dem);
		cin>>n;
		memset(ok,0,sizeof(ok));
		if (n==0) {
			cout<<"INSOMNIA\n";
			continue;
		}
		long long m=0;
		while (true) {
			m+=n;
			long long tam=m;
			while (tam) {
				if (!ok[tam%10]) {
					ok[tam%10]=1;
					++ok[10];
				}
				tam/=10;
			}
			if (ok[10]==10) {
				cout<<m<<endl;
				break;
			}
		}
	}
	fclose(stdin);
	fclose(stdout);
}