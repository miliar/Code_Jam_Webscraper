#include<stdio.h>
#include<string.h>

int main()
{int T;
scanf("%d",&T);
for(int i=0;i<T;i++)
{char S[10];
scanf("%s",&S);
int l=strlen(S);
int a=0,count=0;
while(a<l)
{if(S[a]==S[0])
{a++;
}
else
{count=count+1;
S[0]=S[a];
a++;
}}
if(S[0]=='-')
{count++;
}
printf("CASE #%d: %d \n",i+1,count);
}return 0;
}
