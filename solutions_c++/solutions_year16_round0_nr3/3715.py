#include<stdio.h>
#include<string.h>
#include<math.h>

long long tmp[12],pr[5761456];
int N =100000009,in=0;
int status[100000009/32];

bool check(int N,int pos){return (bool)(N & (1<<pos));}
int Set(int N,int pos){	return N=N | (1<<pos);}

void sieve()
{
     int i,j,m;
     m=int(sqrt(N));
     for(i=3;i<=m;i+=2)
		 if(check(status[i/32],i%32)==0)
	 		 for(j=i*i;j<=N;j+=2*i)
				 status[j/32]=Set(status[j/32],j%32);
	 pr[in++]=2;
	 for(i=3;i<N;i+=2)
		 if( check(status[i/32],i%32)==0)
            pr[in++]=i;
}

long long dv(long long v)
{
    int i;
    for(i=0;pr[i]*pr[i]<=v;i++)
        if(v%pr[i]==0)
            return pr[i];
    return v;
}

int main()
{
    freopen("C-small-attempt.in","r",stdin);
    freopen("Csmall.txt","w",stdout);
    int i,j,k,l,m,t,flag,flagp,cnt;
    long long b,n;
    char s[20],w[20];
    sieve();
    printf("Case #1:\n");
    cnt=0;
    for(k=1;k<16384;k++)
    //for(k=1;k<109;k++)
    {
        n=k;
        in=0;
        while(n)
        {
            b=n%2;
            n=n/2;
            s[in++]=b+48;
        }
        for(in=in;in<14;in++)
            s[in]=48;
        s[in]=0;
        w[0]=49;
        for(i=1,j=in-1;j>=0;j--,i++)
            w[i]=s[j];
        w[i++]=49;
        w[i]=0;
        //printf("%s\n",w);
        flag=1;
        b=0;
        for(i=2;i<=10;i++)
        {
            b=0;
            for(l=0,j=15;j>=0;j--,l++)
                b+=pow(i,l)*(w[j]-48);
            //printf("%d %lld\n",i,b);
            if(dv(b)!=b)
                tmp[i]=b;
            else
            {
                flag=0;
                break;
            }
        }
        if(flag)
        {
            printf("%s",w);
            for(j=2;j<=10;j++)
                printf(" %lld",dv(tmp[j]));
            printf("\n");
            cnt++;
            if(cnt==50)
                break;
        }
    }
    return 0;
}
