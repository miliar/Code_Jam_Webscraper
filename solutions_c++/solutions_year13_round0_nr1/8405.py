#include <stdio.h>
int main()
{
int z,x,notyet,one,three,i,j; 
char a[5][5],key;  
scanf("%d",&z);

for(x=0;x<z;x++)
{                

notyet=0;

for(i=0;i<4;i++)
{                
scanf("%s",a[i]);                                              
}



for(i=0;i<4;i++)
{
key=a[i][0];

if(key=='T')
key==a[i][1];

one=0;
three=0;

for(j=0;j<4;j++)
{
if(a[i][j]==key)
three++;
else if(a[i][j]=='T')
one++;
else if(a[i][j]=='.')
notyet++;                
}


if((((three==3)&&(one==1))||three==4)&&(key!='.'))
{
printf("Case #%d: %c won\n",x+1,key);                                    
goto ans;
}                
}

for(j=0;j<4;j++)
{
key=a[0][j];

if(key=='T')
key==a[1][j];

one=0;
three=0;

for(i=0;i<4;i++)
{
if(a[i][j]==key)
three++;
else if(a[i][j]=='T')
one++;
else if(a[i][j]=='.')
notyet++;                
}

if((((three==3)&&(one==1))||three==4)&&(key!='.'))
{
printf("Case #%d: %c won\n",x+1,key);                                  
goto ans;               
}
}


one=0;
three=0;


key=a[0][0];

if(key=='T')
key==a[1][1];

for(i=0;i<4;i++)
{
if(a[i][i]==key)
three++;
else if(a[i][i]=='T')
one++;
else if(a[i][i]=='.')
notyet++;                   
}

if((((three==3)&&(one==1))||three==4)&&(key!='.'))
{
 printf("Case #%d: %c won\n",x+1,key);                                   
goto ans;
}

j=3;
key=a[0][j];

if(key=='T')
key==a[1][2];

one=0;
three=0;


for(i=0;i<4;i++)
{
if(a[i][j]==key)
three++;
else if(a[i][j]=='T')
one++;
else if(a[i][j]=='.')
notyet++;     
j--;              
}

if((((three==3)&&(one==1))||three==4)&&(key!='.'))
{
printf("Case #%d: %c won\n",x+1,key);                                    
goto ans;
}

if(notyet!=0)
printf("Case #%d: Game has not completed\n",x+1);

else
printf("Case #%d: Draw\n",x+1);


ans:
    

      
continue;      
}

return 0;    
}
