#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;

int main(){
    FILE *fp = fopen("B-small-attempt1.in","r+");
    FILE *fp2 = fopen("output.txt","w+");
    int no_of_test_cases;
    //scanf("%d",&no_of_test_cases);
    int no = 1;
    fscanf(fp,"%d",&no_of_test_cases);

    while(no_of_test_cases--){
        int old,news,value;
        //scanf("%d %d %d",&old,&news,&value);
        fscanf(fp,"%d %d %d",&old,&news,&value);
        //printf("Case #%d: ",no++);
        fprintf(fp2,"Case #%d: ",no++);
        int res =0;
        for(int i=0; i<old; i++){
            for(int j=0; j<news; j++){
                if((i&j) < value){
                    res++;
                }
            }
        }
        //printf("%d\n",res);
        fprintf(fp2,"%d\n",res);
    }
    return 0;
}
