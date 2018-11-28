#include<cstdio>
#include<iostream>
#include<algorithm>
#include<bitset>
#include<vector>
#include<set>
#include<map>

using namespace std;


void alg(int casenum){
    int res = 0, a,b,k;
    printf("Case #%d: ", casenum);
    scanf("%d%d%d", &a, &b, &k);
    for(int i=0; i<k; i++){
        for(int j=0; j<a; j++){
            for(int l=0; l<b; l++){
                if((j&l)==i){
                    res++;
                }
            }
        }
    }
    printf("%d\n", res);

}

int main(){
    int cases = 0;
    scanf("%d", &cases);
    for(int i=1; i<=cases; i++){
        alg(i);
    }
}
