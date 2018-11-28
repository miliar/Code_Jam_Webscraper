#include<stdio.h>
int main()
{
   /* fstream ifile;
    ifile.open("A-small-attempt0.in");
    fstream ofile;
    ofile.open("t.txt");

*/

int t,k,countd=0,countt,countx,counto;
int flag;
char temp[5];
char a[4][4];
//ifile.read((char *)&t, sizeof(t));
scanf("%d",&t);
for(k=1;k<=t;k++)
{int i,j;
flag=0;
i=0;j=0;
for(i=0;i<4;i++)
   {
     //  ifile.read((char *)&temp, sizeof(temp));
       scanf("%s",&temp);
   for(j=0;j<4;j++)
   {
    a[i][j]=temp[j];
   if(a[i][j]=='.')
    countd+=1;
   }
   }

for(i=0;i<4;i++)
   {
     countt=0;
countx=0;
counto=0;
for(j=0;j<4;j++)
{   if(a[i][j]=='X')
    countx+=1;
    else if (a[i][j]=='O')
    counto+=1;
    else if(a[i][j]=='T')
    countt+=1;
}

    if(countx==4)
{   //ofile.write((char *)&obj, sizeof(obj));
    printf("Case #%d: X won\n\n",k);
    flag=1;
    break;
}

if(counto==4)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    break;
}

if(countx==3 && countt==1)
{
    printf("Case #%d: X won\n\n",k);
    flag=1;
    break;
}

if(counto==3 && countt==1)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    break;
}
}

if (flag==1)
continue;
else
{
    for(j=0;j<4;j++)
   {
countt=0;
countx=0;
counto=0;
for(i=0;i<4;i++)
{   if(a[i][j]=='X')
    countx+=1;
    else if (a[i][j]=='O')
    counto+=1;
    else if(a[i][j]=='T')
    countt+=1;
        }


if(countx==4)
{
    printf("Case #%d: X won\n\n",k);
    flag=1;
    break;
}

if(counto==4)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    break;
}
if(countx==3 && countt==1)
{
    printf("Case #%d: X won\n\n",k);
    flag=1;
    break;
}
if(counto==3 && countt==1)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    break;
}
   }
}
if(flag==0)
{countt=0;
countx=0;
counto=0;
for(i=0;i<4;i++)
 {
     if(a[i][i]=='X')
    countx+=1;
    else if (a[i][i]=='O')
    counto+=1;
    else if(a[i][i]=='T')
    countt+=1;
        }
if(countx==4)
{
    printf("Case #%d: X won\n\n",k);
    flag=1;
    continue;
}

if(counto==4)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    continue;
}
if(countx==3 && countt==1)
{
    printf("Case #%d: X won\n\n",k);
    flag=1;
    continue;
}
if(counto==3 && countt==1)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    continue;
}
 }
if(flag==0)
{countt=0;
countx=0;
counto=0;
for(i=0;i<4;i++)
 {
     if(a[i][3-i]=='X')
    countx+=1;
    else if (a[i][3-i]=='O')
    counto+=1;
    else if(a[i][3-i]=='T')
    countt+=1;
        }
if(countx==4)
{
    printf("Case #%d: X won\n\n",k);
    flag=1;
    continue;
}

if(counto==4)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    continue;
}
if(countx==3 && countt==1)
{
    printf("Case #%d: X won\n\n",k);
    flag=1;
    continue;
}
if(counto==3 && countt==1)
{
    printf("Case #%d: O won\n\n",k);
    flag=1;
    continue;
}
 }
 if(flag==0)
{
    if(countd==0)
        printf("Case #%d: Draw\n\n",k);
    else
        printf("Case #%d: Game has not completed\n\n",k);

   }



}
return 0;
}
