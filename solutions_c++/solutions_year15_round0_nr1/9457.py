#include <stdio.h>
using namespace std;

int main()
{
freopen("A-large.in","r",stdin);
FILE*fout=fopen("A-large.out","w");
unsigned short T,x,M,I,S,c;
scanf("%hu",&T);
for(x=1;x<=T;x++)
{
scanf("%hu",&M);
c=getchar();
I=S=0;
for(c=0;c<=M;c++)
{
if(S<c)
{
I+=c-S;
S=c;
}
S+=getchar()-'0';
}
fprintf(fout,"Case #%hu: %hu\n",x,I);
}
fclose(fout);
return(0);
}
