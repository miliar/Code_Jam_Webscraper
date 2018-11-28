#include <cstdio>
#include <cstring>
using namespace std;
long long int t,cnt,flag;
char s[100000];
int main()
{
    scanf("%lld",&t);
    for(int j=1;j<=t;j++)
    {
     scanf("%s",s);
     cnt=0;
     flag=0;
     for(int i=0;i<strlen(s);i++)
     {
     if(s[i]=='-'){flag=1;if(i!=0 && s[i+1]!='-')cnt++;else if(i==0){while(s[i+1]=='-')i++;} else{while(s[i+1]=='-')i++;cnt++;} }
     else if(flag==1 && s[i]=='+'){cnt++;flag=0;}
     }
     if(s[strlen(s)-1]=='-')cnt++;
     printf("Case #%d: %lld\n",j,cnt);
    }
    return 0;
}
