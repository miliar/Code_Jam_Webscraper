#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>

using namespace std;

int a[8][8];
int br[26];

void solve(int test_case)
{
    int i, j, b=0, ans;
    int f, s;

    memset(br, 0, sizeof(br));

    scanf("%d", &f);

    for(i=0; i<4; i++)
        for(j=0; j<4; j++){
            scanf("%d", &a[i][j]);
        }

    for(j=0; j<4; j++)
        br[a[f-1][j]] ++;

    // ======================================

    scanf("%d", &s);
	
    for(i=0; i<4; i++)
        for(j=0; j<4; j++){
            scanf("%d", &a[i][j]);
        }

    for(j=0; j<4; j++)
        br[a[s-1][j]] ++;

    // =====================================

    for(i=1; i<=16; i++){
	if(br[i] == 2){
            b++;
            ans = i;
        }
    }
    printf("Case #%d: ", test_case);

    if( b== 1) printf("%d\n", ans);
    else if( b> 1) printf("Bad magician!\n");
    else if(! b) printf("Volunteer cheated!\n");
}

int main()
{
   
    int i, t;

    scanf("%d", &t);
   
    for(i=1; i<=t; i++)
      solve(i);

    return 0;
}
