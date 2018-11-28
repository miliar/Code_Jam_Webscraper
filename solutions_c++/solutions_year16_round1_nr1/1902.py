#include<bits/stdc++.h>

using namespace std;

#define std::cout cout;
#define std::cin cin;

int main()
{
	int i,j,t,cases,len;
	char s[1000],ans[1001],temp;
	freopen("problem1 large.in","r",stdin);
    freopen("problem1 large.out","w",stdout);
    scanf("%d",&cases);
    for(t=1;t<=cases;t++)
    {
    cin>>s;
    len=strlen(s);
    for(i=0;i<1000;i++)
    {
        ans[i]='0';
    }
    ans[0]=s[0];
    for(i=1;i<len;i++)
    {
        if((s[i]-'A')>=(ans[0]-'A'))
        {
            for(j=len-1;j>0;j--)
            {
                ans[j]=ans[j-1];
            }
            ans[0]=s[i];
        }
        else
        {
            ans[i]=s[i];
        }
    }
    printf("Case #%d: ",t);
    for(i=0;i<len;i++)
    {
        printf("%c",ans[i]);
    }
    printf("\n");
    }
	return 0;
}
