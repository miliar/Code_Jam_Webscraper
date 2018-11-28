#include <bits/stdc++.h>
using namespace std;

int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int tst;
	cin >> tst;

	for (int t = 1; t <= tst; ++t)
	{
		int n;
		cin >> n;
		printf("Case #%d: ", t);
		if(n == 0){
			printf("INSOMNIA\n");
			continue;
		}
		set<int> vis;
		long long i;
		for (i = n; ; i += n)
		{
			long long num = i;
			while(num){
				vis.insert(num%10);
				num /= 10;
			}
			if(vis.size() == 10) break;
		}
		printf("%lld\n",i);
	}

}
