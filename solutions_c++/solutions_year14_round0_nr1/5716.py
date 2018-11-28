#include <cstdio>

using namespace std;

int main()
{

    int a[5][5];
    int q[5][5];
    int test;
    scanf("%d",&test);
       int k = 1;
    while(test--){

        int b;
        int temp[17]= {0};
        scanf("%d",&b);
        for(int i = 1;i<=4;i++){
            for(int j = 1;j<=4;j++){
                    scanf("%d",&a[i][j]);
            }
        }
        for(int i = 1; i <= 4;i++){
            temp[a[b][i]]++;
        }
        int c;
        scanf("%d",&c);
        for(int i = 1;i<=4;i++){
            for(int j = 1;j<=4;j++){
                    scanf("%d",&q[i][j]);
            }
        }
        for(int i = 1;i <= 4;i++){
                temp[q[c][i]]++;
        }
        int count = 0;
        int temp2= 0;
        for(int i = 1;i <17;i++){
            if(temp[i] >1){
                count++;
                temp2 = i;
            }
        }
        if(count == 0){
            printf("Case #%d: Volunteer cheated!\n",k);

        }
        if(count == 1){
            printf("Case #%d: %d\n",k,temp2);
        }
        if(count >1){
            printf("Case #%d: Bad magician!\n",k);
        }
        k++;
    }
    return 0;
}
