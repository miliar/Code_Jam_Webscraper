#include<iostream>
#include<stdio.h>
 
using namespace std;
 int a[102][102]={0};
 int n,m;
 
 int checkcol(int x){
     for(int i=0;i<m;i++){
         if(a[x][i]!=1)
            return 0;
     }
     return 1;
 }
 
 int checkrow(int y){
     for(int i=0;i<n;i++){
         if(a[i][y]!=1)
            return 0;
     }
     return 1;
 }
int main(){
    int t,flag=0;
    
    scanf("%d",&t);
    for(int i1=1;i1<=t;i1++){
            flag=0;
            scanf("%d",&n);
            scanf("%d",&m);
            for(int j=0;j<n;j++){
                for(int k=0;k<m;k++){
                    scanf("%d",&a[j][k]);
                }
            }
        
        for(int i=0;i<n && flag==0;i++){
            for(int j=0;j<m && flag==0;j++){
                if(a[i][j]==1){
                    if( !(checkcol(i) || checkrow(j)) ){
                        printf("Case #%d: NO\n",i1);
//                        cout<<endl<<i<<"**"<<j<<endl;
                        flag=1;
                    }
                }
            }
        }
        if(flag==0)
         printf("Case #%d: YES\n",i1);
    }               
    return 0;
}
        