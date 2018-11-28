#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int ccnt=0;
void flip(char* a)
{
    int s = strlen(a);
    for(int i=0;i<s/2;i++)
    {
        char tmp = a[i];
        a[i]=a[s-i-1];
        a[s-i-1]=tmp;
    }
}
bool chkp(unsigned long long a)
{
    for(int i=2;i<5000;i++)
    {
        if(a%i==0)
            return false;
    }
    return true;
}
void aaa(unsigned long long a)
{
     for(int i=2;i<5000;i++)
    {
        if(a%i==0)
        {
            printf("%d ",i);
            return;
        }
    }
    return;
}
unsigned long long con(char* a,int n)
{
    unsigned long long res=1;
    for(int i=1;i<16;i++)
    {
        if(a[i]=='1')
        {
            unsigned long long tmp=1;
            for(int j=0;j<i;j++)
            {
                tmp*=n;
            }
            res+=tmp;
        }
    }
    //printf("%llu\n",res);
    return res;
}
void fn(int cnt,char* a,int pos)
{
    if(cnt>=14)
    {
        //flip(a);
        for(int i=2;i<11;i++)
        {
            if(chkp(con(a,i)))
                return;
        }
        flip(a);
        printf("%s ",a);
        flip(a);
        for(int i=2;i<11;i++)
        {
            aaa(con(a,i));
        }
        printf("\n");
        ccnt++;
        if(ccnt>=50)exit(0);
        //flip(a);
        return;
    }
    a[pos]='0';
    fn(cnt+1,a,pos+1);
    a[pos]='1';
    fn(cnt+1,a,pos+1);
}
main()
{
    printf("Case #1:\n");
    char a[]="1000000000000001";
    //genp();
    fn(0,a,1);
}
