#include<stdio.h>
#include<string.h>
int coun[28],nu[10];
int main()
{
    int t,i,j,l,k;
    char st[3000];
FILE *fptr,*op;
fptr=fopen("a.txt","r");
op=fopen("co2.txt","w");
op=fopen("co2.txt","a");
fscanf(fptr,"%d",&t);
for(j=1;j<=t;j++)
{
for(i=0;i<26;i++)
coun[i]=0;
for(i=0;i<10;i++)
nu[i]=0;
fscanf(fptr,"%s",st);
l=strlen(st);
for(i=0;i<l;i++)
++coun[st[i]-'A'];
nu[0]=coun[25];
nu[2]=coun['W'-'A'];
nu[4]=coun['U'-'A'];
nu[6]=coun['X'-'A'];
nu[8]=coun['G'-'A'];
nu[1]=coun['O'-'A']-nu[0]-nu[2]-nu[4];
nu[3]=coun['H'-'A']-nu[8];
nu[5]=coun['F'-'A']-nu[4];
nu[7]=coun['S'-'A']-nu[6];
nu[9]=coun['I'-'A']-nu[5]-nu[6]-nu[8];

 fprintf(op,"Case #%d: ",j);
 for(i=0;i<10;i++)
    for(k=0;k<nu[i];k++)
    fprintf(op,"%d",i);
 fprintf(op,"\n");
}

return 0;
}

