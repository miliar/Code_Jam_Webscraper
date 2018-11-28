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

int main()
{
    int t,n,a,b,x,temp,flag,loopc;
    /*


    */
    t=fast_scan();
    for(int i=1;i<t+1;i++)
    {
        n=fast_scan();
        if(!n) printf("Case #%d: INSOMNIA\n",i);
        else
        {
            x=1;
            b=0;
            loopc=0;
            flag=0;
            while(++loopc)
            {
                temp=n*loopc;
                while(temp)
                {
                    a=temp%10;
                    b=b|(1<<a);
                    if(b == 1023)
                    {
                        flag=1;
                        break;
                    }
                    temp/=10;
                }
                if(flag) break;
            }
            printf("Case #%d: %d\n",i,n*loopc);
        }
    }
    return 0;
}
