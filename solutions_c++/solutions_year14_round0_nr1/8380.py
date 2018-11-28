// Author : Muhammad Rifayat Samee
// Problem : A
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;
int A[5][5];
int prob[17];
int main(){

	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
    int cases,i,j,k,us,us1,res,ct=1;
    scanf("%d",&cases);
    while(cases--){
        scanf("%d",&us);
        us--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&A[i][j]);
            }
        }
        memset(prob,0,sizeof(prob));
        for(i=0;i<4;i++){
            prob[A[us][i]] = 1;
        }
        int f = 0;
        scanf("%d",&us1);
        us1--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d",&A[i][j]);
            }
        }
        for(i=0;i<4;i++){
            //printf("%d\n",A[us1][i]);
            if(prob[A[us1][i]]){
                f++;
                res = A[us1][i];
            }
        }
        printf("Case #%d: ",ct++);
        if(f==0){
            printf("Volunteer cheated!\n");
        }
        else if(f>1){
            printf("Bad magician!\n");
        }
        else
        printf("%d\n",res);
    }
	return 0;
}
