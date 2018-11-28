#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;

int T,A,N,J;
int arr [101];
//int dp[101000001];

int minimum (int a, int j, int n){
    if (j==n)
        return 0;
    while (j<n&&arr[j]<a){
        a+=arr[j++];
    }
    if (j==n)
        return 0;
    if (a!=1)
        return 1+min(minimum(a+a-1,j,n),minimum(a,j,n-1));
    else return 1+minimum(a,j,n-1);
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for (int k =1;k<=T;k++){
        scanf("%d %d",&A,&N);
        for (int i =0;i<N;i++)
            scanf("%d", &arr[i]);
        sort(arr,arr+N);
        J=0;
        while (J<N&&arr[J]<A){
            A+=arr[J++];
        }
        printf("Case #%d: %d\n",k, minimum(A,J,N));
    }
}
