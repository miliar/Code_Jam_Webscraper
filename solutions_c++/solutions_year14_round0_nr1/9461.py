#include<iostream>
#include<cstdio>

using namespace std;
int main()
{
    int t;
    int a[4][4],b[4][4];
    int i,j,k,l,m;
    int a1,a2,c,ans;
    int caseno = 0;
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    scanf("%d",&t);
    while(t--){
        c = 0;
        scanf("%d",&a1);
        for(i = 0; i < 4; i++){
            for(j = 0; j < 4; j++){
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&a2);
        for(i = 0; i < 4; i++){
            for(j = 0; j < 4; j++){
                scanf("%d",&b[i][j]);
            }
        }
        for(i = 0; i < 4; i++){
            for(j = 0; j < 4; j++){
                //printf("compare = %d  %d",a[a1-1][i],b[a2-1][j]);
                if(a[a1-1][i] == b[a2-1][j]){
                    ans = a[a1-1][i];
                    c++;
                }
            }
        }
        if(c == 0)
            printf("Case #%d: Volunteer cheated!\n",++caseno);
        else if(c == 1)
            printf("Case #%d: %d\n",++caseno,ans);
        else
            printf("Case #%d: Bad magician!\n",++caseno);
    }
    return 0;
}
