# include <bits/stdc++.h>
using namespace std;
int main(void)
{
    int test;
    scanf("%d",&test);
    int testcount=1;
    while(test--)
    {
        int ans=0,init=0,i=0;
        string s;
        cin>>s;
        bool flag=0;
        if(s[i]=='-')
        {
            while(s[i]=='-')
                i++;
            ans++;
            init=i;
        }
        for(int k=init;k<s.length();k++)
        {
                int count=k;
                while(s[count]=='+')
                {
                    count++;
                    if(count==s.length())
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                    break;
                while(s[count]=='-')
                    count++;
                k=count-1;
                ans=ans+2;
        }
        printf("Case #%d: %d\n",testcount,ans);
        testcount++;
    }
    return 0;
}
