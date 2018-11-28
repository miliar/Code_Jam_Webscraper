#include<stdio.h>

int ans;
void print_ans(int num, int test_case){
    if(num==1)
        printf("Case #%d: %d\n",test_case,ans);
    else if(num>1)
        printf("Case #%d: Bad magician!\n",test_case);
    else if(num==0)
        printf("Case #%d: Volunteer cheated!\n",test_case);
    return;
}

int find(int *first, int *second){
    int num=0;
    for(int i=0; i<4;i++){
        for(int j = 0; j<4;j++){
            if(first[i]==second[j]){
                num++;
                ans = first[i];
            }
        }
    }
    return num;
}
int main(){
     int t, a, b;
     int board[4][4];
     int first[4];
     int second[4];
     scanf("%d",&t);
     while(t--){
        scanf("%d",&a);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&board[i][j]);
        for(int i =0; i<4;i++)
            first[i] = board[a-1][i];
        scanf("%d",&b);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&board[i][j]);
        for(int i =0; i<4;i++)
            second[i] = board[b-1][i];
        print_ans(find(first, second), t);
     }
     return 0;
}
