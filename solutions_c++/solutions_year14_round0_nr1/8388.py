#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
     int t;
     scanf("%d",&t);
     int cases=1;
     int a[5][5];
     int b[5][5];
     int x,y;
     int i ,j,k;
     int aa[20];
   
     
     while(t--)
     {
         cin>>x;
         for(i=1;i<=4;i++)
             for(j=1;j<=4;j++)             
                cin>>a[i][j];
         cin>>y;
         for(i=1;i<=4;i++)
             for(j=1;j<=4;j++)             
                cin>>b[i][j];
                
          memset(aa,0,sizeof(aa));
         
          for(i=1;i<=4;i++)
          {
              aa[a[x][i]]++;
              aa[b[y][i]]++;
          }
          
          int num2=0;
          for(i=1;i<=16;i++)
          {            
             if(aa[i]==2) num2++;
          }
          
          if(num2>1) printf("Case #%d: Bad magician!\n",cases++);
          else if(num2==0) printf("Case #%d: Volunteer cheated!\n",cases++);
          else
          {
              for(i=1;i<=16;i++){
                                 if(aa[i]==2)
                                 {
                                  printf("Case #%d: %d\n",cases++,i);
                                  break;
                                  }
                                  }
          }
          
     }
     return 0;
}
          
          
         
                     
         
