# include <stdio.h>
# include <string.h>
# include <iostream>
# include <algorithm>
//#define LOCAL
using namespace std;
typedef long long ll;
int t[10],res;

int main(){
	#ifdef LOCAL
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	#endif
	int n;
	scanf("%d",&n);
	for(int times=1;times<=n;times++){
		memset(t,0,sizeof(t));
		res = 10;
		ll s,a;
		cin >> a;
		printf("Case #%d: ",times);
		if (a == 0){
			puts("INSOMNIA");
			continue;
		}
		s = a;
		for(int i=1;;i++){
			ll ss = s;
			while(ss>0){
				int tt = ss%10;
				ss/=10;
				if (!t[tt]) {
					res --;
					t[tt] = 1;
				}
			}
			if (res == 0) break;
			s += a;
		}
		cout << s << endl;
	}
}