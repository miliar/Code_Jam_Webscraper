#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int a[11]={0,2,4,6,8,1,3,5,7,9},b[100];
int c[11]={90,87,85,88,71,79,84,70,83,78};
char str[12][10]={"ZERO","TWO","FOUR","SIX","EIGHT","ONE","THREE","FIVE","SEVEN","NINE"};

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int i,j,t,len,in,co=1;
    char s[2009],w[2009];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        in=0;
        len=strlen(s);
        memset(b,0,sizeof(b));
        for(i=0;i<len;i++)
            b[s[i]]++;
        for(i=0;i<10;i++)
        {
            while(b[c[i]])
            {
                w[in++]=a[i]+48;
                for(j=0;str[i][j]!=0;j++)
                    b[str[i][j]]--;
            }
        }
        w[in]=0;
        sort(w,w+in);
        printf("Case #%d: %s\n",co++,w);
    }
    return 0;
}
