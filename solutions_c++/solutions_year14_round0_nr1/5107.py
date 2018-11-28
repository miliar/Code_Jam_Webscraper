
#include<stdio.h>

int main()
{
long long int tc,i,j,k,n,l;
long long int a[1005][105];
long long int a1[1005][105];

freopen("ques1.txt","w",stdout);
scanf("%lld",&tc);

for(k=1; k<= tc ; k++)
{
          scanf ("%lld",&n);
          
          for(i=1;i<=4;i++){
                           for(j=1;j<=4;j++){
                                            scanf("%lld",&a[i][j]);
                           }
          }
                                            
          scanf("%lld",&l);
          for(i=1;i<=4;i++){
                           for(j=1;j<=4;j++){
                                            scanf("%lld",&a1[i][j]);
                           }
          }
          
          long long  no;
          long long  chut = 0;
          
          for(i = 1; i <= 4 ; i++)  
          {
                for(j = 1; j<= 4; j++)
                 {
                        if(a[n][i] == a1[l][j])
                       {
                                   no = a[n][i];
                                   chut++;
                                   
                                   break;
                      }
                }
          }
          
          if(chut == 0) 
          {
                  printf("Case #%lld: Volunteer cheated!\n",k);
          }
          else if(chut == 1) {
               printf("Case #%lld: %lld\n",k,no);
          }
          else
          printf("Case #%lld: Bad magician!\n",k);
    }
    
    
    
    return 0;
}
          
                      
          
