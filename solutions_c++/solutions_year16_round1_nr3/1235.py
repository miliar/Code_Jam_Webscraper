#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

void print(int arr[], int n)
{
	int i;
	for(i = 0;i < n;i++)
		printf("%d ", arr[i]);
	printf("\n");
}

int check(int all[], int bff[], int n)
{
	int i;
	//print(all, n);
	for(i = 1;i < n-1;i++)
		if(!(all[i-1] == bff[all[i]] || all[i+1] == bff[all[i]]))
			return 0;
	if(!(all[n-1] == bff[all[0]] || all[1] == bff[all[0]]))
		return 0;
	if(!(all[0] == bff[all[n-1]] || all[n-2] == bff[all[n-1]]))
		return 0;
	return 1;
}

int main()
{
	int t, caseNum = 1, i, n, bff[1005], ans, now, j;
	int all[10];
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		for(i = 0;i < n;i++){
			scanf("%d", &bff[i]);
			bff[i]--;
		}
		ans = 2;
		for(i = 3;i <= n;i++){
			for(j = 0;j < n;j++)
				all[j] = j;
			now = 0;
			do{
				now = check(all, bff, i);
				if(now == 1){
					//print(all, i);
					break;
				}
			}while(next_permutation(all, all + n));
			if(i > ans && now == 1){
				ans = i;
			}
		}
		printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}
