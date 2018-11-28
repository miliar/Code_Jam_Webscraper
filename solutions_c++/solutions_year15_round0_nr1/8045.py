#include<iostream>
#include<cstdio>
#include<cmath>
#define SIZE 1010
using namespace std;
char s[SIZE];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-out.txt","w",stdout);
    int cas,num,t,acc;
    int ans;
    cin>>cas;
for(int q=1;q<=cas;q++)
{
    cin>>num>>s;
    ans = 0;
    acc = s[0]-'0';
    for(int i=1;i<=num;i++)
    {
        if(s[i]-'0' > 0)
        {
            t = max(0,i-acc);
            ans+=t;
            acc+=s[i]-'0';
            acc+=t;
        }
       // cout<<i<<' '<<ans<<' '<<acc<<endl;

    }
    cout<<"Case #"<<q<<": "<<ans<<endl;
}
    return 0;
}
