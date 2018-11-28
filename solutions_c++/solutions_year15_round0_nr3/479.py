#include<cstdio>
#include<algorithm>

using namespace std;

int sign(int p)
{
    return p>0?1:-1;
}
int cal(int p,int q)
{
    int pp=abs(p),qq=abs(q);
    if(pp==1)   return sign(p)*q;
    if(qq==1)   return sign(q)*p;
    if(pp==2)
    {
        if(qq==2)       return sign(p)*sign(q)*-1;
        else if(qq==3)  return sign(p)*sign(q)*4;
        else            return sign(p)*sign(q)*-3;
    }
    else if(pp==3)
    {
        if(qq==2)       return sign(p)*sign(q)*-4;
        else if(qq==3)  return sign(p)*sign(q)*-1;
        else            return sign(p)*sign(q)*2;
    }
    else
    {
        if(qq==2)       return sign(p)*sign(q)*3;
        else if(qq==3)  return sign(p)*sign(q)*-2;
        else            return sign(p)*sign(q)*-1;
    }
}
int cti(char c)
{
    if(c=='i')      return 2;
    else if(c=='j') return 3;
    else            return 4;
}

bool ch;
long long t,l,x,g,b[60005],ml,c,sg;
char s[60005];

int main()
{
//    freopen("C-large.in","r",stdin);
//    freopen("C_out_large.txt","w",stdout);
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        scanf("%d%d%s",&l,&x,s);
        ch=false;
        sg=1;
        for(int i=0;i<l;i++)    sg=cal(sg,cti(s[i]));
        if(x>6)
        {
            if(x%2==0)
            {
                if((x-6)%4==0)  sg=1;
                else            sg=cal(sg,sg);
                x=6;
            }
            else
            {
                if((x-5)%4==0)  sg=1;
                else            sg=cal(sg,sg);
                x=5;
            }
        }
        else    sg=1;
        for(int i=0;i<l;i++)
        {
            for(int j=1;j<x;j++)    s[j*l+i]=s[i];
        }
        ml=l*x;
        b[ml-1]=cti(s[ml-1]);
        for(int i=ml-2;i>=0;i--)    b[i]=cal(cti(s[i]),b[i+1]);
        c=1;
        for(int i=0;i<2*l&&i<ml-2;i++)
        {
            c=cal(c,cti(s[i]));
//            printf("c: %d\n",c);
            if(abs(c)==2)
            {
                g=1;
                for(int j=0;j<2*l&&i+j<ml-2;j++)
                {
                    g=cal(g,cti(s[i+j+1]));
//                    printf("--> g: %d and b: %d\ncheck: %d\n",g,b[i+j+2],sg);
                    if(abs(g)==3&&abs(b[i+j+2])==4&&sg*sign(c)*sign(g)*sign(b[i+j+2])==1)  ch=true;
                    if(ch)  break;
                }
                if(ch)  break;
            }
            if(ch)  break;
        }
        if(ch)  printf("Case #%d: YES\n",z);
        else    printf("Case #%d: NO\n",z);
    }
    return 0;
}
