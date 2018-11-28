#include<cstdio>
#include<map>
#include<stack>
#include<vector>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
char a[5][5];
struct cnt{
       int x;
       int o;
       };
cnt abx[4],aby[4],abd[2];
bool flag;       

int check()
{
    
    int i,j;
    for(i=0;i<4;i++)
    for(j=0;j<4;j++)
    {
     if(a[i][j]=='X'||a[i][j]=='T')
     abx[i].x++;
     if(a[i][j]=='O'||a[i][j]=='T')
     abx[i].o++;
     if(!flag && a[i][j]=='.' )
     flag=true;
     
     
     if(a[j][i]=='X'||a[j][i]=='T')
     aby[i].x++;
     if(a[j][i]=='O'||a[j][i]=='T')
     aby[i].o++;
    
         
    if(i==j)
    {if(a[i][j]=='X'||a[i][j]=='T')
    abd[0].x++;
    if(a[i][j]=='O'||a[i][j]=='T')
    abd[0].o++;}
    
    if(i+j==3)
    {if(a[i][j]=='X'||a[i][j]=='T')
    abd[1].x++;
    if(a[i][j]=='O'||a[i][j]=='T')
    abd[1].o++;
    }
    } 
     
}


int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t,i,j,k=1;
	
    scanf("%d",&t);
	while(t--)
	{
     
     for(i=0;i<4;i++)
     {
     abx[i].x=0;
     abx[i].o=0;
     aby[i].x=0;
     aby[i].o=0;
     
     
     
     }
     abd[0].x=0;
     abd[0].o=0;
     abd[1].x=0;
     abd[1].o=0;
     
     flag=false;
     for(i=0;i<4;i++)
     scanf("%s",a[i]);
                  
                     
     
     check();
     bool t=false;
     printf("Case #%d: ",k++);
     for(i=0;i<4;i++)
     {
     if(abx[i].x==4 || aby[i].x==4 || abd[0].x==4|| abd[1].x==4)
     {
                  t=true;
                  printf("X won");
                  break;
     }
     
     
     if(abx[i].o==4 || aby[i].o==4 || abd[1].o==4 ||abd[0].o==4)
     {
                  t=true;
                  printf("O won");
                  break;
     }
     }
     
     if(!t && !flag)
     printf("Draw");
 
     
     if(flag && !t)
     {
             printf("Game has not completed");
     }
     
     
     printf("\n");	
     }
     
}

    
