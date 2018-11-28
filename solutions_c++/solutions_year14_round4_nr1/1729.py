#include <cstdio>
#include <algorithm>

using namespace std;

void sol(int cse)
{
	int n;
	int arr[20000];
	int x;
	int i,j,k;
	int ans = 0;
	scanf("%d %d",&n,&x);
	for(i=0;i<n;i++) scanf("%d",arr+i);
	sort(arr,arr+n);
	for(i=0,j=n-1;i<j;) {
		if(arr[i]+arr[j] <= x) {
			ans++;
			i++;
			j--;
		} else {
			ans++;
			j--;
		}
	}
	if(i==j) ans++;
	printf("Case #%d: %d\n",cse,ans);
}

int main()
{
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;sol(i), i++);
	return 0;
}