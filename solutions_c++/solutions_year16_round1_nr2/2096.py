#include<bits/stdc++.h>
#define MAX 10000
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define ellapse printf("Time : %0.3lf\n",clock()*1.0/CLOCKS_PER_SEC);
using namespace std;
/*
//E,SE,S,SW,W,NW,N,NE
int dr[8]={0,1,1,1,0,-1,-1,-1};
int dc[8]={1,1,0,-1,-1,-1,0,1};
*/
typedef long long l64d;
typedef unsigned long int ud;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
vector<int> ok;
bool seen[15] = {};
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    //std::ios::sync_with_stdio(false);
    int t;
    int n;
    int cnt[2505] = {};
    int a;
    scanf("%d",&t);
    for(int i=1;i<=t;i++) {
        scanf("%d",&n);
        memset(cnt, 0 , sizeof cnt);
        for(int j=0;j<2*n-1;j++) {
            for(int k=0;k<n;k++) {
                scanf("%d",&a);
                cnt[a]++;
            }
        }
        printf("Case #%d:", i);
        for(int j=1;j<=2500;j++) {
            if(cnt[j]%2==1) {
                printf(" %d",j);
            }
        }
        printf("\n");
    }

    #ifdef Xanxiver
    ellapse;
    #endif // Xanxiver
}
