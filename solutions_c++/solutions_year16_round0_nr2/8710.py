#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("ques.in","r",stdin);
    freopen("ans.txt","w",stdout);
    //fflush(stdin);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        char s[100009];
        scanf("%s",s);
        int n=strlen(s);
        int ans=0;
        for(int i=n-1;i>=0;i--)
        {
            if(ans%2==0)
            {
                if(s[i]=='-')
                    ans++;
            }
            else
            {
                if(s[i]=='+')
                    ans++;
            }
        }
        cout<<"Case #"<<tt<<": "<<ans<<"\n";
    }
    return 0;
}
