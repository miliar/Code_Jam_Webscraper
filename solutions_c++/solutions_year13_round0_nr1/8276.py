#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
int i,j,count_x=0,count_o=0,count_t=0,IN=0,T=0,x,flag=0;
char a[4][4],ch,res[100][100];
scanf("%d",&T);
//getchar();
//scan//
for(x=0;x<T;x++)
{
//fflush(stdin);
//fflush(stdin);
//getchar();
IN=0;flag=0;
for(i=0;i<4;i++)
{

for(j=0;j<4;j++)
{
//fflush(stdin);//
//scanf("%c",&ch);
cin>>ch;
if(ch=='\n')
{
j--;
}
a[i][j]=ch;
}
//scanf("%s",&a[i]);
//getchar();
}
//fflush(stdin);//
//getchar();
//getchar();
/*for(i=0;i<4;i++)
for(j=0;j<4;j++)
   scanf("%c",&a[i][j]);*/
//row//
for(i=0;i<4;i++)
{
count_x=0;count_o=0;count_t=0;
for(j=0;j<4;j++)
{
if(a[i][j]=='X')
{
count_x++;
}
else
if(a[i][j]=='O')
{
count_o++;
}
else
if(a[i][j]=='T')
{
count_t++;
}
else 
IN=1;
}
if((count_x==4 && count_o==0)||(count_x==3 && count_t==1 && count_o==0))
{

//printf("Case #%d: X won\n",x+1);
strcpy(res[x],"X won");
flag=1;
break;
}
else
if((count_o==4 && count_x==0)||(count_o==3 && count_t==1 && count_x==0))
{

//printf("Case #%d: O won\n",x+1);
strcpy(res[x],"O won");
flag=1;
break;
}
}
if(flag==1)
{
flag=0;
//getchar();
continue;
}
//column//

for(j=0;j<4;j++)
{
count_x=0;count_o=0;count_t=0;
for(i=0;i<4;i++)
{
if(a[i][j]=='X')
{
count_x++;
}
else
if(a[i][j]=='O')
{
count_o++;
}
else
if(a[i][j]=='T')
{
count_t++;
}
else 
IN=1;
}
if((count_x==4 && count_o==0)||(count_x==3 && count_t==1 && count_o==0))
{

//printf("Case #%d: X won\n",x+1);
strcpy(res[x],"X won");
flag=1;
break;
}
else
if((count_o==4 && count_x==0)||(count_o==3 && count_t==1 && count_x==0))
{

//printf("Case #%d: O won\n",x+1);
strcpy(res[x],"O won");
flag=1;
break;
}
}
if(flag==1)
{
flag=0;
//getchar();
continue;
}
//diagnol//
count_x=0;count_o=0;count_t=0;
for(i=0;i<4;i++)
{
if(a[i][i]=='X')
{
count_x++;
}
else
if(a[i][i]=='O')
{
count_o++;
}
else
if(a[i][i]=='T')
{
count_t++;
}
else 
IN=1;
}
if((count_x==4 && count_o==0)||(count_x==3 && count_t==1 && count_o==0))
{

//printf("Case #%d: X won\n",x+1);
strcpy(res[x],"X won");
flag=1;
break;;
}
else
if((count_o==4 && count_x==0)||(count_o==3 && count_t==1 && count_x==0))
{

//printf("Case #%d: O won\n",x+1);
strcpy(res[x],"O won");
flag=1;
break;
}
if(flag==1)
{
flag=0;
//getchar();
continue;
}
//2//
count_x=0;count_o=0;count_t=0;
for(i=0,j=3;i<4,j>=0;i++,j--)
{
if(a[i][j]=='X')
{
count_x++;
}
else
if(a[i][j]=='O')
{
count_o++;
}
else
if(a[i][j]=='T')
{
count_t++;
}
else 
IN=1;
}
if((count_x==4 && count_o==0)||(count_x==3 && count_t==1 && count_o==0))
{
//printf("Case #%d: X won\n",x+1);
strcpy(res[x],"X won");
flag=1;
break;
}
else
if((count_o==4 && count_x==0)||(count_o==3 && count_t==1 && count_x==0))
{
//printf("Case #%d: O won\n",x+1);
strcpy(res[x],"O won");
flag=1;
break;
}
if(flag==1)
{
flag=0;
//getchar();
continue;
}
if(IN==1)
{
//printf("Case #%d: Game has not completed\n",x+1);
strcpy(res[x],"Game has not completed");
//getchar();
continue;
}
else
{
//printf("Case #%d: Draw\n",x+1);
strcpy(res[x],"Draw");
//getchar();
continue;
}
}
for(x=0;x<T;x++)
{
printf("Case #%d: %s\n",x+1,res[x]);
}
}
