#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    char s[105];

   long long int t,l,i,j,k,cnt,c=1;

    cin>>t;
    getchar();

    while(t--)
    {
        gets(s);

        l=strlen(s);
        cnt=0;
        for(i=l-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                cnt++;
                for(j=i;j>=0;j--)
                {
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
        }
        printf("Case #%lld: %lld\n",c,cnt);
        c++;
    }


}
