#include<stdio.h>
#include<iostream>
#define gc getchar

long long int read() {
  long long int ret=0;
  char c=gc();
  while(c<'0'||c>'9') c=gc();
  while(c>='0'&&c<='9') {
    ret=10*ret+c-48;
    c=gc();
  }
  return ret;
}


using namespace std;

int main(){
    FILE *fp = fopen("A-small-attempt2.in","r+");
    FILE *fp2 = fopen("output.txt","w+");
    //long long int no_of_test_cases = read();
    long long int no_of_test_cases;
    fscanf(fp,"%lld",&no_of_test_cases);
    int no = 1;
    int value;

    while(no_of_test_cases--){
        int row1,row2;
        int matrix1[4][4],matrix2[4][4];

        //row1 = read();
        fscanf(fp,"%d",&row1);
        row1--;

        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                //matrix1[i][j] = read();
                fscanf(fp,"%d",&matrix1[i][j]);
            }
        }

        //row2 = read();
        fscanf(fp,"%d",&row2);
        row2--;

        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                //matrix2[i][j] = read();
                fscanf(fp,"%d",&matrix2[i][j]);
            }
        }

        int count = 0;

        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(matrix1[row1][i] == matrix2[row2][j]){
                    count++;
                    value = matrix1[row1][i];
                }
            }
        }

        if(count == 1){
            //printf("Case #%d: %d\n",no++,value);
            fprintf(fp2,"Case #%d: %d\n",no++,value);
        }
        else if(count > 1){
            //printf("Case #%d: Bad magician!\n",no++);
            fprintf(fp2,"Case #%d: Bad magician!\n",no++);
        }
        else{
            //printf("Case #%d: Volunteer cheated!\n",no++);
            fprintf(fp2,"Case #%d: Volunteer cheated!\n",no++);
        }
    }

    return 0;
}
