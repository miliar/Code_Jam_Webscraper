#include<stdio.h>
using namespace std;
int p=1;


char mul(char,char);
char mul(char a,char b)
{
    char ch='1';
if(a=='1')return b;
else if(a==b)p*=-1;
else if(a=='i'&&b=='j')ch='k';
else if(a=='j'&&b=='k')ch='i';
else if(a=='k'&&b=='i')ch='j';
else if(a=='j'&&b=='i'){ch='k';p*=-1;}
else if(a=='k'&&b=='j'){ch='i';p*=-1;}
else if(a=='i'&&b=='k'){ch='j';p*=-1;}
return ch;

}


main()
{
    int t=0,f=0;
    char arr[4]={'i','j','k','1'};

    scanf("%d",&t);

    int i=0,l,x;
    char a[10005],ch='i',c='1';
for(i=0;i<t;i++)
{
p=1;
//ch='i';
c='1';
f=0;
scanf("%d %d",&l,&x);
scanf("%s",&a);

for(int k=0;k<x;k++)
{for(int j=0;j<l;j++)
{

//    printf("mul(%c,a[%d])\n",c,j);
 c=mul(c,a[j]);

 if(c==arr[f])
{
    f++;
    c='1';
}

}
}
//printf("%c %d %d", c, p, f);

if(c=='1'&&p==1&&(f==3 || f==4)) printf("Case #%d: YES\n",i+1);
else printf("Case #%d: NO\n",i+1);
}
return 0;
}
