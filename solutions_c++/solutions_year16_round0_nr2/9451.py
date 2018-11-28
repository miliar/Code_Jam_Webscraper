#include<stdio.h>
#include<stdlib.h>
//#define gc() getchar_unlocked()
//#define pc(x) putchar_unlocked(x)
#define gc() getchar()
#define pc(x) putchar(x)
#define endl '\n'
char s[6];
inline int fast_scan(){
    int x = 0;
    char c = gc();
    while(c <'0' || c >'9') c = gc();
    while(c >='0' && c <='9'){
        x = x * 10 + (c - '0');
        c = gc();
    }
    return x;
}
inline void fast_print(int n){

    int i = 0;
    do{
        s[i++] = (char)(n%10 + '0');
        n /= 10;
    }while(n > 0);
    --i;
    while(i >= 0) pc(s[i--]);
}

void flip(bool *b,int index)
{
    int i=0,temp;
    while(i<=index)
    {
        if(i==index)
        {
            b[i]=!b[i];
            break;
        }
        else
        {
            temp=b[i];
            b[i++]=!b[index];
            b[index--]=!temp;
        }
    }
}
int main()
{
    int t,i,j,bottom,top=0,temp,nextp,blen,tlen,loopc,flag;
    bool *a;
    a=(bool*)calloc(101,sizeof(bool));
    t=fast_scan();
    for(int i=1;i<t+1;i++)
    {
        char c= getchar();
        blen=0;
        while(c!='\n')
        {
            if(c=='+') a[blen++]=1;
            else a[blen++]=0;
            c=getchar();
        }
        tlen=blen;
        loopc=0;
        bottom=blen-1;
        while(1)
        {
            temp=0;
            for(j=0;j<blen;j++) temp+=a[j];
            if (temp==blen) break;
            while(bottom>=0 && a[bottom]) bottom--;
            if(!a[top]) flip(a,bottom);
            else
            {
                flag=0;
                for(nextp=bottom;nextp>=0;nextp--)
                {
                    if(a[nextp])
                    {
                        flip(a,nextp);
                        flag=1;
                        break;
                    }
                }
                if(!flag) flip(a,0);
            }
            loopc++;
        }
        printf("Case #%d: %d\n",i,loopc);
    }

    return 0;
}
