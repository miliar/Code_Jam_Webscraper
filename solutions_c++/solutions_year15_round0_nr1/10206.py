#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#define getcx getchar_unlocked
#define pc(x) putchar_unlocked(x)
#ifndef ONLINE_JUDGE
    #define getcx getchar
    #define pc(x) putchar(x)
#endif // ONLINE_JUDGE
using namespace std;
#define ull unsigned long long int
#define lli long long int
#define li long int
#define ii int
#define mod 1000000007

inline int inp()
{
    int n=0;
    int ch=getcx();
    int sign=1;
    while(ch<'0' || ch>'9')
    {
        if(ch=='-')
            sign=-1;
        ch=getcx();
    }
    while(ch>='0' && ch<='9')
        n=(n<<3)+(n<<1)+ ch-'0',ch=getcx();
    return n*sign;
}

inline long long in()
{
    long long n=0;
    long long ch=getcx();
    long long sign=1;
    while(ch<'0' || ch>'9')
    {
        if(ch=='-')
            sign=-1;
        ch=getcx();
    }
    while(ch>='0' && ch<='9')
        n=(n<<3)+(n<<1)+ch-'0',ch=getcx();
    return n*sign;
}

inline void write(lli n)
{
    lli N=n,rev,count=0;
    rev=N;
    if(N==0)
    {
        pc('0');
        pc('\n');
        return;
    }
    while((rev%10)==0)
    {
        count++;
        rev/=10;
    }
    rev=0;
    while(N!=0)
    {
        rev=(rev<<3)+(rev<<1)+N%10;
        N/=10;
    }
    while(rev!=0)
    {
        pc(rev%10 + '0');
        rev/=10;
    }
    while(rev!=0)
    {
        pc(rev%10+'0');
        rev/=10;
    }
    while(count--)
        pc('0');
}

int main()
{
    int t,c,i,n,m,cnt,j=1,k;
    char ch;
    char s[1001];
    FILE *f,*fp;
    //t=inp();
    f=fopen("A-small-attempt4.in","r");
    fp=fopen("A-small.txt","w");
    fscanf(f,"%d",&t);
    while(t--)
    {
        //n=inp();
        fscanf(f,"%d %s\n",&n,s);
        n++;
        i=0;
        c=0;
        cnt=0;
        for(k=0;k<=n;k++)
        {
            ch=s[k];
            //cout<<s[k];
            m=ch-'0';
            if(c<i)
              {
                  cnt+=(i-c);
                  c+=(i-c);
              }
            c+=m;
            i++;
        }
        //cout<<"\n";
        /*cout<<"Case #";
        write(j);
        cout<<": ";
        write(cnt);
        cout<<"\n";*/
        fprintf(fp,"Case #%d: %d\n",j,cnt);
        j++;
    }
    fclose(f);
    fclose(fp);
    return 0;
}
