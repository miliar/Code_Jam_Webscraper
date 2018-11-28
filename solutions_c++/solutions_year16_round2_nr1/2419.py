#include<stdio.h>
#include<string.h>

int cnt[30],ans[30];
char more[10][10]={"ZERO","TWO","FOUR","FIVE","ONE","THREE","SIX","SEVEN","EIGHT","NINE"};
char s[2020],out[2020];

int n[10]={0,2,4,5,1,3,6,7,8,9};
char a[10]={'Z','W','U','F','O','R','X','V','G','I'};



int main()
{
     freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ti,l,i,j,k;
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        scanf("%s",s);
        l=strlen(s);
        memset(cnt,0,sizeof(cnt));
        memset(ans,0,sizeof(cnt));
        for(i=0; i<l; ++i)
        {
            cnt[s[i]-'A']++;
        }
        for(i=0; i<10; ++i)
        {
            j=a[i]-'A';
            ans[n[i]]=cnt[j];
            k=strlen(more[i]);
            --k;
            while(k>=0){
                j=more[i][k]-'A';
                cnt[j]-=ans[n[i]];
                --k;
            }
        }
       // puts("p");
        j=0;
        for(i=0; i<10; ++i)
        {
            while(ans[i])
            {
                out[j++]=i+'0';
                --ans[i];
            }
        }
        out[j]='\0';
        printf("Case #%d: %s\n",ti,out);
    }
    return 0;
}
