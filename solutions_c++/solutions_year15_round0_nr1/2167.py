#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int T,sum,ans,n;
char s[1006];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    cin>>T;
    int t = 0;
    while(t < T)
    {
        t++;
        printf("Case #%d: ",t);
        cin>>n>>s;
        sum = 0;
        ans = 0;
        for(int i=0; i<n+1;i++)
        {
            int k = s[i] - '0';
            if (k == 0) continue;
            if (sum >= i)
            {
                sum += k;
            }
            else
            {
                ans += i - sum;
                sum = i + k;
            }
        }
        cout<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
