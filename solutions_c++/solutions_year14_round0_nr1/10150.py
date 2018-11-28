#include <iostream>
using namespace std;
int A,a[5][5],B,b[5][5];
int main(){
   // freopen("a.in","r",stdin);
   // freopen("a.out","w",stdout);
    int data,r=0,wc;
    cin>>data;
    int rec[17],cnt;
    while ( data-- ){
          r++;
          cnt=0;
          memset(rec,-1,sizeof(rec));
          scanf("%d",&A);
          for (int i=1;i<=4;i++)   
              for (int j=1;j<=4;j++)
                  scanf("%d",&a[i][j]);
          for (int j=1;j<=4;j++) 
              rec[ a[A][j] ] ++;
          //sort(&a[A][1],&a[A][5]);
          scanf("%d",&B);
          for (int i=1;i<=4;i++)
              for (int j=1;j<=4;j++)
                  scanf("%d",&b[i][j]);
          for (int j=1;j<=4;j++){
              rec[ b[B][j] ]++;
              if ( rec[ b[B][j] ] > 0 ){ 
                   wc=b[B][j];  
                   cnt++;
              }
          }
          if ( cnt == 0 ) printf("Case #%d: Volunteer cheated!\n",r);
          if ( cnt > 1 ) printf("Case #%d: Bad magician!\n",r);
          if ( cnt == 1 ) printf("Case #%d: %d\n",r,wc);
          //sort(&b[B][1],&b[B][5]);
    
          
          
          
          
    }
    return 0;
}
