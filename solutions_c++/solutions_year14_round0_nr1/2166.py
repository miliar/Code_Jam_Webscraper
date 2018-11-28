#include <cstdio>
#include <cmath>
int main()
{
      freopen("A-small-attempt0.in","r",stdin);
      freopen("outputA","w",stdout);

      int cases;
      scanf("%d",&cases);
    
      for(int c = 1 ; c <=cases ; c++)
      {
          int count=0, yes=0;
          int A[4][4];
          int B[4][4];
          int first, second ;
          scanf("%d",&first);
          for(int i=0; i <4; i++)
              for(int j=0; j<4; j++)
                  scanf("%d", &A[i][j]);
          
          scanf("%d",&second);
          for(int i=0; i<4; i++)
              for(int j=0 ; j<4; j++)
                  scanf("%d", &B[i][j]);
          
          for(int i=0; i<4; i++)
          {
              for(int j=0; j<4; j++)
              {
                  if(A[first-1][i]==B[second-1][j])
                  {
                      count=count+1;
                      yes=B[second-1][j];
                      if (count>=2)
                          break;
                  }
              }
          }
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
      }
      return 0 ;
}
