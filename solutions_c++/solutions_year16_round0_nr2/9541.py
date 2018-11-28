#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,cnt,j,n,k;
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cnt=0;
        string s;
        cin>>s;
        n=s.length();
        i=0;
        while(s[i]=='-')
            i++;
        if(i!=0)
            cnt++;
        for(j=i;j<n;)
        {
            if(s[i]=='+')
            {
                while(s[j]!='-' && j<n)
                    j++;
                if(s[j]=='-' && j<n)
                    cnt+=2;
                while(s[j]!='+' && j<n)
                    j++;

            }

        }
        printf("Case #%d: %d\n",k,cnt);

    }
}
