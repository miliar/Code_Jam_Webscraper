#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<functional>
using namespace std;
double arr1[1005], arr2[1005];
int N;
void solve(){
    int ans[2] = {0, 0};
    sort(arr1, arr1+N);
    sort(arr2, arr2+N);
    for (int round = 0; round < 2; round++){
        for (int i=0, j=0; i<N && j<N; i++){
            bool flag = true;
            for (; j<N && flag; j++){
                if (arr1[i] < arr2[j]){
                    ans[round]++;
                    flag = false;
                }
            }
        }
        for (int i=0; i<N; i++)
            swap(arr1[i], arr2[i]);
    }
    printf("%d %d", ans[1], N - ans[0]);
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
        scanf("%d", &N);
        for (int i=0; i<N; i++)
            scanf("%lf", &arr1[i]);
        for (int i=0; i<N; i++)
            scanf("%lf", &arr2[i]);
		printf("Case #%d: ", t);
        solve();
        putchar('\n');
	}

}
