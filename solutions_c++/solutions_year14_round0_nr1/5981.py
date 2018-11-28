#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int MAX = 5;
int arr1[MAX][MAX];
int arr2[MAX][MAX];
int r1;
int r2;

int main(){
int testcase ;
int cnt=0;
scanf("%d", &testcase);
while(testcase--){
    scanf("%d", &r1);
    for(int i=1;i<MAX;++i){
        for(int j=1;j<MAX;++j){
            scanf("%d", &arr1[i][j]);
        }
    }
    scanf("%d", &r2);
    for(int i=1;i<5;++i){
        for(int j=1;j<5;++j){
            scanf("%d", &arr2[i][j]);
        }
    }
    //sort(arr1[r1]+1, arr1[r1]+4);
    //sort(arr2[r2]+1);
    int nc=0;
    int rec;
    for(int i=1;i<5;++i){
        for(int j=1;j<5;++j){
            if(arr1[r1][i]==arr2[r2][j]){
                    nc++;
                rec=arr1[r1][i];
                break;
            }
        }
    if(nc>1)break;
    }
    if(nc==0)printf("Case #%d: Volunteer cheated!\n", ++cnt);
    else if(nc==1)printf("Case #%d: %d\n", ++cnt, rec);
    else printf("Case #%d: Bad magician!\n", ++cnt);
}
return 0;
}
