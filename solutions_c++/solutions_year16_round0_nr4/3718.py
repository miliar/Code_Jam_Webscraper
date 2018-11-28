#include <cstdio>
#include <algorithm>
#include <iostream>
typedef unsigned long long ull;
using namespace std;
int main (){
    int T;
    scanf("%d",&T);
    for(int I = 1 ; I <= T ; I ++ ){
        int k,c,s;
        scanf("%d%d%d",&k,&c,&s);
        if(s<k-c+1)printf("Case #%d: IMPOSSIBLE\n",I);
        else if(c>=k){
            printf("Case #%d:",I);
            ull tmp=0;
            for(int j = k-1 ; j >= 0 ; j --){
                    tmp*=k;
                    tmp+=j;
            }
            for(int j = c-k ; j > 0 ; j --)tmp*=k;
            tmp++;
            cout << " " << tmp;
            puts("");
        }
        else{
            if(k%c==0){
                printf("Case #%d:",I);
                for(int i = 0 ; i < k/c ; i ++){
                    ull tmp=0;
                    for(int j = i*c ; j < (i+1)*c ; j ++){
                        tmp*=k;
                        tmp+=j;
                    }
                    tmp++;
                    cout << " " << tmp;
                }
                puts("");
            }
            else{
                printf("Case #%d:",I);
                for(int i = 0 ; i < k/c ; i ++){
                    ull tmp=0;
                    for(int j = i*c ; j < (i+1)*c ; j ++){
                        tmp*=k;
                        tmp+=j;
                    }
                    tmp++;
                    cout << " " << tmp;
                }
                {
                    ull tmp=0;
                    for(int j = k-c ; j < k ; j ++){
                        tmp*=k;
                        tmp+=j;
                    }
                    tmp++;
                    cout << " " << tmp;
                }
                puts("");
            }
        }
    }

}
