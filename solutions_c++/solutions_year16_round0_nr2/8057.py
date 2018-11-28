#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long int i,j,k,t,ans=0,o;
    scanf("%lld",&t);
    for(o=1;o<=t;o++)
    {
        char s[10000],b[10000]={'\0'};
        scanf("%s",s);
        i=strlen(s)-1;
        j=0;
        while(i>=0)
        {
            char c=s[i];
            b[j++]=c;
            while(c==s[i]) i--;

        }
        b[j]='\0';
        i=0;
        while(b[i]=='+') i++;
        printf("Case #%lld: %lld\n",o,(j-i));
    }
    return 0;
}
