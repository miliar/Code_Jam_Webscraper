#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
struct node
{
    int a,b,n;
};
node table[250][250];
queue <node> Q;
char ans[1000];
int main(){
    
    int n,m,i,j,k,t,a,b,last,x,y;
    node temp,p;
    
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    
    scanf("%d",&t);
    for(k=1;k<=t;k++)
       {
        scanf("%d%d",&a,&b);
        
        a+=100;
        b+=100;
        for(i=0;i<250;i++)
           for(j=0;j<250;j++)
              {
               table[i][j].a = 0;
               table[i][j].b = 0;
               table[i][j].n = 999999;
              }
        
        temp.a = 100;
        temp.b = 100;
        temp.n = 1;
        Q.push(temp);
        
        while(!Q.empty())
           {
            p = Q.front();
            table[p.a][p.b].n = p.n;
            //if(table[p.a][p.b] .n != 999999) 
            //   {
            //    Q.pop();
            //    continue;
            //   }
            //printf("%d %d %d\n",p.a,p.b,p.n);
            if( p.a + p.n < 201 && table[p.a + p.n][p.b].n == 999999)
               {
               // printf("-*-");
                temp.a = p.a+p.n;
                temp.b = p.b;
                temp.n = p.n+1;
                table[p.a+p.n][p.b].n = p.n;
                table[p.a+p.n][p.b].a = p.a;
                table[p.a+p.n][p.b].b = p.b;
                
                Q.push(temp);
               }
            if( p.a - p.n >= 0 && table[p.a - p.n][p.b].n == 999999)
               {
               // printf("-*-");
                temp.a = p.a-p.n;
                temp.b = p.b;
                temp.n = p.n+1;
                table[p.a-p.n][p.b].n = p.n;
                table[p.a-p.n][p.b].a = p.a;
                table[p.a-p.n][p.b].b = p.b;
                
                Q.push(temp);
               }
               
            if( p.b + p.n < 201 && table[p.a][p.b+p.n].n == 999999)
               {
              //  printf("........");
                temp.a = p.a;
                temp.b = p.b+p.n;
                temp.n = p.n+1;
                table[p.a][p.b+p.n].n = p.n;
                table[p.a][p.b+p.n].a = p.a;
                table[p.a][p.b+p.n].b = p.b;
                
                Q.push(temp);
               }
            if( p.b - p.n >= 0 && table[p.a][p.b-p.n].n == 999999)
               {
                temp.a = p.a;
                temp.b = p.b-p.n;
                temp.n = p.n+1;
                table[p.a][p.b-p.n].n = p.n;
                table[p.a][p.b-p.n].a = p.a;
                table[p.a][p.b-p.n].b = p.b;
                
                Q.push(temp);
               }
            
            Q.pop();
            
           }
        //printf("...");
        last = 0;
        /*for(i=90;i<110;i++)
           {for(j=90;j<110;j++)
              printf("%d ",table[i][j].n);
            printf("\n");
           }  */
        //scanf(" ");
        x = a;
        a = b;
        b = x;
        while(a != 100 || b != 100)
           {
            //printf("%d %d\n",a,b);
            if(table[a][b].a == a )
               {
                if(table[a][b].b > b)
                   ans[last++] = 'W';
                   
                else ans[last++] = 'E';
               }
            else if(table[a][b].b == b)
               {
                if(table[a][b].a > a)
                   ans[last++] = 'S';
                else ans[last++] = 'N';
               }
            x = a;y = b;
            a = table[x][y].a;
            b = table[x][y].b;
           }
        
        
        
        printf("Case #%d: ",k);
        for(last--;last>=0;last--)
           printf("%c",ans[last]);
        printf("\n");
       }
    
    
    
    
    
 scanf(" ");
 return 0;
}
