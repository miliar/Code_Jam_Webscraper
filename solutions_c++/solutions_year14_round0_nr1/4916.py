#include<iostream>
#include<cstdio>

using namespace std;

int matrixA[4][4];
int matrixB[4][4];
int rowsA[16];
int rowsB[16];

void printMA(){
        for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                        cout<<matrixA[i][j];
                }
                cout<<"\n";
        }
}

int main(){
        int T,ans1,ans2,testCase = 1;
        scanf("%d",&T);
        while(testCase <= T){
                scanf("%d",&ans1);
                ans1--;
                for(int i = 0; i < 4; i++){
                        for(int j = 0; j < 4; j++){
                                scanf("%d",&matrixA[i][j]);
                                rowsA[--matrixA[i][j]] = i;
                        }
                }

                scanf("%d",&ans2);
                ans2--;
                for(int i = 0; i < 4; i++){
                        for(int j = 0; j < 4; j++){
                                scanf("%d",&matrixB[i][j]);
                                rowsB[--matrixB[i][j]] = i;
                        }
                }
                int numCorrect = 0;
                int card = 0;
                for(int i = 0 ; i < 4; i++){
                        if(rowsB[matrixA[ans1][i]] == ans2){
                                numCorrect++;
                                card = matrixA[ans1][i] + 1;
                        }
                }
                if(numCorrect > 1){
                        printf("Case #%d: Bad magician!\n",testCase);
                }
                else if(numCorrect == 0){
                        printf("Case #%d: Volunteer cheated!\n",testCase);
                }
                else if(numCorrect == 1){
                        printf("Case #%d: %d\n",testCase,card);
                }
                else{
                        printf("error\n");
                }

                testCase++;
        }
}
