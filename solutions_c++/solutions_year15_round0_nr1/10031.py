#include<stdio.h>
int main()
{ 
char inp;
int j,i,t,s,standing,invite;
scanf("%d",&t);
i=0;
while(i<t)
{ i++;
scanf("%d",&s);scanf("%c",&inp);
for(j=0,standing=0,invite=0;j<s+1;j++)
{ scanf("%c",&inp);//printf("%c",inp);
if(inp!='0')
{if(j<=standing){standing+=(inp-'0');}
else
invite+=j-standing;
}
}
printf("Case #%d: %d\n",i,invite);
}
return 0;
}
