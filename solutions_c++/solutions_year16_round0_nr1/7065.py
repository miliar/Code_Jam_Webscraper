#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("codejam.txt","r",stdin);
	freopen("codejamout1.txt","w",stdout);
	int t;
	cin >> t;
	for(int tst = 1; tst <= t; tst++){
		long long int n,x;
		printf("Case #%d: ",tst);
		cin >> n;
		if(n == 0){
			puts("INSOMNIA");
		}else{
			int cnt = 10;
			long long int i = 1;
			bool flag[11];
			memset(flag, false, sizeof(flag));
			while(cnt > 0){
				x = i*n;
				bool b = false;
				while(x){
					if(flag[x%10] == false){
						cnt--;
						flag[x%10] = true;
						if(cnt == 0) {
							printf("%lld\n",i*n);
							b= true;
						}
					}
					if(b == true) break;
					x = x/10;
				}
				i++;
			}
		}
	}
	return 0;
}

