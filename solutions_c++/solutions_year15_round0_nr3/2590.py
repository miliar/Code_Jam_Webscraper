#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>

using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define p(n) printf("%d ",n)
#define pl(n) printf("%ld ",n)
#define pll(n) printf("%lld\n",n)
#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,a,b)   for(i=a;i>=b;i--)
# define toint(n)   (n-'0')
typedef long long ll;

char mul(char b, char a, ll *flag)
{
    if((a=='i')&&(b=='j'))
        return 'k';
    else if((a=='j')&&(b=='k'))
        return 'i';
    else if((a=='k')&&(b=='i'))
        return 'j';
    else if((a=='j')&&(b=='i'))
    {(*flag)*=-1; ;return 'k'; }
    else if((a=='i')&&(b=='k'))
    {(*flag)*=-1; return 'j'; }
    else if((a=='k')&&(b=='j'))
    {(*flag)*=-1; return 'i';}
    else if(a==b)
        {(*flag)*=-1; return'1';}
    else if(a=='1')
        return b;
    else
        return a;
}

bool Solve(char *s, ll beg)
{
    ll i,j,k,flag;
    char basei,basej,basek;
    
    basei=basej=basek='1';
    
    //printf("len: %d\n",strlen(s));
    flag=1;
    fo(i,beg,strlen(s))						// for i
    {
        basei=mul(s[i],basei,&flag);
        if((basei=='i')&&(flag==1))
            {i++;break;}
    }
    if(i==strlen(s))
        return 0; //printf("@");
    
    flag=1;
    fo(j,i,strlen(s))							// for j
    {
        basej=mul(s[j],basej,&flag);
        //printf("check J: %lld %c\n",j,basej);
        if((basej=='j')&&(flag==1))
            {j++;break;}
    }
    if(j==strlen(s))
        return 0; //printf("@");
    
    flag=1;
    fo(k,j,strlen(s))							// for k
    {
        //printf("s[k]: %c  base K: %c\n",s[k],basek);
        basek=mul(s[k],basek,&flag);
        //printf("check K: %lld %c flag: %lld\n",k,basek,flag);
    }//printf("@");
    if((basek!='k')||(flag!=1))
        return 0;
    
    return 1;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,z;
    ll x,len,i;
    char *s,*snew;
    s(t);
    fo(z,1,t+1)
    {
        sll(len);	sll(x);
        
        s=(char*)malloc(len*sizeof(char));
        snew=(char*)malloc(x*len*sizeof(char));
        scanf("%s",s);
        
        fo(i,0,x*len)
            snew[i]=s[i%len];
        
        //printf("%s\n",snew);
        if(Solve(snew,0))
            printf("Case #%d: YES\n",z);
        else
            printf("Case #%d: NO\n",z);
    }
    return 0;
}