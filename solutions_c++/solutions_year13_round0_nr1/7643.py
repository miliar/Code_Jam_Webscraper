#include<cstdio>
#include<iostream>
int main()
{
    int a[4][4],diagonal=0,column=0,row=0,test,l,k,i,j,m=1;
    char s;
    scanf("%d",&test);
    while(test--)
       {   
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {std::cin>>s;
            if(s=='X')
            a[i][j]=1;
            else if(s=='O')
            a[i][j]=2;
            else if(s=='T')
            a[i][j]=10;
            else
            a[i][j]=140;
            }
        }
        for(i=0;i<4;i++)
        {   
               j=0;        
               k=a[i][j]+a[i][j+1]+a[i][j+2]+a[i][j+3];
              if((k==16)||(k==8)||(k==13)||(k==4))
              {
                  row=1;
                  
                  break;
              }
              else
              row=0;
//            printf("%d\n",k);
        }
        if(row==0)
        {
            for(i=0;i<4;i++)
        {   
            
                j=0;
                k=a[j][i]+a[j+1][i]+a[j+2][i]+a[j+3][i];
               if(k==16||k==8||k==13||k==4)
              {
                  column=1;
                  break;
              }
              else
              column=0;
  //          printf("%d\n",k);
        }
        }
         if(row==0&&column==0)
        {
            k=a[0][0]+a[1][1]+a[2][2]+a[3][3];
            l=a[0][3]+a[1][2]+a[2][1]+a[3][0]; 
             if(k==16||k==8||k==13||k==4)
             diagonal=1;
             else if(l==16||l==8||l==13||l==4)
             diagonal=1;
             else
             diagonal=0;
    //         printf("%d %d %d",l,k,diagonal);
        }
        if(row||diagonal==1||column==1)
        {
            if(k==16||k==8||l==16||l==8)
            {
                printf("Case #%d: ",m);
                printf("O won\n");
                
            }
            else
            {
               printf("Case #%d: ",m);
                printf("X won\n"); 
            }
            
        }
        else
        {
            if(k>140||l>140)
            {
              printf("Case #%d: ",m);
                printf("Game has not completed\n");   
            }
            else
            {
                printf("Case #%d: ",m);
                printf("Draw\n"); 
            }
        
        }
    //printf("%d %d %d",row,column,diagonal);
    //printf("%d",k);
    //column=0;
   // row=0;
 //   diagonal=0;
 m++;
k=0;
l=0;
    }
    return 0;
    
}
