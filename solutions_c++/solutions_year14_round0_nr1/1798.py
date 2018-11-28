#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int t,temp;
    scanf("%d", &t);
    temp = t;
    int arr1[4][4];
    int arr2[4][4];
    int ans1, ans2, no, index1;
    while(t>0){
        no = 0;
        scanf("%d", &ans1);
        for(int a=0;a<4;a++){
            for(int b=0;b<4;b++){
                scanf("%d", &arr1[a][b]);
            }
        }
        scanf("%d", &ans2);
        for(int a=0;a<4;a++){
            for(int b=0;b<4;b++){
                scanf("%d", &arr2[a][b]);
            }
        }
        ans1--;
        ans2--;
        for(int a=0;a<4;a++){
            for(int b=0;b<4;b++){
                if(arr1[ans1][a]==arr2[ans2][b]){
                    no++;
                    index1 = a;
                }     
            }   
        }
        printf("Case #%d: ", temp-t+1);
        if(no==1)   printf("%d\n", arr1[ans1][index1]);
        else if(no==0)      printf("Volunteer cheated!\n");
        else        printf("Bad magician!\n");
        t--;
    }
#ifdef DEBUG
    system("pause>nul");
#endif
    return 0;
}
