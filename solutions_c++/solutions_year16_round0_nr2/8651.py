#include<stdio.h>
#include<string.h>
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long int tt;
    scanf("%lld", &tt);
    for (long long int qq=1;qq<=tt;qq++)
    {
        printf("Case #%lld: ", qq);
        char s[110],a[110];
        int len,i,j,flag=0,c=0;
        scanf("%s",s);
        len=strlen(s);
	   a[0]=s[0];
	   j=1;
        for(i=0;i<len-1;i++)
        {
            if(s[i]==s[i+1])
                continue;
            a[j++]=s[i+1];
        }
        a[j]='\0';
        len=strlen(a);
        if(a[0]=='-')
            flag=1;
        for(i=0;i<len;i++)
        {
            if(a[i]=='-')
                c++;
        }
        printf("%d\n",2*c-flag);
	}
	return 0;
}
