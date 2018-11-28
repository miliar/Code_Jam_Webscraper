#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<iostream>
using namespace std;
int main(void)
{
    int T,s_max,counter,ans;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        ans=counter=0;
        string s;
        scanf("%d ",&s_max);
        cin>>s;
        counter=s[0]-'0';
        for(int l=1;l<s.length();l++)
        {
            if(counter<l && s[l]-'0'>0)
            {
                ans+=l-counter;
                counter=l;
            }
            counter+=s[l]-'0';
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
