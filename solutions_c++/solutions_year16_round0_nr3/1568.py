#include <iostream>
#include<cstdio>

using namespace std;

long long poiskdel(long long n)
{
    long long i=2;
    while(i*i<=n){if(!(n%i)) return i;i++;}
    return 0;
}

long long perevod(int osn,int *b,int n)
{
    long long rez=0,pow=1;
    for(int i=0;i<n;i++)
    {
        rez+=pow*b[i];
        pow*=osn;
    }
    return rez;
}

int main()
{
    FILE* out=fopen("C-large.out","w");
    int a[16];
    a[15]=a[0]=1;
    for(int i=1;i<15;i++) a[i]=0;
    bool fl=true;
    int kol=0;
    fprintf(out,"Case #1:\n");
    while(fl&& kol<500)
    {
        bool prov=true;
        long long b[11];
        for(int i=2;i<=10 && prov;i++)
        {
            long long dec=perevod(i,a,16);
            long long del=poiskdel(dec);
            if(!del) prov=false;
            else b[i]=del;
        }
        if(prov)
        {
            kol++;
            for(int i=15;i>=0;i--) fprintf(out,"%d",a[i]);for(int i=15;i>=0;i--) fprintf(out,"%d",a[i]);
            fprintf(out," ");
            for(int i=2;i<=10;i++) fprintf(out,"%d ",b[i]);
            fprintf(out,"\n");
        }
        fl=false;
        for(int i=0;i<=15;i++) if(!a[i]) fl=true;
        if(!fl) break;
        int i=1;
        a[i]++;
        while(a[i]>1){a[i]=0;a[++i]++;}
    //выводить в обратном порядке!
    }
    //fprintf(out,"%d\n",kol);
    return 0;
}
