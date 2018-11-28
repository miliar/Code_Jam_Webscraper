#include<iostream>
using namespace std;

int main(void)
{
    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    char a[4][4];
    int i,j;
    int c,r,t,tc=1,tc1;
    int cz;
    
    scanf("%d",&tc1);
   // cout<<tc1;
    
    while(tc<=tc1)
    {
    cz=0;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>a[i][j];
            if(a[i][j]=='.')
            cz=1;
        }
    }     
    t=0;
    for(i=0;i<4;i++)
    {
    r=0;
    c=0;
    r=r+a[i][0]+a[i][1]+a[i][2]+a[i][3];
    c=c+a[0][i]+a[1][i]+a[2][i]+a[3][i];
       
         
         if(r==352||c==352||r==348||c==348)
         {printf("Case #%d: X won\n",tc);
         t++;
         break;
         }
         else if(r==316||c==316||r==321||c==321)
         {           printf("Case #%d: O won\n",tc);
                     t++;
                     break;
         }
        
         }
                if(t==0)
                 {   r=0;
                     c=0;
                     r=a[0][0]+a[1][1]+a[2][2]+a[3][3];
                     c=a[0][3]+a[1][2]+a[2][1]+a[3][0];
                      if(r==352||c==352||r==348||c==348)
                     printf("Case #%d: X won\n",tc);
                     else if(r==316||c==316||r==321||c==321)
                      printf("Case #%d: O won\n",tc);
                     else if(cz==1)
                     printf("Case #%d: Game has not completed\n",tc); 
                     else
                     printf("Case #%d: Draw\n",tc);
                     
                    }
         tc++;
         }
         return 0;
}
