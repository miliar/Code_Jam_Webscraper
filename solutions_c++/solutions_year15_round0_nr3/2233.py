#include<stdio.h>
#include<string.h>
int res[100000],t;
char mul[8][8]={'a','i','j','k','b','c','d','e',
                'i','b','k','d','c','a','e','j',
                'j','e','b','i','d','k','a','c',
                'k','j','c','b','e','d','i','a',
                'b','c','d','e','a','i','j','k',
                'c','a','e','j','i','b','k','d',
                'd','k','a','c','j','e','b','i',
                'e','d','i','a','k','j','c','b'};
int conv(char x)
{switch(x)
 {case 'a':return 0;
case 'i':return 1;
case 'j':return 2;
case 'k':return 3;
case 'b':return 4;
case 'c':return 5;
case 'd':return 6;
case 'e':return 7;}}
void output()
{int i;
 for(i=0;i<t;i++)
{if(res[i]==3)
 printf("case #%d: YES\n",i+1);
else
printf("case #%d: NO\n",i+1);
}}

int main()
{
 int i,j,k,n,len;
char s[1000000],l;
scanf("%d",&t);
for(i=0;i<t;i++)
{
   scanf("%d%d",&len,&n);
   scanf("%s",s);
   for(j=0;j<n-1;j++)
   strncat(s,s,len);
  
   len=n*len;
   j=0;
   l=s[0];

   while(j<len-1)
 { 
if(l=='i'){j++;res[i]=1;break;}
  else { l=mul[conv(l)][conv(s[j+1])];}
  j++; 
}
    l=s[j];

   while(j<len-1)
 {
 if(l=='j'){j++;res[i]++;break;}
   else {l=mul[conv(l)][conv(s[j+1])];}
   j++;
}
   l=s[j];
   while(j<len-1)
 { 
    
l=mul[conv(l)][conv(s[j+1])];
   j++;
}
if(l=='k')res[i]++;

else res[i]=0;
}
output();
}
 

