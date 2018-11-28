#include <iostream>
#include <stdio.h>
#include <algorithm>

#define MAXN 1005
using namespace std;

double A[MAXN], B[MAXN];
int N;

int main()
{
    int k;
    scanf("%d", &k);
    for(int t=1; t<=k; t++) {
        scanf("%d", &N);
        for(int i=1; i<=N;i++){
            scanf("%lf", &A[i]);
        }
        for(int i=1; i<=N;i++){
            scanf("%lf", &B[i]);
        }

        sort(A+1, A+N+1);
        sort(B+1, B+N+1);
        
        int ans1=0, ans2=0; 
        int i=1, j=1;
        do {
            if(A[i] > B[j]) {
                ans1++;
                i++; j++;
            }
            else {
                i++;
            }
        } while(i <= N && j <= N);
        
        i = j = 1;
        do {
            if(B[j] > A[i]) {
                ans2++;
                i++; j++;
            }
            else {
                j++;
            }
        } while(i <= N && j <= N);


        printf("Case #%d: %d %d\n",t ,ans1 ,N - ans2); 
    }
    return 0;
}
