#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <set>
#include <functional>

using namespace std;

int main(int argc,const char * argv[]){
    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );
    int t,k=1;
    scanf("%d",&t);
    while(t--){
        int fCard,sCard;
        scanf("%d",&fCard);
        int a[5][5];
        int b[5][5];
        for(int h=1;h<5;h++)
            for(int k=1;k<5;k++)
                scanf("%d",&a[h][k]);
        scanf("%d",&sCard);
        for(int i=1;i<5;i++)
            for(int j=1;j<5;j++)
                scanf("%d",&b[i][j]);
        int candidates = 0,s=0;
        for(int m=1;m<5;m++){
            for(int n=1;n<5;n++){
                if(a[fCard][m]==b[sCard][n]){
                    candidates++;
                    s=m;
                    }
            }
        }
        printf("Case #%d: ",k++);
        if(candidates>1)
            printf("Bad magician!");
        else if(candidates==1)
            printf("%d",a[fCard][s]);
        else
            printf("Volunteer cheated!");
        printf("\n");
    }
    return 0;
}
