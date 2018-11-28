#include<cstdio>
int a[3][4][4];
int ver[20];
int main(){
    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
       for(int j=0;j<20;j++)           ver[j]=0;
       int b,c;
       scanf("%d",&b);
       for(int j=0;j<4;j++){
          for(int k=0;k<4;k++){
                scanf("%d",&a[1][j][k]);  
          }        
       }
       scanf("%d",&c);
       for(int j=0;j<4;j++){
          for(int k=0;k<4;k++){
                scanf("%d",&a[2][j][k]);                    
          }
       }
       for(int j=0;j<4;j++){
           ver[a[1][b-1][j]]=1;
       }
       int counter=0;
       int atual=0;
       for(int j=0;j<4;j++){
           if(ver[a[2][c-1][j]]==1){
              atual=a[2][c-1][j];
              counter++;           
           }        
       }
       if(counter>1)printf("Case #%d: Bad magician!\n",i+1);
       else if(counter==0)printf("Case #%d: Volunteer cheated!\n",i+1);
       else printf("Case #%d: %d\n",i+1,atual);
    }
}
