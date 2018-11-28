#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<vector>
using namespace std;
int arr1[4][4], arr2[4][4];
int ans1, ans2;
void solve(){
    int flag = 0;
    int res;
    for (int i=0; i<4; i++){
        for (int k=0; k<4; k++){
            if (arr2[ans2][i] == arr1[ans1][k]){
                flag++;
                res = arr2[ans2][i];
            }
        }
    }
    if (flag == 0)
        printf("Volunteer cheated!");
    else if (flag == 1)
        printf("%d", res);
    else
        printf("Bad magician!");
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
        scanf("%d", &ans1);
        ans1--;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                scanf("%d", &arr1[i][j]);
        scanf("%d", &ans2);
        ans2--;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                scanf("%d", &arr2[i][j]);
		printf("Case #%d: ", t);
        solve();
        putchar('\n');
	}

}
