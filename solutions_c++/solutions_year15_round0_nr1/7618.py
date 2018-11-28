#include<iostream>
#include<fstream>
#include<stdio.h>

using namespace std;

int main(){
    int no_of_test_cases;

    scanf("%d",&no_of_test_cases);
    int caseNo = 1;
    while(no_of_test_cases--){
        int sMax;
        char str[1002];
        int arr[1002] = {0};

        scanf("%d",&sMax);
        scanf("%s",str);
        int i = 0;
        while(str[i]!='\0'){
            arr[i] = str[i] - '0';
            i++; 
        }
        int res = 0;
        int totalStanding = arr[0];
        for(int i= 1; i<= sMax; i++){
            if(totalStanding < i){
                res++;
                totalStanding++;
            }
            totalStanding += arr[i];
        }
        printf("Case #%d: %d\n",caseNo,res);
        caseNo++;
    }
    return 0;
}
