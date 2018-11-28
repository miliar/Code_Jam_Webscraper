#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std; 

int T;

int m[4][4];

int r[16][2];

void solve(int t){
     memset(r,0,sizeof r);
     for (int i=0;i<2;i++){
         int rowNumber;
         scanf("%d",&rowNumber);
         for (int j=0;j<4;j++)
         for (int k=0;k<4;k++) scanf("%d",&m[j][k]);
         for (int j=0;j<4;j++) r[m[rowNumber-1][j]-1][i]=1;
         }
     
     int ans=0;
     int res=0;
     for (int i=0;i<16;i++){
         ans=ans+r[i][0]*r[i][1];
         if (r[i][0]*r[i][1]==1) res=i+1;
         }
     
     if (ans<1){
        printf("Case #%d: Volunteer cheated!\n",t);        
        }
     if (ans>1){
        printf("Case #%d: Bad magician!\n",t);        
        }   
     if (ans==1){
        printf("Case #%d: %d\n",t,res);         
        }   
     
     }

int main(){
    scanf("%d",&T);
    for (int t=1;t<=T;t++){
        solve(t);
        }
    return 0;
    }
