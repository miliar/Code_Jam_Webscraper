#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

typedef long long ll;
using namespace std;

int main(){
    int T,N,M[1000];
    
    scanf("%d",&T);
    
    for(int i=1;i<=T;i++){
        int ans1=0,ans2=10000000;
        
        scanf("%d",&N);
        
        for(int j=0;j<N;j++){
            scanf("%d",&M[j]);
            
            if(j>0) ans1+=max(M[j-1]-M[j],0);
        }
        
        for(int j=0;j<=10000;j++){
            int ans3=0;
            
            for(int k=1;k<N;k++){
                if(M[k-1]<=M[k]+j){
                    ans3+=min(j,M[k-1]);
                }else{
                    ans3=-1;
                    break;
                }
            }
            
            if(ans3!=-1){
                ans2=min(ans2,ans3);
            }
            
        }
        
        printf("case #%d: %d %d\n",i,ans1,ans2);
        
        
    }
    
    return 0;
}
