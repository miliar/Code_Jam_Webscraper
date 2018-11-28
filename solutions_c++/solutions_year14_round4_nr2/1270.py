#include<stdio.h>
#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
using namespace std;
int n;
int num[1010];
int tmp[1010];
bool check(int tmp[]){
    bool state = 0;
    for(int i = 0 ; i < n-1;i++)
    if(state == 0){
        if(tmp[i+1] <tmp[i] ) state  =1;
    }else{
        if(tmp[i+1] > tmp[i]) return false;
    }
    return true;
}
int bsort(int tmp[], int l,int r, int state){
    int cnt=0;
    for(int i = l ; i <= r; i++)
    for(int j = l; j < r; j++)
    if(state == 0){
        if(tmp[j] > tmp[j+1]){
            swap(tmp[j],tmp[j+1]);
            cnt++;
        }
    }else{
        if(tmp[j] < tmp[j+1]){
            swap(tmp[j],tmp[j+1]);
            cnt++;
        }
    }
    return cnt;
}
int abs(int x){return x<0?-x:x;}

int findPos(int value,int tmp[]){
    for(int i = 0 ; i< n;i++)
        if(tmp[i] == value) return i;
}
int best[1010];
int main(){
    int T;scanf("%d",&T);
    for(int _ = 1; _<=T;_++){
        printf("Case #%d: ",_);
        scanf("%d",&n);
        for(int i = 0 ; i < n ;i++){scanf("%d",&num[i]);tmp[i]=num[i];}
        int ans = 2147483647;
        sort(tmp,tmp+n);
        do{
            int h[1010];
           // puts("hi");
            for(int i = 0 ; i < n;i++)
                h[i] = findPos(num[i],tmp);

            if(check(tmp)){
                int a1 = bsort(h,0 , n-1,0);
                if(a1 < ans){

                    ans = a1;
                    //for(int i = 0 ; i<n;i++) best[i] = tmp[i];
                }
                //ans = min(ans, a1);
            }

        }while(next_permutation(tmp,tmp+n));
        //for(int i = 0 ; i< n ;i++){
         //   printf("%d ",best[i]);
        //}
        //puts("");
        printf("%d\n",ans);
    }
    return 0;
}

