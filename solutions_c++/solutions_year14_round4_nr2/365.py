#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 10010
int n,val[maxn],cap;
int main()
{
    int tt;
    int i,N;
    freopen("22.in","r",stdin), freopen("22.out","w",stdout);
    scanf("%d",&tt);
    for (int tcas = 1; tcas <= tt; tcas++){
        scanf("%d",&N);
        for (i = 0;i<N;i++)
            scanf("%d",&val[i]);
        int L = 0, R = N;
        int ans = 0;
        while(L<R){
            int minv = val[L], mini = L;
            for (i = L; i<R; i++)
            if (val[i]<minv){
                minv = val[i];
                mini = i;
            }
            if (mini-L < R-mini-1){
                //go left
                for (i = mini; i>L; i--){
                    ans++;
                    swap(val[i], val[i-1]);
                }
                L++;
            }else {
                // go right
                for (i = mini; i+1<R; i++){
                    ans++;
                    swap(val[i],val[i+1]);
                }
                R--;
            }
        }
        printf("Case #%d: %d\n",tcas, ans);
    }
	return 0;
}
