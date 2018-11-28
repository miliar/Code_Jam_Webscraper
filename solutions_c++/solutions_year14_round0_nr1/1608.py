#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
#include<iostream>
#include<cmath>
using namespace std;
#define mem(a,b) memset(a,b,sizeof(a))
#define pb push_back
typedef long long ll;

const int N = 110000;

int main()
{
	int T; scanf("%d",&T);
	for(int ka=1;ka<=T;ka++) {
        int r[2];
        int a[2][4][4];
        for(int g=0;g<2;g++) {
            scanf("%d",&r[g]);
            for(int i=0;i<4;i++) for(int j=0;j<4;j++) scanf("%d",&a[g][i][j]);
        }
        int s[4],l=0;
        for(int i=0;i<4;i++) {
            for(int j=0;j<4;j++) {
                if(a[0][r[0]-1][i]==a[1][r[1]-1][j]) {
                    s[l++]=a[0][r[0]-1][i];
                    break;
                }
            }
        }
        printf("Case #%d: ",ka);
        if(l==0) puts("Volunteer cheated!");
        else if(l>1) puts("Bad magician!");
        else printf("%d\n",s[0]);
	}

    return 0;
}
