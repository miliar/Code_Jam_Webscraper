#include<cstdio>
#include<cstring>
using namespace std;
char s[]={'a','e','i','o','u'};
char l[1000110];
int max[1000110];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("text.out","w",stdout);
    int T,n,ca=1;
    int i,j,k,len,flag,v;
    long long sum;
    scanf("%d",&T);
    while(T--)
    {
       scanf("%s%d",l,&n);
        for(k=0,sum=0;k<5;k++)
        if(s[k]==l[0])break;
        if(k==5)max[0]=1;
        else max[0]=0;
        len=strlen(l);
        if(n==1&&max[0]==1){flag=0;sum++;}
        else flag=-1;
       for(i=1;l[i]!='\0';i++){
            for(k=0;k<5;k++)
            if(s[k]==l[i])break;
            if(k==5)
            max[i]=max[i-1]+1;
            else max[i]=0;

            if(max[i]>=n)
            {
                sum+=(i+2-n);
                flag=i;
            }
            else if(flag!=-1)sum+=flag+2-n;
       }
       len=i;
        printf("Case #%d: %lld\n",ca++,sum);
    }
    return 0;
}
