#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    int t;
    scanf("%d",&t);
    for(int p=1;p<=t;p++)
    {
        int n,cnt=0,ex=-1;
        scanf("%d",&n);
        string str;
        cin>>str;
        for(ll i=0;i<=n;i++){
            if(str[i]=='0'){
                if(ex<i)
                cnt++;
            }
            else
                ex+=str[i]-'0';
        }
        printf("Case #%d: %d\n",p,cnt);
    }
}
