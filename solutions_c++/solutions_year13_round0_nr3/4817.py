#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for (int tc=1; tc<=t; tc++) {
		int ans=0;
		int a,b;
		scanf("%d %d",&a,&b);
		for (int i=1; i*i<=b; i++) {
			if (i*i >= a) {
				char buffer[100];
				sprintf(buffer,"%d",i);
				string t1 = buffer;
				string t2 = buffer;
				reverse(t2.begin(),t2.end());
				if (t1 == t2) {
					sprintf(buffer,"%d",i*i);
					t1 = buffer;
					t2 = buffer;
					reverse(t2.begin(),t2.end());
					if (t1==t2) ans++;
				}

			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
