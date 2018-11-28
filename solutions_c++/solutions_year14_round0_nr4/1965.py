#include <cstdio>
#include <cmath>
int main()
{
      freopen("D-large.in","r",stdin);
      freopen("outputDlarge","w",stdout);

      int cases, N;
      scanf("%d",&cases);

      for(int c = 1 ; c <=cases ; c++)
      {
          scanf("%d",&N);
          
          double A[2][N];
          int    B[2][N];
          int count1=0, count2=0, temp=0, oo1=0, oo=0, w=0, w1=0;
          
          for(int i=0; i<2; i++)
              for(int j=0; j<N; j++)
              {
                  scanf("%lf", &A[i][j]);
                  B[i][j]=(round(A[i][j]*10000));
                  ///////stupid swap///////
                  if (j>=1)
                      for (int k=0; k<j; k++)
                          if (B[i][j-k]<B[i][j-1-k])
                          {
                              temp=B[i][j-k];
                              B[i][j-k]=B[i][j-1-k];
                              B[i][j-1-k]=temp;
                              
                          }
              }
          //round 1
          for(int j=0; j<N; j++)
          {
              if (w1==0)
                  oo1=j;
              
              if (B[0][oo1]>B[1][j])
              {
                  count2=count2+1;
                  oo1=oo1+1;
                  if (oo1>=N)
                      break;
              }
              else
              {
                  for(int k=1; k<N-j; k++)
                      if (B[0][j+k]>B[1][j])
                      {
                          count2=count2+1;
                          oo1=j+k+1;
                          w1=1;
                          //printf("%d",oo);
                          
                          break;
                      }
                  if (oo1>=N)
                      break;
              }
              
          }

          //round 2
          for(int j=0; j<N; j++)
          {
              if (w==0)
                  oo=j;
              
              if (B[0][j]<B[1][oo])
              {
                  count1=count1+1;
                  oo=oo+1;
                  if (oo>=N)
                      break;
              }
              else
              {
                  for(int k=1; k<N-j; k++)
                      if (B[0][j]<B[1][j+k])
                      {
                          count1=count1+1;
                          oo=j+k+1;
                          w=1;
                          //printf("%d",oo);

                          break;
                      }
                  if (oo>=N)
                      break;
              }
            
          }
          
          
          printf("Case #%d: %d %d\n",c,count2, N-count1);
          /*
          printf("///////////\n");
          for(int i=0; i<2; i++)
          {
              for(int j=0; j<N; j++)
              {
                  printf(" %d",B[i][j]);
              }
              printf("\n");
              
          }
          printf("///////////\n");
          */
          /*
          if (count==1)
          {
              printf("Case #%d: %d\n",c,yes);
          }
          else if (count==0)
          {
              printf("Case #%d: Volunteer cheated!\n",c);
          }
          else
          {
              printf("Case #%d: Bad magician!\n",c);
          }
           */
      }
      return 0 ;
}
