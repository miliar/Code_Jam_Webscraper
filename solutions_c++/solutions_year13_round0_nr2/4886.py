#include<iostream>
#include<stdio.h>
using namespace std;

int main(){
        
        freopen("B-large (1).in","r",stdin);
        freopen("out.txt","w",stdout);
        int t,n,m,mat[100][100],i,j,x,flag;
        int row[100],col[100];
        cin>>t;
        int a = 1;
        while(t--){
            cin>>n>>m;
            for(i=0;i<n;i++){
                for(j=0;j<m;j++){
                    cin>>mat[i][j];
                }
            }
            for(i=0;i<n;i++){
                x = mat[i][0];
                row[i] = 0;
                for(j=1;j<m;j++){
                    if(mat[i][j]>x){
                        x = mat[i][j];
                        row[i] = j;
                    }
                }
            }       
             for(i=0;i<m;i++){
                x = mat[0][i];
                col[i] = 0;
                for(j=1;j<n;j++){
                    if(mat[j][i]>x){
                        x = mat[j][i];
                        col[i] = j;
                    }
                }
            }      
            flag=0;
            for(i=0;i<n;i++){
                for(j=0;j<m;j++){
                     if((mat[i][j] == mat[i][row[i]]) || (mat[i][j] == mat[col[j]][j]));
                     else{
                         flag=1;
                         break;
                     }
                 }
                 if(flag==1) break;
             }
             if(flag == 0) cout<<"Case #"<<a<<": YES\n";
             else cout<<"Case #"<<a<<": NO\n";    
             a++;
         } 
         
}        
                    
                    
