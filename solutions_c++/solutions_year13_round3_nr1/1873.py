#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#define fori(a) for(i=0;i<a;i++)
#define forj(a) for(j=0;j<a;j++)
#define fork(a,b) for(k=a;k<b;k++)
int main()
{
    int t,i,j,k,n,ans,count,l,m,flag;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    //printf("%d\n",t);
    fori(t)
    {
        char s[110];
        scanf("%s %d",s,&n);
        ans=0;
        l=strlen(s);
        forj(l-n+1)
        {
            //puts("Here");
            k=j;
            //printf("%c\n",s[j]);
            while(k<l-n+1)
            {
                flag=1;
                for (m=k; m<k+n; m++)
                {
                    //printf("%c\n",s[m]);
                    if (s[m]=='a'||s[m]=='e'||s[m]=='i'||s[m]=='o'||s[m]=='u')
                    {
                        flag=0;
                        break;
                    }
                }
                //printf("flag=%dn",flag);
                if (flag==1)
                {
                    //printf ("incr=%d\n",l-k-n+1);
                    ans+=(l-k-n+1);
                    break;
                }
                else k++;
            }
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
