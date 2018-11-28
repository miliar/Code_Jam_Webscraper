#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
#define LL long long
char str[110];
int t,m,ans;
bool check(char s[])
{
    for(int i=0; i<strlen(s); i++)
    {
        if(s[i]=='-')return false;
    }
    return true;
}
void work(char s[])
{
    int i;
    for(i=strlen(s)-1; i>=0; i--)
    {
        if(s[i]=='-')break;
    }
    if(s[0]=='+')
    {
        s[0]='-';
        ans++;
        //cout<<s<<endl;
    }
    char tmp[110];
    for(int j=0; j<=i; j++)
    {
        if(s[j]=='+')tmp[i-j]='-';
        else tmp[i-j]='+';
    }
    for(int j=0; j<=i; j++)
    {
        s[j]=tmp[j];
    }
    //cout<<s<<endl;
    ans++;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int o=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",str);
        //cout<<"***  "<<str<<"  ***"<<endl;
        ans=0;
        for(int i=strlen(str)-1;i>=0;i--)
        {
            if(str[i]=='+')
            {
                if(ans%2==1)ans++;
            }
            else
            {
                if(ans%2==0)ans++;
            }
        }
        printf("Case #%d: %d\n",++o,ans);
    }
}








