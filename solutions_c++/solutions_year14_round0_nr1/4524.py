#include <iostream>
using namespace std;
#include<stdio.h>


int main() {
    int i,t,row;
    freopen("/Users/saintni/Documents/c++/try/try/A-small-attempt2.in","r",stdin);
   freopen("/Users/saintni/Documents/c++/try/try/output.txt","w",stdout);
    scanf("%d¥n",&i);
    int D[4][4];
    int E[4][4];
    
    
    for(t=1;t<=i;t++)
    {
        printf("Case #%d: ", t);
        scanf("%d",&row);
        
        
        
        // Fill in test data
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d",&D[i][j]);
            }
        }
        
        
        
        int row2;
        scanf("%d",&row2);
        
        
        // Fill in test data
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d",&E[i][j]);            }
        }
        
        int nu=0;int k;
        int c[4]={33,33,33,33};
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(D[row-1][i]==E[row2-1][j]){
                    c[i]=D[row-1][i];
                    nu++;k=i;
                }
            }
       }
       if(nu==0){
           printf("Volunteer cheated!");
           cout<<endl;
       }
       else if(nu>1){
            printf("Bad magician!");
            cout<<endl;
        }
        else {
            printf("%d",c[k]);
            cout<<endl;
      }
    }
    return 0;
}