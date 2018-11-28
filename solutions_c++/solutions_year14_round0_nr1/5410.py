#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std; 

#define MAXN 110

int cnt1[MAXN],cnt2[MAXN];
int m1[MAXN][MAXN],m2[MAXN][MAXN];

int main(){
    int nt;
    scanf(" %d",&nt);
    for(int t = 1 ; t <= nt ; t++){        
        for(int i = 0 ; i < MAXN ; i++) cnt1[i] = cnt2[i] = 0;        
        int r1,r2;
        scanf(" %d",&r1);r1--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++){
                scanf(" %d",&m1[i][j]);                
            }
            
        scanf(" %d",&r2);r2--;
        for(int i = 0 ; i < 4 ; i++)
            for(int j = 0 ; j < 4 ; j++){
                scanf(" %d",&m2[i][j]);                
            }
        
        for(int j = 0 ; j < 4 ; j++){
            cnt1[m1[r1][j]]++;
            cnt2[m2[r2][j]]++;            
        }        
        int n1 = 0;
        int ans = -1;
        for(int i = 1 ; i <= 16 ;i++)
            if(cnt1[i] == 1 && cnt2[i] == 1){
                n1++;
                ans = i;
            }
                
        printf("Case #%d: ",t); 
        if(n1 == 0) printf("Volunteer cheated!\n");
        else if(n1 == 1) printf("%d\n",ans);
        else printf("Bad magician!\n");       
    }
    return 0;
}
