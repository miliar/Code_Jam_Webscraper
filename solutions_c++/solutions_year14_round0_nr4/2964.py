#include <iostream>
#include <cstdio> 
#include <algorithm>
#include <vector>
#include <cstring>
#define maxn 1005
#define inf 0x3fffffff
#define exp 1e-8
#define DBL double
using namespace std;

DBL a[maxn], b[maxn];
int n;

int main(){
	freopen("D-large.in","r",stdin); 
	freopen("out.txt","w",stdout); 
	int T;
	cin >> T;
	int cas = 1;
	while (T--){
		scanf("%d", &n);
		for(int i=0; i<n; i++)
			cin >> a[i];
		for(int i=0; i<n; i++)
			cin >> b[i];
		sort(a, a+n);
		sort(b, b+n);
		int cnt1=0, cnt2=0;
		int h=0, t=n-1;
		for(int i=0; i<n; i++){
			if(a[i]<b[h])
				t--;
			else
				cnt1++, h++;
		}	
		h=0, t=n-1;
		for(int i=n-1; i>=0; i--){
			if(a[i]<b[t])
				t--;
			else
				cnt2++, h++;
		}
		printf("Case #%d: %d %d\n", cas++, cnt1, cnt2);
	}
	return 0;
}