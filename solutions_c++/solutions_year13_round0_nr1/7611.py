#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
#define p(i) printf("%d\n",i)
#define s(i) scanf("%d",&i)
#define sc(i) scanf("%s",&i)
#define f(n,i) for(int i=0;i<n;i++)
int total=0;
bool comp(char a,char c)
{
     if(a==c&&a!='.'){return 1;}
if((c=='T'&&a!='.')||(a=='T'&&c!='.')){return 1;}
return 0;
}
int main()
{
    int t;
    s(t);
    f(t,k)
    {char str[4][5];total=0;
    f(4,i){scanf("%s",&str[i]);}
    int co=0,cx=0;
    int flago=0,flagx=0,flag=0;
    f(4,i)
    f(4,j)
    if(str[i][j]!='.')total++;
    f(4,i)
    {
    flag=0;flagx=0;flago=0;
    f(3,j)
    {if(str[i][j]=='O'||str[i][j+1]=='O')flago++;
    if(str[i][j]=='X'||str[i][j+1]=='X')flagx++;
    
    if(!comp(str[i][j],str[i][j+1]))
    {if(str[i][j]=='O'||str[i][j+1])
    //printf("\nin %c %c\n",str[i][j],str[i][j+1]);
    flag=1;
    break;
    }
    }
    if(flag==0&&str[i][0]=='O'&&flagx==0)co++;
    else if(flag==0&&flago==0)cx++;
    }
    f(4,i)
    {flag=0;
    flago=flagx=0;
    f(3,j)
    {
    if(str[j][i]=='O'||str[j+1][i]=='O')flago++;
    if(str[j][i]=='X'||str[j+1][i]=='X')flagx++;      
    if(comp(str[j][i],str[j+1][i])==0){
                                        //printf("%c %c\n",str[j][i],str[j+1][i]);
                                        flag=1;break;}}
    if(flag==0&&str[0][i]=='O'&&flagx==0)co++;
    else if(flag==0&&flago==0)cx++;
    }
    flag=0;
    flago=flagx=0;
    f(3,i)
    {
          if(str[i][i]=='O'||str[i+1][i+1]=='O')flago++;
    if(str[i][i]=='X'||str[i+1][i+1]=='X')flagx++;
          if(comp(str[i][i],str[i+1][i+1])==0){flag=1;break;}}
    
    if(flag==0&&str[0][0]=='O'&&flagx==0)co++;
    else if(flag==0&&flago==0)cx++;
    
    
    flag=0;
    flago=flagx=0;
    f(3,i)
    {
          if(str[i][3-i]=='O'||str[i+1][2-i]=='O')flago++;
    if(str[i][3-i]=='X'||str[i+1][2-i]=='X')flagx++;
          if(comp(str[i][3-i],str[i+1][2-i])==0){flag=1;break;}
    }
    if(flag==0&&str[0][3]=='O'&&flagx==0)co++;
    else if(flag==0&&flago==0)cx++;
    
    printf("Case #%d: ",k+1);
    if(cx==0&&co>0)
    printf("O won\n");
    else if(co==0&&cx>0)
    printf("X won\n");
    else if(cx>0&&co>0)
    printf("Draw\n");
    else if(cx<1&&co<1&&total==16)
    printf("Draw\n");  
    else 
    printf("Game has not completed\n");
}
}    
