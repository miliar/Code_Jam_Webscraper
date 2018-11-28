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
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);

    //std::ios::sync_with_stdio(false);
    int t,k,c,s;
    l64d res,tmp;
    l64d n;
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:", i+1);
        for(int j=0;j<k;j++) {
            printf(" %d", j+1);
        }
        printf("\n");
    }

    #ifdef Xanxiver
    ellapse;
    #endif // Xanxiver
}

