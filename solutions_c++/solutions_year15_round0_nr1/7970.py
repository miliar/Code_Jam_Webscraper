#include<bits/stdc++.h>

using namespace std;

int main()
{

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,i,n,c;
    char s[1005];

    scanf("%d",&t);

    c=t;

    while(t--)
    {

        //scanf("%d %s",&n,s);
        cin>>n;
        cin>>s;

        int sum=0,ans=0;

        for(i=0;i<=n;i++)
        {

            if(i!=0)
            sum=sum+s[i-1]-'0';

            if(sum>=i || s[i]=='0')
            {

                continue;

            }
            else {


                ans=ans+i-sum;
                sum=sum+(i-sum);

            }

        }

        printf("Case #%d: %d\n",c-t,ans);

    }

    return 0;

}


























