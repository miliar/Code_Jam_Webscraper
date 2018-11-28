#include<cstdio>

int t,s,l[1100];

void input()
{
scanf("%d",&s);
getchar();
for(int i=0;i<s+1;i++)
{
l[i]=(getchar())-48;
}
getchar();
return;
}


int main()
{
scanf("%d",&t);
int ans,piv=0;

for(int tmp=0;tmp<t;tmp++)
{
piv=0;
ans=0;
input();
for(int i=0;i<s+1;i++)
{
if(piv<i)
{ans=ans+i-piv;
piv=i;}

piv+=l[i];
}
printf("Case #%d: %d\n",tmp+1,ans);

}
return 0;
}

