#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int t,l,a[100],d[100];
char s[5000];
int main()
{
    scanf("%d",&t);
    for (int i=1; i<=t; i++)
    {
        scanf("%s",&s);
        l=strlen(s);
        for (int j=0; j<l; j++)
        d[s[j]]++;
        a[0]=d['Z'];
        d['E']-=d['Z']; d['R']-=d['Z']; d['O']-=d['Z']; d['Z']=0;
        a[8]=d['G'];
        d['E']-=d['G']; d['I']-=d['G']; d['H']-=d['G']; d['T']-=d['G']; d['G']=0;
        a[6]=d['X'];
        d['S']-=d['X']; d['I']-=d['X']; d['X']=0;
        a[4]=d['U'];
        d['F']-=d['U']; d['O']-=d['U']; d['R']-=d['U']; d['U']=0;
        a[5]=d['F'];
        d['I']-=d['F']; d['V']-=d['F']; d['E']-=d['F']; d['F']=0;
        a[7]=d['V'];
        d['S']-=d['V']; d['E']-=2*d['V']; d['N']-=d['V']; d['V']=0;
        a[9]=d['I'];
        d['N']-=2*d['I']; d['E']-=d['I']; d['I']=0;
        a[3]=d['R'];
        d['T']-=d['R']; d['E']-=2*d['R']; d['H']-=d['R']; d['R']=0;
        a[2]=d['T'];
        d['W']-=d['T']; d['O']-=d['T']; d['T']=0;
        a[1]=d['E'];
        d['O']-=d['E']; d['N']-=d['E']; d['E']=0;
        printf("Case #%d: ",i);
        for (int j=0; j<=9; j++)
        for (int k=1; k<=a[j]; k++)
        printf("%d",j);
        printf("\n");
        for (int j='A'; j<='Z'; j++)
        d[j]=0;
        for (int j=0; j<=9; j++)
        a[j]=0;
    }
    return 0;
}
