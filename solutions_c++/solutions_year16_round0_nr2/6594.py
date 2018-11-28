#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int main()
{
    int t,cnt,i;
    string s;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        cnt=0;
        cin>>s;
        int len=s.length(),flag;
        (s[0]=='+')?flag=1:flag=0;
        for(i=0;i<len-1;i++)
        {
            if(s[i]==s[i+1])continue;
            cnt++;
            flag=!flag;
        }
        if(flag==0)cnt++;
        printf("Case #%d: %d\n",test,cnt);
    }
}
